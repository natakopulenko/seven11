angular.module('pages.main').controller('CategoryController', ['$scope','UtilsService',
    function ($scope, utilsService) {
        $scope.servicetypes = null;
    utilsService.getCategory(function(response) {
                $scope.categories = response.data;
            });
    $scope.get_services=(function(category_id) {
            if (category_id !== null) {
                utilsService.getServiceType(category_id, function(response) {
                    $scope.servicetypes = response.data;
                });
            }
        });
     $scope.clear_services = function() {
         $scope.servicetypes = null;
     }
    }


]);