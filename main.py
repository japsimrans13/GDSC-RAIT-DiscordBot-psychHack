import discord
import os
import requests
import json
import random
# from nanoid import generate
from dotenv import load_dotenv

load_dotenv()

#Create a connection with Discord
client = discord.Client()

greetings = [ "hello", "hi", 'hie', "hey","good morning", "good evening",]

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#Gets response from the api that you choose
def get_greetings():
    response = requests.get("https://gdsc-rait-discord-bot-api-psych-hack.vercel.app/greetings")
    print(response.text)
    message ="Hello Sir"
    if response.status_code == 200:
        # Checking if our api is working properly
        res_json  = json.loads(response.text)
        message = res_json['message']
    return (message)


@client.event
async def on_message(message):
    if message.author == client.user:
        #If the last message sent was from the bot itself, don't do anything
        return
    msg = message.content.lower()

    if any(word in msg for word in greetings):
        greeting_responses = get_greetings()
        await message.channel.send(greeting_responses)


token = os.getenv('DISCORD_TOKEN')
client.run(token)