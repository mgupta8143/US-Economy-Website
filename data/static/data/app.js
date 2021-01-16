/*var xmlHttp = new XMLHttpResponse();
xmlHttp.open("GET", 'https://www.investing.com/currencies/', false);
xmlHttp.send(null);
var element = document.getElementById("stuck");
alert(xmlHttp.responseText);
request.responseType = 'text';
element.innerHTML = xmlHttp.responseText;*/



var interval =0 ; //every 10 seconds scrapes from data-rates which in turn scrapes every 5 minutes or so from yahoo finacne
x = 0

 function doAjax() {
 	$.ajax({
	    type: "get",
	    url: "http://localhost:8000/data-rates",
	    dataType: 'html',
	    success: function(response) {
	    	arr = $.parseHTML(response);
	    	interval = 60000;
	    	//$("#EUR-USD-ROW")
	    	update("EUR-USD", arr, 5, "EUR-USD-ROW");
	    	update("Bitcoin-USD", arr, 7, "Bitcoin-USD-ROW");
	    	update("Ethereum-USD", arr, 9, "Ethereum-USD-ROW");
	    	update("USD-JPN", arr, 11, "USD-JPN-ROW");
	    	update("GBP-USD", arr, 13, "GBP-USD-ROW");
	    	update("AUD-USD", arr, 15, "AUD-USD-ROW");
	    	update("NZD-USD", arr, 17, "NZD-USD-ROW");
	    	update("USD-CNY", arr, 19, "USD-CNY-ROW");
	    	update("USD-HKD", arr, 21, "USD-HKD-ROW");
	    	update("USD-SGD", arr, 23, "USD-SGD-ROW");
	    	update("USD-INR", arr, 25, "USD-INR-ROW");
	    	update("USD-MXN", arr, 27, "USD-MXN-ROW");
	    	update("USD-PHP", arr, 29, "USD-PHP-ROW");
	    	update("USD-IDR", arr, 31, "USD-IDR-ROW");
	    	update("USD-THB", arr, 33, "USD-THB-ROW");
	    	update("USD-MYR", arr, 35, "USD-MYR-ROW");
	    	update("USD-ZAR", arr, 37, "USD-ZAR-ROW");
	    	update("USD-RUB", arr, 39, "USD-RUB-ROW");
	    	changeUpdate('EUR-USD-CHANGE', arr, 41);
	    	changeUpdate('Bitcoin-USD-CHANGE', arr,43);
	    	changeUpdate('Ethereum-USD-CHANGE', arr, 45);
	    	changeUpdate('USD-JPN-CHANGE', arr, 47);
	    	changeUpdate('GBP-USD-CHANGE', arr, 49);
	    	changeUpdate('AUD-USD-CHANGE', arr, 51);
	    	changeUpdate('NZD-USD-CHANGE', arr, 53);
	    	changeUpdate('USD-CNY-CHANGE', arr, 55);
	    	changeUpdate('USD-HKD-CHANGE', arr, 57);
	    	changeUpdate('USD-SGD-CHANGE', arr, 59);
	    	changeUpdate('USD-INR-CHANGE', arr, 61);
	    	changeUpdate('USD-MXN-CHANGE', arr, 63);
	    	changeUpdate('USD-PHP-CHANGE', arr, 65);
	    	changeUpdate('USD-IDR-CHANGE', arr, 67);
	    	changeUpdate('USD-THB-CHANGE', arr, 69);
	    	changeUpdate('USD-MYR-CHANGE', arr, 71);
	    	changeUpdate('USD-ZAR-CHANGE', arr, 73);
	    	changeUpdate('USD-RUB-CHANGE', arr, 75);
	    	percentChangeUpdate('EUR-USD-CHANGE-PERCENT', arr, 77);
	    	percentChangeUpdate('Bitcoin-USD-CHANGE-PERCENT', arr, 79);
	    	percentChangeUpdate('Ethereum-USD-CHANGE-PERCENT', arr, 81);
	    	percentChangeUpdate('USD-JPN-CHANGE-PERCENT', arr, 83);
	    	percentChangeUpdate('GBP-USD-CHANGE-PERCENT', arr, 85);
	    	percentChangeUpdate('AUD-USD-CHANGE-PERCENT', arr, 87);
	    	percentChangeUpdate('NZD-USD-CHANGE-PERCENT', arr, 89);
	    	percentChangeUpdate('USD-CNY-CHANGE-PERCENT', arr, 91);
	    	percentChangeUpdate('USD-HKD-CHANGE-PERCENT', arr, 93);
	    	percentChangeUpdate('USD-SGD-CHANGE-PERCENT', arr, 95);
	    	percentChangeUpdate('USD-INR-CHANGE-PERCENT', arr, 97);
	    	percentChangeUpdate('USD-MXN-CHANGE-PERCENT', arr, 99);
	    	percentChangeUpdate('USD-PHP-CHANGE-PERCENT', arr, 101);
	    	percentChangeUpdate('USD-IDR-CHANGE-PERCENT', arr, 103);
	    	percentChangeUpdate('USD-THB-CHANGE-PERCENT', arr, 105);
	    	percentChangeUpdate('USD-MYR-CHANGE-PERCENT', arr, 107);
	    	percentChangeUpdate('USD-ZAR-CHANGE-PERCENT', arr, 109);
	    	percentChangeUpdate('USD-RUB-CHANGE-PERCENT', arr, 111);
	    	document.getElementById('USDX').innerHTML = "United States Dollar Index: " + parseFloat(arr[113].innerHTML).toFixed(2);
	    	if(parseFloat(arr[113].innerHTML).toFixed(2) > 102) {
	    		$(".USDX-background").addClass('bg-success');
	    		document.getElementById('USDX_RATING').innerHTML = "<strong>We currently have a strong dollar according to this index.</strong>";

	    	}
	    	else if (parseFloat(arr[113].innerHTML).toFixed(2) > 95) {
	    		$(".USDX-background").addClass('bg-success');
	    		document.getElementById('USDX_RATING').innerHTML = "<strong>We currently have a neither particularly strong nor weak dollar according to this index.<strong>";
	    	}
	    	else {
	    		document.getElementById('USDX_RATING').innerHTML = "<strong>We currently have a weakening dollar according to this index.</strong>";
	    		$(".USDX-background").removeClass('bg-success');
	    		$(".USDX-background").css('background', 'red');
	    	}	
	        console.log("Currency Rates Updated!");
	        x++;
	    },
	    complete: function (data) {
            setTimeout(doAjax, interval);
        }
 
 	});
 	//alert("updated");
 }

 function changeUpdate(str, arr, i) {
 	document.getElementById(str).innerHTML = parseFloat(arr[i].innerHTML).toFixed(4);
 	if (parseFloat(arr[i].innerHTML) > 0) {
 		$("#" + str).css('color', '#90ee90');
 		document.getElementById(str).innerHTML = "+" + parseFloat(arr[i].innerHTML).toFixed(4);

 	}
 	else if (parseFloat(arr[i].innerHTML) < 0)
 	{
 		$("#" + str).css('color', '#ff5252');
 		 document.getElementById(str).innerHTML = parseFloat(arr[i].innerHTML).toFixed(4);
 	}
 	 $("#" + str).css('font-weight', 'bold');

 }

 function percentChangeUpdate(str, arr, i) {
 	document.getElementById(str).innerHTML = parseFloat(arr[i].innerHTML).toFixed(4);
 	if (parseFloat(arr[i].innerHTML) > 0) {
 		$("#" + str).css('color', '#90ee90');
 		 document.getElementById(str).innerHTML = "+" + parseFloat(arr[i].innerHTML).toFixed(4) + "%";
 	}
 	else if (parseFloat(arr[i].innerHTML) < 0)
 	{
 		$("#" + str).css('color', '#ff5252');
 		document.getElementById(str).innerHTML = parseFloat(arr[i].innerHTML).toFixed(4) + "%";
 	}
 	 $("#" + str).css('font-weight', 'bold');

 }

 function update(str, arr, i, str2) {
 	if (x != 0) {
 	if (parseFloat(document.getElementById(str).innerHTML) < parseFloat(arr[i].innerHTML))
 	{
 		$("." + str2).addClass("bg-success");
 		setTimeout(function(){
			 $("." + str2).removeClass("bg-success")
		},1000);

 	}
 	else if (parseFloat(document.getElementById(str).innerHTML) > parseFloat(arr[i].innerHTML)) 
 	{
 		$("." + str2).addClass("bg-danger");
 		setTimeout(function(){
			 $("." + str2).removeClass("bg-danger")
		},1000);
 	}
 }
 	document.getElementById(str).innerHTML = parseFloat(arr[i].innerHTML).toFixed(4);
 	$("#" + str).css('font-weight', 'bold');

 }

setTimeout(doAjax, interval);




