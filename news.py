import requests
import json

k = 0

response = requests.get(f'https://newsapi.org/v2/everything?q=tesla&from=2025-02-11&sortBy=publishedAt&apiKey=c7beaf51487949d4a75ae2764a3ab63d')
result = json.loads(response.text)

def article(num):
    res = result['articles'][num]
    return f'''
Author: {res['author']}
Title: {res['title']}
Description: {res['description']}
URL: {res['url']}
Published at: {res['publishedAt']}
'''

if __name__ == "__main__":
    key = 'c7beaf51487949d4a75ae2764a3ab63d'
    while k < 5:
        print(article(k))
        k += 1
