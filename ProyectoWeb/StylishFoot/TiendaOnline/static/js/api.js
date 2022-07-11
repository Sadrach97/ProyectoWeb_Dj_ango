const settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://google-translate20.p.rapidapi.com/translate",
	"method": "POST",
	"headers": {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": "59fb86a085mshb53edf361496d58p18db8ajsnc728b03a920b",
		"X-RapidAPI-Host": "google-translate20.p.rapidapi.com"
	},
	"data": {
		"text": "The POST method has several advantages over GET: it is more secure because most of the request is hidden from the user; Suitable for big data operations.",
		"tl": "es",
		"sl": "en"
	}
};

$.ajax(settings).done(function (response) {
	console.log(response);
});