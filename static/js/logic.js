
var Application = angular.module('Application', ['ngSanitize', 'ui.bootstrap', 'monospaced.elastic', 'angular-clipboard']).config(function($httpProvider, $locationProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});


Application.controller('Paste_system', ['$scope', '$http', '$timeout', '$location', function ($scope, $http, $timeout, $location) {

    //$scope.state_alert = false;

/*
    Alert system:
*/

    $scope.alerts = [];

        $scope.addAlert = function(msg, type, show_time, url) {
            $scope.alerts.splice(0, 1);
            $scope.alerts.push({type: type, msg: msg});
            $scope.url_to_copy = url;
        };

      $scope.closeAlert = function(index) {
        $scope.alerts.splice(index, 1);
      };
    //
    //var stop_alert = function (){
    //    $scope.state_alert = false;
    //    console.log("dwa");
    //};
    //var run_alert = function (content, type, show_time){
    //    $scope.state_alert = true;
    //
    //    $scope.alert = content;
    //    $scope.alert_type = type;
    //    $timeout(function(){stop_alert();}, show_time);
    //};

/*
    End Alert system
*/


/*
    All inset
*/
    $scope.show_all_inset = function(){
        console.log("wysłano");
        console.log($scope.bigCurrentPage);
        var success = function(response){
            //console.log(response.data);
            $scope.show_all_inset.insets = response.data.results;
            $scope.bigTotalItems = response.data.count;

            //run_alert("Pobrano...", "success", 1500);
        };
        var error = function(reason){
            //run_alert("Nastąpił błąd przy pobieraniu.", "error", 1500)
        };
        $http.get("/api/v1/Insets/?page=" + $scope.bigCurrentPage).then(success, error);
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
                $scope.addAlert("<strong>You sent</strong>, URL is: <a href='"+$location.absUrl()+"show_inset/-1-" + response.data.url_private + "'>"+$location.absUrl()+"show_inset/-0-"+response.data.url_private+"</a>", "success", 5000, $location.absUrl()+"show_inset/-1-"+response.data.url_private);
            }else{
                $scope.addAlert("<strong>You sent</strong>, URL is: <a href='"+$location.absUrl()+"show_inset/-0-" + response.data.id + "'>"+$location.absUrl()+"show_inset/-0-"+response.data.id+"</a>", "success", 5000, $location.absUrl()+"show_inset/-0-"+response.data.id);
            }
        };
        var error = function(response){
            $scope.addAlert("Nastąpił błąd przy wysyłaniu.", "danger", 1500)
        };
        $http.post("/api/v1/Insets/",
            {
                "content": content,
                "private": priv

            }).then(success, error);
    };


//$scope.state_alert = false;
$scope.bigCurrentPage = 1;
$scope.inset_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam id turpis eget metus lobortis finibus. Nullam lectus ante, bibendum vitae dolor quis, tincidunt faucibus metus. Aenean vehicula aliquet sem. Nulla sem lectus, aliquet at lacus non, tristique ornare sem. Proin convallis aliquet urna sed varius. Morbi ornare risus arcu, sit amet congue eros blandit a. Aenean pellentesque id dolor eget rhoncus. Morbi vestibulum eros non nunc vulputate venenatis. Praesent ipsum eros, posuere sed porttitor sit amet, fermentum elementum purus. Sed odio ex, ultricies eget rutrum in, lacinia eu turpis";
}]);

/*
    End inset
*/

