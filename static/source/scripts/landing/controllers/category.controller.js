angular.module('pages.main').controller('CategoryController', ['$scope','$routeParams','VacationService',
    function ($scope, $routeParams, vacationService) {
    vacationService.getCategoryServices($routeParams.categorySlug, function(response) {
                $scope.category_services = response.data;
            })
    }
]);