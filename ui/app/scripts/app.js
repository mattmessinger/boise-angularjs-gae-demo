'use strict';

angular
  .module('uiApp', [
    'ngCookies',
    'ngResource',
    'ngSanitize',
    'ngRoute'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })

  // here is the piece of angularjs code that is awesome (assuming you are not using angular ui router)
  .run( function($rootScope, $window) {
    $rootScope.$on('$routeChangeSuccess', function () {
      $window.scrollTo(0, 0);    //scroll to top of page after each route change
    });
  });
