angular.module('pages.main').factory('VacationService', ['$http', function($http) {
    return {
        getCategoryServices: function(category_slug, callback) {
            $http.get('api/v1/categories/'+category_slug+'/')
                .success(function(response) {
                    if (typeof callback == 'function')
                        callback(response);
                })
                .error(function(response) {

                });
        },
        getServices: function(serviceTypeId, callback) {
            $http.get('api/v1/service_type/'+serviceTypeId+ '/services')
            .success(function(response) {
                    if (typeof callback == 'function')
                        callback(response);
                })
                .error(function(response) {

                });
        },
        getService: function(serviceId, callback) {
            $http.get('api/v1/services/'+serviceId+'/')
            .success(function(response) {
                    if (typeof callback == 'function')
                        callback(response);
                })
                .error(function(response) {

                });
        }

    }
}]);