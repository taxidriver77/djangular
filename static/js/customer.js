            (function(){
                'use strict';

                 angular.module('scrumboard.demo',['ngRoute'])
                    .controller('CustomerController',
                        [ '$scope', '$http','Login', CustomerController ]);

                 function CustomerController($scope, $http , Login ){

                   var request = {

                        // https://bo.zelty.fr/app_api/1.0/<service>
                        // service : POST /customer[/<customer_id>]
                        // service : GET /customers
                        //API Key : 28f84ccd190145f5b9e460c565643873dbc8617f

                         method: 'GET',
                         url: 'https://bo.zelty.fr/app_api/1.0/customers',
                         headers: {
                               'x-api-key': '28f84ccd190145f5b9e460c565643873dbc8617f'
                         }
                   }
                   $scope.data = [];

                   $http.get(request).then(function(response){
                        $scope.data = response.data;
                   });


                 }
            }());