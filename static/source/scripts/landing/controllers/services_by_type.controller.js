angular.module('pages.main').controller('ServicesByTypeController', ['$scope','$routeParams','VacationService',
    function ($scope, $routeParams, vacationService) {
    vacationService.getServices($routeParams.serviceTypeId, function(response) {
                $scope.services = response.data;
                $scope.type = response.type;
            })
    }
]);