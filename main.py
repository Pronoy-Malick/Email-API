import requests

api_key = "690f81937e0e4b6bbd6f56de7db83fde"
url= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=690f81937e0e4b6bbd6f56de7db83fde"

request = requests.get(url)
contents = request.json()

for item in contents["articles"]:
    print(item["title"] + "\n")
    print(item["description"])
