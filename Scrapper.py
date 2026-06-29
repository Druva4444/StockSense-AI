import requests
from DB import get_connection
from datetime import date
from dotenv import load_dotenv
load_dotenv()
import os
conn = get_connection()
cur = conn.cursor()
API_key= os.getenv("NEWS_API")
cur.execute("""
CREATE TABLE IF NOT EXISTS article (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT,
    description TEXT,
    content TEXT,
    source TEXT,
    site TEXT
)
""")
conn.commit()

def writeDB(text):
    today = date.today().isoformat()
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": text,
        "from": "2026-06-28",
        "sortBy": "popularity",
        "apiKey": API_key
    }

    response = requests.get(url, params=params)
   
    articles = response.json()['articles']
    
    for article in articles:
        title = article['title']
        author = article['author']
        description = article['description']
        content = article['content']
        source = article['source']['name']
        site =article['publishedAt']
        cur.execute("INSERT INTO article (title, author, description,content,source,site) VALUES (%s, %s, %s, %s, %s, %s)", (title, author, description,content,source,site))

    conn.commit()
    