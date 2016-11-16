var resultDiv;

document.addEventListener("deviceready", init, false);
function init() {
	document.querySelector("#startScan").addEventListener("touchend", startScan, false);
	resultDiv = document.querySelector("#results");
}

function startScan() {

	cordova.plugins.barcodeScanner.scan(
		function (result) {
			$("#errors").html(result.text);
			var json = result.text;
			json = JSON.parse(json);
			$("#errors").html(json);

			$("#magasin").html("<h2>"+json.Magasin+"</h2>");
			$("#lieu").html("<h3>"+json.Lieu+"</h3>");
			$("#caisse").html("<h3>"+json.Caisse+"</h3>");
			$("#date").html("<h3>"+json.Date+"</h3>");
	
			json.Produits.forEach(function(prod) {
				$('#produits').append('<tr><td>'+prod.Produit+'</td><td>'+prod.Prix+'</td><td>X'+prod.Qte+'</td></tr>');
			});

			$("#total").html("<h3>Total : "+json.Total+" Euros</h3>");
			
			insertTicket(result.text,json.Date);
		}, 
		function (error) {
			alert("Scanning failed: " + error);
		}
	);

}

