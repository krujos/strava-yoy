'use strict';

var stravaApp = angular.module('stravaApp', ['ui.bootstrap']);

// Main app controller.
stravaApp.controller('StravaController', function StravaController($scope, $http) {
    $scope.login = function () {
        window.location.replace('/login');
    };
});

stravaApp.controller('UserController', function UserController($scope, $http) {

    $scope.username = "loading....";

    $scope.today = function() {
        $scope.dt = new Date();
    };
    $scope.today();

    $scope.clear = function () {
        $scope.dt = null;
    };

    $scope.open = function($event) {
        $event.preventDefault();
        $event.stopPropagation();
        $scope.opened = true;
    };

    $scope.dateOptions = {
        formatYear: 'yy',
        startingDay: 1
    };

    $scope.initDate = new Date('2016-15-20');
    $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
    $scope.format = $scope.formats[0];


});

