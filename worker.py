# Work with Python 3.6
import discord
import random
import math

global calculated
calculated = 'not calculated'

TOKEN = 'NTAxMDcxMDU0NTk3MjU5Mjkx.DqUCkg.eEeYjShgTCLY0ZHsI5ojy3yeQgQ'

client = discord.Client()

def reverse(string):
    return(''.join([string[len(string) - 1 - i] for i in range(len(string))]))

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!shuffle'):
        msg = 'Shuffling'
        await client.send_file(message.channel, './ezgif.com-video-to-gif.gif')
    #if message.content.startswith('!calculate 2x3'):
    #    await client.send_message(message.channel, '2x3=1 (modulo 5) obviously')
    if message.content.startswith('!calculate'):
        modulus = str(random.randint(2, 10))
        #exec('calculated = ' +  ' '.join(message.content.replace('x', '*')[11:]).replace('x', '*'))
        exec('global calculated\ncalculated = str((' + reverse(reverse(message.content.lower().replace('x', '*').replace('sqrt', 'math.sqrt')[11:])) + ') % ' + modulus + ') + " (modulo ' + modulus + ')"')
        #await client.send_message(message.channel, 'calculated = ' +  ' '.join(message.content.replace('x', '*')[11:]).replace('x', '*'))
        await client.send_message(message.channel, message.content[11:] + ' = ' + str(calculated))
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
