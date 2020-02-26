import os
import flask
import flask_socketio
import models, random
import app


class Chatbot():
    def __init__(self):
        return 
    def response(self, message):
        if message == '!! help':
            response = 'Want me to say more? I respond to: !! about, !! say<something>, !! quotes, and !! imagine'
        elif message == '!! about':
            response = 'Welcome to the Relaxattion Chatroom! Here you will be able to escape from the stresses of your life and relaaaaaaax :)' 
        elif message == '!! say <something>':
            response = message[7:]
        elif message == '!! quotes':
            chatbot_quotes=[" Difficult roads often lead to beautiful destinations", "I promise you nothing is as chaotic as it seems", "Act the way that you want to feel.", "Tension is who you think you should be. Relaxation is who you are."]
            response = chatbot_quotes[random.randint(0,len(chatbot_quotes))]
        elif message == '!! imagine':
            scenes = ['Imagine you are on a beautiful island, away from your problems', 'Imagine you are in your bed, sleeping your troubles away', 'Imagine you are in the library reading your favorite book']
            response = scenes[random.randint(0, len(scenes))]
        else:
            chatbot_message = "I'm sorry, I don't understand what you're saying. Try '!!help for commands I understand.'"
        return response
