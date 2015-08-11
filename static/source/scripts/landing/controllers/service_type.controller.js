angular.module('pages.main').controller('ServiceTypeController', ['$scope','UtilsService',
    function ($scope, utilsService) {



        $scope.get_services= function(category_id) {

                utilsService.getServiceType(category_id, function(response) {
                    $scope.servicetypes = response.data;
                });

        };

    }
]);