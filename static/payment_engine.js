$(document).ready(function() {
	var discount = $(".discount[checked='checked']").attr("value"),
		allDiscounts = {discount1:0,discount2:0,discount3:0,discount4:0},
		fullPrice = Number($("#price").text()),
		value = "",
		valueDep = "",
		valueGift = "",
		valueIns = "",
		totalDiscount,
		price_After_1St,
		price_After_2nd,
		price_After_3rd,
		price_After_4th,
		wallet = Number($("#wallet").text()).toFixed(2);
	$(".discount").on("change",function(){
		discount = $(this).attr("value");
		if(discount == "false"){
			$("#disPercents").attr("disabled","disabled");
			$("#walletInput").attr("disabled","disabled");
			$("#giftCard").attr("disabled","disabled");
			$("#insurence").attr("disabled","disabled");
		}
		else{
			$("#walletInput").removeAttr("disabled");
			$("#disPercents").removeAttr("disabled");
			$("#giftCard").removeAttr("disabled");
			$("#insurence").removeAttr("disabled");
		}
	});
	$("#disPercents").on("input", function(){
		var inputValue = Number(this.value);
		if(isNaN(inputValue)){
			this.value = value;
		}
		else{
			value = inputValue;
			price_After_1St = (Number(fullPrice)/100) * inputValue;
			$("#after_1st span").text(price_After_1St.toFixed(2));
			allDiscounts.discount1 = Number(price_After_1St.toFixed(2));
		}
		count();
	});
	$("#walletInput").on("input", function(){
		var inputValue = Number(this.value),
		actualWallet;
		if(isNaN(inputValue) || inputValue > wallet || inputValue > fullPrice){
			this.value = valueDep;
		}
		else{
			actualWallet = (wallet - inputValue).toFixed(2);
			valueDep = inputValue;
			price_After_2nd = inputValue;
			$("#after_2nd").text(price_After_2nd.toFixed(2));
			$("#wallet").text(actualWallet);
			allDiscounts.discount2 = Number(price_After_2nd.toFixed(2));
		}
		count();
	});
	$("#giftCard").on("input", function(){
		var inputValue = Number(this.value);
		if(isNaN(inputValue)){
			this.value = valueGift;
		}
		else{
			valueGift = inputValue;
			price_After_3rd = inputValue;
			$("#giftCardValue").text(price_After_3rd.toFixed(2));
			allDiscounts.discount3 = Number(price_After_3rd.toFixed(2));
		}
		count();
	});
	$("#insurence").on("input", function(){
		var inputValue = Number(this.value);
		if(isNaN(inputValue)){
			this.value = valueIns;
		}
		else{
			valueIns = inputValue;
			price_After_4th = inputValue;
			$("#insurenceValue").text(price_After_4th.toFixed(2));
			allDiscounts.discount4 = Number(price_After_4th.toFixed(2));
		}
		count();
	});
	function count(){
		totalDiscount = allDiscounts.discount1 + allDiscounts.discount2 + allDiscounts.discount3 + allDiscounts.discount4;
		toPay = fullPrice - totalDiscount;
	$("#total").text("Kopējā Atlaide: " + totalDiscount.toFixed(2));
	$("#priceToPay").text("Nāksies Piemaksāt: " + toPay.toFixed(2));
	}
});