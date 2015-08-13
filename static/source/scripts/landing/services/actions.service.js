angular.module('pages.main').factory('ActionsService', ['$http', function($http) {
    return {
        getActions: function(callback) {
            $http.get('api/v1/actions/')
                .success(function(response) {
                    if (typeof callback == 'function')
                        callback(response);
                })
                .error(function(response) {
                });
        },
        getAction: function(action_id, callback) {
            $http.get('api/v1/action/' + action_id)
                .success(function(response) {
                    if (typeof callback == 'function')
                        callback(response);
                })
                .error(function(response) {

                });
        }
    }
}]);