$.get('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:city_name%22)&format=json', function(data){
	let windSpeed = (data['query']['results']['channel']['wind']['speed'])

$('#sf_wind_speed').text(windSpeed);

});
