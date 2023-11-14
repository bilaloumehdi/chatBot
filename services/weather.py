import requests

def get_weather(city= "london"):
    # function that will make an API call to the weather API
    # return tuple of tempurature, place and weather description
    
    url='https://api.openweathermap.org/data/2.5'
    api_key = "8177764c8dfd0bad06a8a54c80589567"

    complete_url = f'{url}/weather?q={city}&appid={api_key}'
    
    data = requests.get(complete_url).json()
    print(data)
    # extract information like place,temperature , weather description
    x = data["main"]
    temp = round(x["temp"] - 273.15,2)
    place = data['name']
    x = data['weather']
    desc = x[0]['main']

    return (temp,place,desc)

if __name__:
    get_weather()

    