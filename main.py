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
#   response = requests.get("http://127.0.0.1:3000/greetings")
#   greetings = json.loads(response.text)
    greetings  = 'This is demo greetings..'
    return (greetings)


@client.event
async def on_message(message):
    if message.author == client.user:
        #If the last message sent was from the bot itself, don't do anything
        return
    msg = message.content.lower()

    if any(word in msg for word in greetings):
        greeting_responses = get_greetings()
        await message.channel.send(greeting_responses)
        # await message.channel.send(random.choice(greeting_responses)['message'])


token = os.getenv('DISCORD_TOKEN')
client.run(token)