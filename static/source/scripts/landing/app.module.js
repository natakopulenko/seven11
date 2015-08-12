var app = angular.module('pages.main', [
    'ngRoute'
]);
app.config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}]);

app.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.config(function ($routeProvider, $locationProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'ajax/templates/landing/'
        })
        .when('/blog/', {
            templateUrl: 'ajax/templates/blog/'
        })
        .when('/vacation/', {
            templateUrl: 'ajax/templates/vacation/'
        })
        .when('/albums/', {
            templateUrl: 'ajax/templates/albums/'
        })
        .when('/categories/:categorySlug/', {
            templateUrl: 'ajax/templates/category/'
        })
        .when('/blog/posts/post:postId/', {
            templateUrl: 'ajax/templates/post/'
        })
        .when('/service_type/:serviceTypeId/services/', {
            templateUrl: 'ajax/templates/service_type/'
        })
        .when('/services/:serviceId/', {
            templateUrl: 'ajax/templates/service/'
        })
        .when('/login/', {
            templateUrl: 'login/'
        })
        .when('/albums/', {
            templateUrl: 'ajax/templates/albums/'
        });

    // configure html5 to get links working on jsfiddle
    $locationProvider.hashPrefix('!');
});