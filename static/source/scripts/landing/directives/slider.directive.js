app.directive("slider", ["$timeout", function($timeout){
            return {
                restrict: 'A',
                link: function(scope, element, attrs) {
                    element.addClass("slider");
                    $timeout(function(){
                    	element.slider();
                    });

                }
            };
        }]);