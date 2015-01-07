import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

from google.appengine.api import mail

import jinja2
import webapp2
import user_data
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))




class MainPage(webapp2.RequestHandler):

    def get(self):

        login_url = "null"
        logout_url = "null"
        curr_user_str = "null"

        curr_user = users.get_current_user()
        if curr_user:
            curr_user = user_data.UserService.get_or_create_user(user_id_str=curr_user.user_id(), user_email=curr_user.email())
            curr_user_str = json.dumps(curr_user.to_dict())
            logout_url = users.create_logout_url(self.request.uri)
        else:
            login_url = users.create_login_url(self.request.uri)

        template_values = {
            'btSelf': curr_user_str,
            'btLoginUrl': login_url,
            'btLogoutUrl': logout_url,
        }

        template = JINJA_ENVIRONMENT.get_template('dist/index.html')
        self.response.write(template.render(template_values))


class UserApi(webapp2.RequestHandler):

    def post(self):

        curr_user = users.get_current_user()
        if curr_user.user_id is None:
            self.abort(401)
            return

        user = user_data.UserService.get_user(user_id_str=curr_user.user_id())

        u = json.loads(self.request.body)
        user.city = u["city"]
        user.state = u["state"]
        user.firstname = u["firstname"]
        user.lastname = u["lastname"]
        user.put()

        # send email to user
        mail.send_mail(sender="matthew.messinger@gmail.com",
                   to=curr_user.email(),
                   subject="Profile updated",
                   body="Name:" + user.firstname + " " + user.lastname)

        # return user object
        json_str = json.dumps(user.to_dict())
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json_str)



application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/profile', UserApi),
], debug=True)
