
var Application = angular.module('Application', ['ngSanitize', 'ui.bootstrap']).config(function($httpProvider) {
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
    All inset
*/
    $scope.show_all_inset = function(){
        console.log("wysłano");

        var success = function(response){
            //console.log(response.data);
            $scope.show_all_inset.insets = response.data;

            //run_alert("Pobrano...", "success", 1500);
        };
        var error = function(reason){
            //run_alert("Nastąpił błąd przy pobieraniu.", "error", 1500)
        };
        $http.get("/api/v1/Insets/").then(success, error);
    };
/*
    End All inset
*/

/*
    Send inset
*/
    $scope.send_inset = function(content, priv)    {
        var success = function(response){
            if(response.data.private == true){
                run_alert("Wysłano..., adres to: <a href='/show_inset/-1-" + response.data.url_private + "'>/show_inset/-0-"+response.data.url_private+"</a>", "success", 5000);
            }else{
                run_alert("Wysłano..., adres to: <a href='/show_inset/-0-" + response.data.id + "'>/show_inset/-0-"+response.data.id+"</a>", "success", 5000);
            }
        };
        var error = function(response){
            run_alert("Nastąpił błąd przy wysyłaniu.", "error", 1500)
        };
        $http.post("/api/v1/Insets/",
            {
                "content": content,
                "private": priv

            }).then(success, error);
    };


});

$scope.state_alert = false;
/*
    End inset
*/

