import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

x = random.randint(1, 999999999999)
y = random.randint(1, 1000)
z = random.randint(1, 100)

@client.event
async def on_ready():
    print(f'Bot has started as {client.user}')

@client.event
async def on_message(message):
    global x, y, z
    if message.author == client.user:
        return

    if message.content.startswith('!start'):
        await message.channel.send('I generated three random numbers. One until 999bn, Second until 1000 and Third until 100')
    
    elif message.content.isdigit():
        if message.content == str(x):
            await message.channel.send(f'You guessed it! It was {x}')
            x = random.randint(1, 999999999999)  
            await message.channel.send('New number generated for x')

        elif message.content == str(y):
            await message.channel.send(f'You guessed it! It was {y}')
            y = random.randint(1, 1000) 
            await message.channel.send('New number generated for y')

        elif message.content == str(z):
            await message.channel.send(f'You guessed it! It was {z}')
            z = random.randint(1, 100) 
            await message.channel.send('New number generated for z')

        else:
            await message.channel.send('Wrong, Try Again!')
    else:
        pass

client.run('#your token here')
