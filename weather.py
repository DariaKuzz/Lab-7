import requests
import json

city_name = input('Please, write down the name '
'of the city. For instance,  Madrid: ')
weather_url = ('https://api.openweathermap.org/data/2.5/weather?'
'q={}&appid={}&units=metric')

def weather(city_name, api_key):
    url = weather_url.format(city_name, api_key)
    response = requests.post(url)
    result = json.loads(response.text)
    return f'''The weather in {city_name}: {(result['weather'][0]\
['main']).lower()}(more descriptions: {result['weather'][0]['description']})
The humidity: {result['main']['humidity']}
The pressure: {result['main']['pressure']}'''


if __name__ == "__main__":
    api_key = '2f44ab8d94825710392977b37c24d3ac'
    print(weather(city_name, api_key))
 