'use strict';

describe('stravaApp controllers', function () {
    beforeEach(module('stravaApp'));

    describe('StravaAppController', function () {
        var scope, ctlr;

        beforeEach(inject(function ($rootScope, $controller) {
            scope = $rootScope.$new();
            ctlr = $controller('StravaController', {$scope: scope});
        }));

        it('should pass', function () {
            expect(true).toBeTruthy();
        });

    });

});