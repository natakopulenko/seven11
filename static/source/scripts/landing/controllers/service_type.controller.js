angular.module('pages.main').controller('ServiceTypeController', ['$scope','UtilsService',
    function ($scope, utilsService) {



        $scope.$watch(function(newValue) {
            if (newValue !== null) {
                utilsService.getServiceType( function(response) {
                    $scope.servicetypes = response.data;
                });
            }
        });

    }
]);