import discord
import random

TOKEN = 'MTA3NjUxMTQ4NDkzMjI2ODA2Mg.GTBVTq.ppnelhEyZ77pRQiCPMEgrB3VYAKjG35RWLtSVg'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'naya-channel':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}')
            return
        elif user_message.lower() == '!random':
            response = f' This is your random number {random.randrange(100000)}'
            await message.channel.send(response)
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere')
        return



client.run(TOKEN)