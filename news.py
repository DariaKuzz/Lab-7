import requests
import json
from datetime import datetime

news_url = ('https://newsapi.org/v2/everything?'
'q=tesla&sortBy=publishedAt&apiKey={}&from={}')

def article(num):
    today = datetime.now().strftime('%d-%m-%Y')
    url = news_url.format(api_key, today)
    response = requests.get(url)
    result = json.loads(response.text)
    res = result['articles'][num]
    return f'''
Author: {res['author']}
Title: {res['title']}
Description: {res['description']}
URL: {res['url']}
Published at: {res['publishedAt']}
'''

if __name__ == "__main__":
    api_key = 'c7beaf51487949d4a75ae2764a3ab63d'
    for k in range(1, 6):
        print(article(k))
