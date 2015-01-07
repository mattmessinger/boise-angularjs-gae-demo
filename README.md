boise-angularjs-gae-demo
========================

Google App Engine demo for Boise AngularJS meetup


This project is made up of two components:

 ui - this is a angularjs app that runs the ui
 server - this is a python app that hosts the ui and api server


Development:

UI: 

 To build and run the UI:

  # one time setup
  > cd ui
  > npm install 
  > bower install 

  # run the UI with node server (ui dev only)
  > grunt serve

  # build the UI for running with backend. this puts the "dist" folder in git/segment/server/web.
  > grunt build --force

Server:

 To build and run the server:

  # one time setup
  Install Google App Engine SDK for Python: https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python
  
  # run the local development server:
  > cd git/segment
  
  # build the UI as described above
  > ~/google_appengine/dev_appserver.py server