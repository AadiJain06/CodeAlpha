# -*- coding: utf-8 -*-
"""CHATBOT

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ge1pqAGGBL3weKuot3PVl8f0YnCaCsS7
"""

import nltk
from nltk.chat.util import Chat, reflections

# Define the patterns for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am good, thank you!', 'I\'m doing well, thanks for asking.']),
    (r'what is your name?', ['I am a chatbot.', 'You can call me a chatbot.']),
    (r'quit', ['Bye, take care.', 'Goodbye!']),
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

# Start conversation
print("Bot: Hi there! How can I help you?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break
    bot_response = chatbot.respond(user_input)
    print("Bot:", bot_response)