angular.module('pages.main').factory('AlbumsService', ['$http', function($http) {
    return {
        getAlbums: function(callback) {
            $http.get('api/v1/albums/')
                .success(function(response) {
                    if (typeof callback == 'function')
                        callback(response);
                })
                .error(function(response) {
                });
        },
        getAlbum: function(album_id, callback) {
            $http.get('api/v1/album/' + album_id)
                .success(function(response) {
                    if (typeof callback == 'function')
                        callback(response);
                })
                .error(function(response) {

                });
        }
    }
}]);