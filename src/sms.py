import json
from twilio.rest import Client
import weather

def sendMessage():
    #Get JSON details for various information to access Twilio
    with open("../data/twilioapi.json") as jsonFile:
        SMSdata = json.load(jsonFile)

    #Get dictionary of JSON data from Weather API
    dailyForecast = weather.getForecast()

    #Setup connection
    client = Client(SMSdata["SID"], SMSdata["Auth"])

    #Send text message to every recipient
    for number in SMSdata["ToPhones"]:
        client.messages.create(
            body="Max temp: " + str(dailyForecast["maxtemp_f"]) + "\n" +
                "Min temp: " + str(dailyForecast["mintemp_f"]) + "\n" +
                "Avg temp: " + str(dailyForecast["avgtemp_f"]),
            from_=SMSdata["FromPhone"],
            to=str(number)
        )
        
    
