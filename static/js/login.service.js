 (function(){
      'use strict';

       angular
            .module('scrumboard.demo')
            .service('Login', [ '$http', '$location' ,  Login ]);

       function Login($http, $location){

          this.login = login;
          this.isloggedIn = isloggedIn;
          this.logout = logout;
          this.redirectIfNotLoggedIn = redirectIfNotLoggedIn;

          function login(credentials){
                return $http.post('/auth_api/login/',credentials)
                    .then(function(response){
                        localStorage.currentUser = JSON.stringify(response.data);
                    });
          }

          function isloggedIn(){
                return !!localStorage.currentUser;
          }

          function logout(){
                delete localStorage.currentUser;
                $http.get('/auth_api/logout/')
                    .then(function(){
                        $location.url('/login');
                    });
          }

          function redirectIfNotLoggedIn(){
                if (!isloggedIn()){
                    $location.url('/login');
                }
          }

       }

})();