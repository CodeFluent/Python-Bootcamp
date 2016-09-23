$(document).ready(function() {
	var searchQuery = getUrlVars()["query"];

	if (searchQuery) {
		console.log(searchQuery);
		if (searchQuery == "harambe") {
			$('#harambe').prepend('<b><p>404 Gorrilla Not Found</p></b>').prepend('<img id="theImg" src="http://s-media-cache-ak0.pinimg.com/564x/15/0f/17/150f17b70e5c6363718e04d9fb21aad3.jpg" />')

		} else {

		$.get("http://www.omdbapi.com/?s=" + searchQuery, function(data){
			 console.log(data);

		}) }
	}
});



// Read a page's GET URL variables and return them as an associative array
function getUrlVars() {
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++) {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}
