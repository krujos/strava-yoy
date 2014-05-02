'use strict';

var stravaApp = angular.module('stravaApp', []);

// Main app controller.
stravaApp.controller('StravaController', function StravaController($scope, $http) {

    $scope.username = '...';

    $scope.login = function () {
        window.location.replace('/login');
    };

    $scope.loadUser = function() {
        $scope.loadUser = function() {
            $http.get('/athlete').success(function (data) {
                $scope.athlete_info = data;
                $scope.username = data.name
            });
        };
    }
});


