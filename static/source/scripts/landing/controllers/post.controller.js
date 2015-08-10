angular.module('pages.main').controller('PostController', ['$scope','$routeParams','BlogService',
    function ($scope, $routeParams, blogService) {
    blogService.getPost($routeParams.postId, function(response) {
                $scope.post = response.data;
            })
    }
]);