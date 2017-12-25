from flask import Flask, render_template
app = Flask(__name__)

import requests

NEWS_API_URL = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=cbdb357849b049ef9bd771a456536e5e"

def get_news_articles():
    # fetch the news data from news api
    response = requests.get(NEWS_API_URL)

    # return the articles in json format
    return response.json()['articles']

@app.route("/")
def index():
    news_articles = get_news_articles()
    return render_template('index.html',
                           articles=news_articles)


