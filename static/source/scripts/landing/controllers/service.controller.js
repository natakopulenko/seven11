angular.module('pages.main').controller('ServiceController', ['$scope','$routeParams','VacationService',
    function ($scope, $routeParams, vacationService) {
    vacationService.getService($routeParams.serviceId, function(response) {
                $scope.service = response.data;
            })
    }
]);