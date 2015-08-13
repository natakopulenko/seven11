angular.module('pages.main').controller('AlbumController', ['$scope','$routeParams','AlbumsService',
    function ($scope, $routeParams, albumsService) {
    albumsService.getAlbum($routeParams.albumID, function(response) {
                $scope.album = response.data;
            });

    }


]);