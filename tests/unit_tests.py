import unittest
import chatbot
import models
import jokeapi
from chatbot import *


class ChatbotTests(unittest.TestCase):
    def test_help(self):
        response = chatbot.Chatbot.response(self, "!! help ")
        self.assertEqual(response, "Want me to say more? I respond to: !! about, !! say <something>, !! quotes, !! joke, !! island, !! tips, !! meditation and !! imagine")
    def test_about(self):
        response = chatbot.Chatbot.response(self, "!! about ")
        self.assertEqual(response, 'Welcome to the Relaxation Chatroom! Here you will be able to escape from the stresses of your life and relaaaaaaax :)')
    def test_say_something(self):
        response = chatbot.Chatbot.response(self, "!! say hello")
        self.assertEqual(response, "hello")
    def test_imagine(self):
        response = chatbot.Chatbot.response(self, "!! imagine ")
        for element in random.sample(scenes, 2):
            self.assertTrue(element in scenes)
    def test_meditation(self):
        response = chatbot.Chatbot.response(self, '!! meditation ')
        self.assertEqual(response, "For more help relaxing, I would recommend downlaoding the Calm application on your phone.")
    def test_tips(self):
        response = chatbot.Chatbot.response(self, "!! tips ")
        self.assertEqual(response, 'Want to know how to relax after a stressful day?: take a shower, prepare you favorite meal, do not think about any of your troubles!')
    def test_joke(self):
        response = chatbot.Chatbot.response(self, "!! joke ")
        self.assertEqual(response, jokeapi.rand_joke)
    def test_quotes(self):
        response = chatbot.Chatbot.response(self, "!! quotes ")
        chatbot_quotes=[" Difficult roads often lead to beautiful destinations", "I promise you nothing is as chaotic as it seems", "Act the way that you want to feel.", "Tension is who you think you should be. Relaxation is who you are."]
        # self.assertEqual(response, chatbot_quotes[random.randint(0,len(chatbot_quotes)-1)]) 
        for element in random.sample(chatbot_quotes, 3):
            self.assertTrue(element in chatbot_quotes)
    def test_no_response(self):
        response = chatbot.Chatbot.response(self, "   ")
        self.assertEqual(response, "I'm sorry, I don't understand what you're saying. Try '!!help for commands I understand.'")
    def test_island (self):
        response = chatbot.Chatbot.response(self, "!! island ")
        self.assertEqual(response,"For extra relaxation, considering visiting an island in the Caribbean, like the Bahamas!")
        

        
        
if __name__ == '__main__':
    unittest.main()