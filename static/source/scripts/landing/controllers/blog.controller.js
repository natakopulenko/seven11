angular.module('pages.main').controller('BlogController', ['$scope','BlogService',
    function ($scope, blogService) {
    blogService.getPosts(function(response) {
                $scope.posts = response.data;
            })
    }
]);