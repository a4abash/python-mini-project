#simple program that provides temperature of entered city
import requests
import json
import win32com.client as wincom
say = wincom.Dispatch("SAPI.SpVoice")

place = input("Enter the name of the city, town or country : ")
link = f"https://api.weatherapi.com/v1/current.json?key=21f7894ddc714712a74154942241203&q={place}"

r = requests.get(link)
# print(r.text)
weatherDictionary = json.loads(r.text)
#print(weatherDictionary["current"]["temp_c"])
w = weatherDictionary["current"]["temp_c"]
say.Speak(f"The present weather in {place}is{w} degree celsius")