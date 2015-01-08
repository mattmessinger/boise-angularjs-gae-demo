boise-angularjs-gae-demo
========================

Google App Engine demo for Boise AngularJS meetup


This project is made up of two components: 
1.  ui - this is a angularjs app that runs the ui  
2.  server - this is a python app that hosts the ui and api server


To build and run the UI
-----------------------

### one time setup
  > $ cd ui  
  > $ npm install   
  > $ bower install 

### run the UI with node server (ui dev only)
  > $ grunt serve

### build the UI for running with backend. this puts the "dist" folder in git/boise-angularjs-gae-demo/server/web.
  > $ grunt build --force


To build and run the server
---------------------------

### one time setup
1. Install Google App Engine SDK for Python: https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python
2. Create a new GCP Project: https://cloud.google.com/  
3. Edit the server/app.yaml file - change "application: XXXXX" to the  "Project ID" your GCP Project
 
 
### run the local development server
 > $ cd git/boise-angularjs-gae-demo  
 > $ ~/google_appengine/dev_appserver.py server
  
### deploy to production
 > $ cd git/boise-angularjs-gae-demo  
 > $ ~/google_appengine/appcfg.py update  server
