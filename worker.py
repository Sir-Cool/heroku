# Work with Python 3.6
import discord
import random

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
        await client.send_message(message.channel, '2x3=1 (modulo 5) obviously')
    elif message.content.startswith('!calculate'):
        modulus = str(random.randint(2, 10))
        exec('calculate = str((' + ' '.join(message.content.replace('x', '*').split(' ')[1:]).replace('x', '*') + ') % ' + modulus + ') + " (modulo ' + modulus + ' obviously)"')
        await client.send_message(message.channel, calculated)
        #await client.send_message(message.channel, '')
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
