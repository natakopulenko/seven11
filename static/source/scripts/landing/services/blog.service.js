angular.module('pages.main').factory('BlogService', ['$http', function($http) {
    return {
        getPosts: function(callback) {
            $http.get('api/v1/blog/')
                .success(function(response) {
                    if (typeof callback == 'function')
                        callback(response);
                })
                .error(function(response) {

                });
        },
        getPost: function(post_id, callback) {
            $http.get('api/v1/posts/'+post_id+'/')
                .success(function(response) {
                    if (typeof callback == 'function')
                        callback(response);
                })
                .error(function(response) {

                });
        }

    }
}]);