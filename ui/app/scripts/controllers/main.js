'use strict';

angular.module('uiApp')
  .controller('MainCtrl', function ($scope, $http) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    $scope.self = self;
    $scope.loginUrl = loginUrl;
    $scope.logoutUrl = logoutUrl;

    $scope.user = angular.copy($scope.self);

    $scope.submitting = false;
    $scope.update = function(user) {

      $scope.submitting = true;
      $scope.message = null;

      $http.post('profile', user)
        .success(function() {

          $scope.self = angular.copy(user);

          $scope.message = "Success!"
          $scope.submitting = false;
        })
        .error (function() {
          $scope.message = "Error"
          $scope.submitting = false;
        });

    };

  });
