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
        await client.send_file(message.channel, './ezgif.com-video-to-gif.gif')
    if message.content.startswith('!calculate 2x3'):
        await client.send_message(message.channel, '2x3=1')
        time.sleep(3)
        await client.send_message(message.channel, '(modulo 5) obviously')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
