import requests

api_key = "866b896303d2470fbe461eea7c1db3dd"
url ="https://newsapi.org/v2/everything?q=tesla&from=2023-07-02&sortBy=publishedAt&apiKey=866b896303d2470fbe461eea7c1db3dd"

# Make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

