angular.module('pages.main').controller('ActionController', ['$scope','$routeParams','ActionsService',
    function ($scope, $routeParams, actionsService) {
    actionsService.getAction($routeParams.actionId, function(response) {
                $scope.action = response.data;
            });

    }


]);