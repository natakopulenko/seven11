app.directive('sideNav', function() {
    return {
        restrict: 'A',

        link: function(scope, element) {
            angular.element(element).sideNav();
        }
    }
});