angular.module('pages.main').controller('CategoryController', ['$scope','UtilsService',
    function ($scope, utilsService) {
    utilsService.getCategory(function(response) {
                $scope.categories = response.data;
            })
    }
]);