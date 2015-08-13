angular.module('pages.main').controller('AlbumsController', ['$scope','AlbumsService',
    function ($scope, albumsService) {
    albumsService.getAlbums(function(response) {
                $scope.albums = response.data;
            });
    $scope.get_album=(function(album_id) {
            if (album_id !== null) {
                AlbumsService.getAlbum(album_id, function(response) {
                    $scope.album = response.data;
                });
            }
        });
     $scope.clear_services = function() {
         $scope.album = null;
     }
    }


]);