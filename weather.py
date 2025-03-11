import requests
import json

city_name = input('Please, write down the name of the city. For instance,  Madrid: ')

def weather(city_name, key):
    response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
    result = json.loads(response.text)
    return f'''The weather in {city_name}: {(result['weather'][0]['main']).lower()} (more descriptions: {result['weather'][0]['description']})
The humidity: {result['main']['humidity']}
The pressure: {result['main']['pressure']}'''


if __name__ == "__main__":
    key = '2f44ab8d94825710392977b37c24d3ac'
    print(weather(city_name, key))
