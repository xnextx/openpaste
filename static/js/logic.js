
var Application = angular.module('Application', []).config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
});


Application.controller('Paste_system', function ($scope, $http, $timeout) {
    $scope.variable = "Jakaś treść";


  });