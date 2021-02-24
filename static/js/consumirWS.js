var app= angular.module('AppWS', []);
app.controller('ControladorAppWs' ,['$scope','$http',function($scope,$http){
  $scope.saludo= "hola michael"
  $http({
    method: "GET",
    url: "http://jsonplaceholder.typicode.com/posts"
  }).then(function correcto(response) {
    $scope.posts=response.data;
  },function incorrecto(response){
    //dato error
  });
}]);
