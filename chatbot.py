import os
import flask
import flask_socketio
import app
import destination_api
import requests
from destination_api import current_temperature
from destination_api import current_timezone
from destination_api import music_from_jamaica
from destination_api import music_from_pr
from destination_api import airport
from destination_api import currency_conversion
from destination_api import outdoor_activity
from destination_api import translate
from destination_api import travel_advice
from destination_api import twilio_texts

class Chatbot():
    def __init__(self):
        return 

    def response(self, message):
        
        if message == '!! help':
            response = 'Please select one of the following: !! about, !! Jamaica, !! Puerto Rico, !! Exit, !! Current Weather, !! more help'
        elif message == '!! more help':
            response = 'Please select one of the following: !! <country code>-Travel, !! PR-Music, !! Activity-<country name>, !! Jamaica-airports, !! translate'
        elif message == '!! say something':
            response = "Hello, I'm a travel bot! For more help, try typing !! help"
        elif message == '!! music':
            response = "Please select one of the following: !! Jamaican-Music, !! PR-Music, !! Jamaica-currency, !! PR-airport"
        elif message == '!! new commands':
            response = "Please select one: !! PR-airport, !! Activity-<country name>, !! PR-currency, !! translate, !! text, !! <country code>-Travel"
        elif message == "!! about":
            response = "The purpose of this chatbot is inform you of random fun facts regarding specific travel locations!"
        elif message == '!! Jamaica':
             response = 'Travel Destination Selected: Jamaica. Fact: Dancehall music is the most popular in Jamaica'
        elif message == '!! Puerto Rico':
            response = "Travel Destination Selected: Puerto Rico. Fact: more than 70% of the rum sold in the United States comes from Puerto Rico."
        elif message == '!! Exit':
            response = 'Thank you! More locations and facts available soon!'
        elif message == '!! text':
            response = twilio_texts()
        elif message == '!! Current Weather':
            response = current_temperature()
        elif message == '!! timezone':
            response = current_timezone()
        elif message == '!! Jamaican-Music':
            response = music_from_jamaica()
        elif message == '!! PR-Music':
            response = music_from_pr()
        elif message == '!! Airport-{}'.format(message[11:]):
            city = '{}'.format(message[11:])
            response = airport(city)
        elif message == '!! Jamaica-currency':
            response = currency_conversion()
        elif message == '!! PR-currency':
            response = "Puerto Rico uses the US Dollar as its currency."
        elif message == '!! Activity-{}'.format(message[12:]):
            response = "something"
            country_name = '{}'.format(message[12:])
            response = outdoor_activity(country_name)
        elif message == '!! translate':
            response = translate()
        elif message == '!! {}-Travel'.format(str(message[3:5])):
            response = "something"
            user_input = '{}'.format(message[3:5]).upper()
            response = travel_advice(user_input)
        

        return(response)