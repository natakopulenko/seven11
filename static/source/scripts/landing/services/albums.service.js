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
        }

    }
}]);