app.directive('slider', function() {
    return {
        restrict: 'A',

        link: function(scope, element) {
            angular.element(element).slider();
        }
    }
});