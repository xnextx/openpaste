
var Application = angular.module('Application', []).config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
});


Application.controller('Paste_system', function ($scope, $http, $timeout) {

    $scope.state_alert = false;

/*
    Alert system:
*/

    var stop_alert = function (){
        $scope.state_alert = false;
        console.log("dwa");
    };
    var run_alert = function (content, type, show_time){
        $scope.state_alert = true;
        $scope.alert = content;
        $scope.alert_type = type;
        $timeout(function(){stop_alert();}, show_time);
    };

/*
    End Alert system
*/

/*
    Send inset
*/
    $scope.send_inset = function(content, priv)    {
        console.log("wysłano");

        var success = function(response){
            run_alert("Wysłano...", "success", 1500)
        };
        var error = function(response){
            run_alert("Nastąpił błąd przy wysyłaniu.", "error", 1500)
        };
        $http.post("/api/v1/Insets/",
            {
                "content": content,
                "private": priv

            }).then(success, error);
    }
});
/*
    End inset
*/