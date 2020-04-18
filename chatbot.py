# import os
# import flask
# import flask_socketio
# import models, random
# import app
# import jokeapi

# scenes = ['Imagine you are on a beautiful island, away from your problems', 'Imagine you are in your bed, sleeping your troubles away', 'Imagine you are in the library reading your favorite book']


# rand_scene = random.randint(0, len(scenes)-1)

# class Chatbot():
#     def __init__(self):
#         return 
#     def response(self, message):
#         bangs, command, args = message.split(' ', 2)
        
#         if command == 'help':
#             response = 'Want me to say more? I respond to: !! about, !! say <something>, !! quotes, !! joke, !! island, !! tips, !! meditation and !! imagine'
#         elif command == 'tips':
#             response = 'Want to know how to relax after a stressful day?: take a shower, prepare you favorite meal, do not think about any of your troubles!'
#         elif command  == 'about':
#             response = 'Welcome to the Relaxation Chatroom! Here you will be able to escape from the stresses of your life and relaaaaaaax :)' 
#         elif command == 'say':
#             response = args
#         elif command == 'quotes':
#             chatbot_quotes=[" Difficult roads often lead to beautiful destinations", "I promise you nothing is as chaotic as it seems", "Act the way that you want to feel.", "Tension is who you think you should be. Relaxation is who you are."]
#             response = chatbot_quotes[random.randint(0,len(chatbot_quotes)-1)]
#         elif command == 'imagine':
#             response = scenes[rand_scene]
#         elif command == 'meditation':
#             response = "For more help relaxing, I would recommend downlaoding the Calm application on your phone."
#         elif command == 'joke':
#             response = jokeapi.rand_joke
#         elif command == "island":
#             response = "For extra relaxation, considering visiting an island in the Caribbean, like the Bahamas!"
#         else:
#             response = "I'm sorry, I don't understand what you're saying. Try '!!help for commands I understand.'"
#         return response


import os
import flask
import flask_socketio
import app
import jokeapi
import requests
from jokeapi import current_temperature
from jokeapi import current_timezone
from jokeapi import music_from_jamaica
from jokeapi import music_from_pr
from jokeapi import flight_api_cost
from jokeapi import currency_conversion
from jokeapi import outdoor_activity
from jokeapi import translate


class Chatbot():
    def __init__(self):
        return 

    def response(self, message):
        
        
        if message == '!! help':
            response = 'Please select one of the following: !! about, !! Jamaica, !! Puerto Rico, !! Exit, !! Current Weather, !! more help'
        elif message == '!! more help':
            response = 'Please select one of the following: !! say something, !! timezone, !! music , !! flights, !! currency, !! activities'
        elif message == '!! say something':
            response = "Hello, I'm a travel bot! For more help, try typing !! help"
        elif message == '!! music':
            response = "Please select one of the following: !! Jamaican-Music, !! PR-Music, !! translate"
        elif message == "!! about":
            response = "The purpose of this chatbot is inform you of random fun facts regarding specific travel locations!"
        elif message == '!! Jamaica':
             response = 'Travel Destination Selected: Jamaica. Fact: Dancehall music is the most popular in Jamaica'
        elif message == '!! Bali':
             response = 'Travel Destination Selected: Bali. Fact: the ice in Bali is quality controlled by the local government.'
        elif message == '!! Puerto Rico':
            response = "Travel Destination Selected: Puerto Rico. Fact: more than 70% of the rum sold in the United States comes from Puerto Rico."
        elif message == '!! Exit':
            response = 'Thank you! More locations and facts available soon!'
        elif message == '!! Current Weather':
            response = current_temperature()
        elif message == '!! timezone':
            response = current_timezone()
        elif message == '!! Jamaican-Music':
            response = music_from_jamaica()
        elif message == '!! PR-Music':
            response = music_from_pr()
        elif message == '!! flights':
            response = flight_api_cost()
        elif message == '!! currency':
            response = currency_conversion()
        elif message == '!! activities':
            response = outdoor_activity()
        elif message == '!! translate':
            response = translate()
        # elif message == '!! advice for country code: {}'.format(message[28:]):
        #     country_code =  "{}".format(message[28:])
        #     travel_warning_search = "https://www.reisewarnung.net/api?country={}".format(country_code)
        #     response = requests.get(travel_warning_search)
        #     json_body = response.json()
        #     danger_rating = json_body["data"]["situation"]["rating"]
        #     advice = json_body["data"]["lang"]["en"]["advice"]
        #     response = "Since the travel danger rating is {}/5, {}".format(danger_rating, advice)
        # elif message == "!! outdoor activities in Jamaica":
        #     url = "https://trailapi-trailapi.p.rapidapi.com/"
        #     querystring = {"q-country_cont":"{}".format(message[25:])}
        #     headers = {
        #         'x-rapidapi-host': "trailapi-trailapi.p.rapidapi.com",
        #         'x-rapidapi-key': "2bc8488dedmsh09812c800fb6b89p19fb19jsn6987dc57cdda"
        #         }
        #     response = requests.request("GET", url, headers=headers, params=querystring)
        #     json_body = response.json()
        #     activity = json_body["places"][0]["name"]
        #     activities_response = "You should check out the activity called: {}".format(activity)
        #     return(activities_response)
            # else:
            #     chatbot_message = "I'm not sure what you mean. Try '!! help'"
        return response