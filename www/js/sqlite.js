//Fonctions SQLites
var db = null;
var historique = null;


db = window.openDatabase("ecoticket", "2.0", "Test DB", 1000000); 

db.transaction(function(tx) {
	tx.executeSql('SELECT * FROM ticket', [], function(tx, rs) {
		historique = rs.rows;
	}, function(tx, error) {
		console.log('SELECT error: ' + error.message);
	});
});

function insertTicket(json,date)
{
	db.transaction(function(tx) {
		tx.executeSql('CREATE TABLE IF NOT EXISTS ticket (json, date)');
		tx.executeSql('INSERT INTO ticket VALUES (?,?)', [json, date]);
	}, function(error) {
		console.log('Transaction ERROR: ' + error.message);
	}, function() {
		console.log('Populated database OK');
	});
}

