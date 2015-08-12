angular.module('pages.main').controller('AlbumsController', ['$scope','AlbumsService',
    function ($scope, albumsService) {
    albumsService.getAlbums(function(response) {
                $scope.albums = response.data;
            });

    }


]);