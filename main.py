import requests
from send_email import send_email

api_key = "690f81937e0e4b6bbd6f56de7db83fde"
url= ("https://newsapi.org/v2/top-headlines?"
      "sources=techcrunch&"
      "apiKey=690f81937e0e4b6bbd6f56de7db83fde&"
      "language=en")

request = requests.get(url)
contents = request.json()

body = "Subject: Today's News\n"
for item in contents["articles"][:20]:
    if item["title"] is not None:
        body = body \
                + item["title"] + "\n" + item["description"] + "\n" \
                + item["url"] + 2*"\n"


body = body.encode("utf-8")
send_email(message= body)


