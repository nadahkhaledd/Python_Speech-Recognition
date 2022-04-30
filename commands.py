import subprocess
import os
from txtToSpeech import say
from get_answer import Fetcher

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" and "name" in text:
            if "my" in text:
                self.respond("You haven\'t told me your name yet")
            else:
                self.respond("My name is python commander. How are you?")

    def respond(self, response):
        say(response)
