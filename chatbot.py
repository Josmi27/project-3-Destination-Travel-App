import os
import flask
import flask_socketio
import models, random
import app
import jokeapi

scenes = ['Imagine you are on a beautiful island, away from your problems', 'Imagine you are in your bed, sleeping your troubles away', 'Imagine you are in the library reading your favorite book']


rand_scene = random.randint(0, len(scenes)-1)

class Chatbot():
    def __init__(self):
        return 
    def response(self, message):
        bangs, command, args = message.split(' ', 2)
        
        if command == 'help':
            response = 'Want me to say more? I respond to: !! about, !! say <something>, !! quotes, !! joke, !! island, !! tips, !! meditation and !! imagine'
        elif command == 'tips':
            response = 'Want to know how to relax after a stressful day?: take a shower, prepare you favorite meal, do not think about any of your troubles!'
        elif command  == 'about':
            response = 'Welcome to the Relaxation Chatroom! Here you will be able to escape from the stresses of your life and relaaaaaaax :)' 
        elif command == 'say':
            response = args
        elif command == 'quotes':
            chatbot_quotes=[" Difficult roads often lead to beautiful destinations", "I promise you nothing is as chaotic as it seems", "Act the way that you want to feel.", "Tension is who you think you should be. Relaxation is who you are."]
            response = chatbot_quotes[random.randint(0,len(chatbot_quotes)-1)]
        elif command == 'imagine':
            response = scenes[rand_scene]
        elif command == 'meditation':
            response = "For more help relaxing, I would recommend downlaoding the Calm application on your phone."
        elif command == 'joke':
            response = jokeapi.rand_joke
        elif command == "island":
            response = "For extra relaxation, considering visiting an island in the Caribbean, like the Bahamas!"
        else:
            response = "I'm sorry, I don't understand what you're saying. Try '!!help for commands I understand.'"
        return response
