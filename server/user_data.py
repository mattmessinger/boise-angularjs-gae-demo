from google.appengine.ext import ndb

class User(ndb.Model):
    firstname = ndb.StringProperty()
    lastname = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    email = ndb.StringProperty()


class UserService:

    @staticmethod
    def get_user(user_id_str):
        return User.get_by_id(user_id_str)

    @staticmethod
    def get_or_create_user(user_id_str, user_email):
        curr_user = User.get_by_id(user_id_str)
        if curr_user is None:
            curr_user = User(id=user_id_str)
            curr_user.email = user_email
            curr_user.put()
        return curr_user