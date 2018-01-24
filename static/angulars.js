var app = angular.module("kiosks",[]);
	app.controller("main_ctrl",function($scope){
		$scope.preces = [
			{nosaukums:"Šokolāde",cena:1.99,bilde:""},
			{nosaukums:"Cepums",cena:0.45,bilde:""},
			{nosaukums:"Piena Spēks",cena:2.00,bilde:""},
			{nosaukums:"Mangalis",cena:1.49,bilde:""},
			{nosaukums:"Semkas",cena:0.99,bilde:""},
			{nosaukums:"Cigaretes",cena:2.99,bilde:""},
			{nosaukums:"Cigaretes2",cena:2.99,bilde:""},
			{nosaukums:"Cigaretes3",cena:2.99,bilde:""},
			{nosaukums:"Cigaretes4",cena:2.99,bilde:""},
			{nosaukums:"Cigaretes5",cena:2.99,bilde:""},
			{nosaukums:"Cigaretes6",cena:2.99,bilde:""},
			{nosaukums:"Cigaretes7",cena:2.99,bilde:""},
			{nosaukums:"Cigaretes8",cena:2.99,bilde:""},
		];
		$scope.hSolarijs = [
			{minutes:6,cena:1},
			{minutes:9,cena:2},
			{minutes:12,cena:3},
			{minutes:15,cena:4},
			{minutes:18,cena:5}
		];//6,9,12,15,18
		$scope.vSolarijs = [
			{minutes:4,cena:1},
			{minutes:6,cena:2},
			{minutes:9,cena:3},
			{minutes:12,cena:4},
			{minutes:15,cena:5}
		];
		$scope.izveletaisSolarijs = function(x){
		};
	});