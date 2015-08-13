angular.module('pages.main').controller('ActionsController', ['$scope','ActionsService',
    function ($scope, actionsService) {
    actionsService.getActions(function(response) {
                $scope.actions = response.data;
            });

    }


]);