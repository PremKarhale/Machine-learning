import requests

url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
	"x-rapidapi-key": "710be8f1aemsh011743b33311529p18feeejsn3347a34e41ee",
	"x-rapidapi-host": "imdb-top-100-movies.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())