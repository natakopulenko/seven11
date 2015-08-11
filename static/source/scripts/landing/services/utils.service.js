angular.module('pages.main').factory('UtilsService', ['$http', function($http) {
    return {
        getCategory: function(callback) {
            $http.get('api/v1/category/')
                .success(function(response) {
                    if (typeof callback == 'function')
                        callback(response);
                })
                .error(function(response) {
                });
        }

    }
}]);