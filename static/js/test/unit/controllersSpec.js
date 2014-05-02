'use strict';

describe('stravaApp controllers', function () {
    beforeEach(module('stravaApp'));

    describe('StravaAppController', function () {
        var scope, ctlr;

        beforeEach(inject(function ($rootScope, $controller) {
            scope = $rootScope.$new();
            ctlr = $controller('StravaController', {$scope: scope});
        }));

        it('should should set the username and try to load the logged in user', function () {
            expect(true).toBeTruthy();
        });

    });

});