import requests
import json

def getForecast():
    #Get API key from weatherAPI JSON file
    with open("../data/weatherapi.json") as jsonFile:
        apiKey = json.load(jsonFile)

    #Get JSON of forecast data
    forecastData = requests.get("http://api.weatherapi.com/v1/forecast.json?key="+apiKey["key"]+"&q=29631&days=1").json()

    #Parse out the day data and return it to sms
    dailyForecast = forecastData["forecast"]["forecastday"][0]["day"]
    return(dailyForecast)