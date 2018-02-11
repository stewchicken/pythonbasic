from chatterbot.trainers import ListTrainer # method to train the chatbot
from chatterbot import ChatBot # import the chatbot

import os

bot = ChatBot('TestBot') # create the chatbot
bot.set_trainer(ListTrainer)# set the trainer

for file in os.listdir('files'):
    chat = open('files/'+file, 'r').readlines()
    print (file)
    bot.train(chat)

while True:
    request = input("You: ")
    response = bot.get_response(request)
    print(response)

