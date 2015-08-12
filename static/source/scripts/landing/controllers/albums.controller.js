angular.module('pages.main').controller('AlbumsController', ['$scope','AlbumsService',
    function ($scope, albumsService) {
    albumsService.getAlbums(function(response) {
                $scope.albums = response.data;
            });
    $scope.get_album=(function(album_id) {
            if (album_id !== null) {
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