# Work with Python 3.6
import discord

TOKEN = 'NTAxMDcxMDU0NTk3MjU5Mjkx.DqUCkg.eEeYjShgTCLY0ZHsI5ojy3yeQgQ'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!shuffle'):
        msg = 'Shuffling'
        await client.send_file(message.channel, '/home/daniel/Downloads/ezgif.com-video-to-gif.gif', content='Shuffling')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
