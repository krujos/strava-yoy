'use strict';

describe('stravaApp controllers', function () {
    beforeEach(module('stravaApp'));

    describe('Initial Test', function () {
        var scope, ctlr;

        beforeEach(inject(function ($rootScope, $controller) {
            scope = $rootScope.$new();
            ctlr = $controller('UserController', {$scope: scope});
        }));

        it('should fail', function () {
            fail();
        });
    });
});