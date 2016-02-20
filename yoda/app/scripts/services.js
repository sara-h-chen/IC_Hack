'use strict';

angular.module('confusionApp')

.constant("baseURL", "http://localhost:3000/")
.service('menuFactory', ['$resource', 'baseURL', function($resource, baseURL) {

  var promotions = [
    {
      _id:0,
      name:'Weekend Grand Buffet',
      image: 'images/buffet.png',
      label:'New',
      price:'19.99',
      description:'Featuring mouthwatering combinations with a choice of five different salads, six enticing appetizers, six main entrees and five choicest desserts. Free flowing bubbly and soft drinks. All for just $19.99 per person ',
    }

  ];

  this.getDishes = function(){
    return $resource.get(baseULR+"dishes/:id",null,{'update':{method:'PUT'}});
  };

  this.getPromotions = function () {
    return $resource.get(baseURL+"promotions/:id",null,{'update':{method:'PUT'}});
  };

}])

.factory('corporateFactory', function() {

  var corpfac = {};

  corpfac.getLeaders = function(){
    return $resource.get(baseURL+"leadership/:id",null,{'update':{method:'PUT'}});
  };

  return corpfac;

})

;
