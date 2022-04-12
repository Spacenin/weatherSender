import json
from twilio.rest import Client
import weather

def sendMessage():
    #Get JSON details for various information to access Twilio
    with open("/home/pi/Code/pys/weatherSend/data/twilioapi.json") as jsonFile:
        SMSdata = json.load(jsonFile)

    #Setup connection
    client = Client(SMSdata["SID"], SMSdata["Auth"])

    #Send text message to every recipient
    for number in SMSdata["ToPhones"]:
        #Get dictionary of JSON data from Weather API
        dailyForecast = weather.getForecast(number[2])
        
        #Create message to send
        client.messages.create(
            body=composeMsg(number, dailyForecast),
            from_=SMSdata["FromPhone"],
            to=str(number[0])
        )
    
def composeMsg(number, dailyForecast):
    #Create message with all applicable stats
    message = \
        "Good morning " + str(number[1]) + "!\n" + \
        "Max temp: " + str(dailyForecast["maxtemp_f"]) + "\n" + \
        "Min temp: " + str(dailyForecast["mintemp_f"]) + "\n" + \
        "Avg temp: " + str(dailyForecast["avgtemp_f"]) + "\n" + \
        "Chance of rain: " + str(dailyForecast["daily_chance_of_rain"]) + "\n" + \
        "Total rainfall: " + str(dailyForecast["totalprecip_in"]) + "\n" + \
        "Max wind speed: " + str(dailyForecast["maxwind_mph"])
        
    return(message)

#Ensure it runs the send message function
if __name__ == "__main__":
    sendMessage()
