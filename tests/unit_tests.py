import unittest
import chatbot
import models
import jokeapi
import random


class ChatbotTests(unittest.TestCase):
    def test_help(self):
        response = chatbot.Chatbot.response(self, "!! help ")
        self.assertEqual(response, "Want me to say more? I respond to: !! about, !! say <something>, !! quotes, !! joke and !! imagine")
    def test_about(self):
        response = chatbot.Chatbot.response(self, "!! about ")
        self.assertEqual(response, 'Welcome to the Relaxation Chatroom! Here you will be able to escape from the stresses of your life and relaaaaaaax :)')
    def test_say_something(self):
        response = chatbot.Chatbot.response(self, "!! say hello")
        self.assertEqual(response, "hello")
    # def test_quotes(self):
    #     response = chatbot.Chatbot.response(self, "!! quotes ")
    #     scenes = ['Imagine you are on a beautiful island, away from your problems', 'Imagine you are in your bed, sleeping your troubles away', 'Imagine you are in the library reading your favorite book']
    #     self.assertEqual(response, scenes[random.randint(0, len(scenes))])
    def test_imagine(self):
        response = chatbot.Chatbot.response(self, "!! joke ")
        self.assertEqual(response, jokeapi.rand_joke)
    def test_no_response(self):
        response = chatbot.Chatbot.response(self, "   ")
        self.assertEqual(response, "I'm sorry, I don't understand what you're saying. Try '!!help for commands I understand.'")
        
        
if __name__ == '__main__':
    unittest.main()