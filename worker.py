# Work with Python 3.6
import discord
import random
import math
import traceback
import re
import time

def remove_zeroes(exp):
    """expression = exp.lstrip('0')
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    changed = True
    while changed:
        changed = False
        for i in range(len(expression)):
            if not(changed):
                if expression[i] == '0':
                    if not(expression [i - 1] in numbers) and (expression[i + 1] in numbers):
                        expression = expression[0:i] + expression[i+1:]
                    else:
                        expression = expression[0:i] + '!"zero"!' + expression[i+1:]
                    changed = True
    return(expression.replace('!"zero"!', '0'))"""
    return(re.sub(r'^0+(?=[0-9])|(?<=[^0-9])(0+)(?=[0-9])', '', exp))

global calculated
calculated = 'not calculated'

TOKEN = 'NTAxMDcxMDU0NTk3MjU5Mjkx.DqUCkg.eEeYjShgTCLY0ZHsI5ojy3yeQgQ'

client = discord.Client()

def reverse(string):
    return(''.join([string[len(string) - 1 - i] for i in range(len(string))]))

@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return
    await client.change_presence(status=discord.Status.dnd, game=discord.Game(name='Working on: '+msg))
    #await client.change_presence(game=discord.Game(name='type !help', type='Testing'))
    # we do not want the bot to reply to itself
    
    if msg.startswith('!shuffle'):
        #msg = 'Shuffling'
        await client.send_file(message.channel, './ezgif.com-video-to-gif.gif')
        last_command = 'Shuffle'
    msg = message.content
    #if msg.startswith('!calculate 2x3'):
    #    await client.send_message(message.channel, '2x3=1 (modulo 5) obviously')
    msg = message.content
    if 'mao' in msg.lower():
        await client.send_message(message.channel, 'Taking Mao\'s name in vain, +5 cards.')
        last_command = 'Penalising taking Mao\'s name in vain.'
    msg = message.content
    if '?' in msg.lower():
        await client.send_message(message.channel, 'Asking questions, +1 card.')
        last_command = 'Penalising asking questions.'
    msg = message.content
    if 'martin' in msg.lower() and not('respect' in msg.lower()):
        await client.send_message(message.channel, 'Failure to pay respect to Martin, +1 card.')
        last_command = 'Penalising failure to respect Martin.'
    msg = message.content
    if msg.startswith('!help'):
        if msg == '!help':
            await client.send_message(message.channel, """I am Martin, I like to shuffle (!shuffle)
I also like modular arithmetic! (!calculate [ mod <modulus>]) <- square brackets indicate optional parameter
    Enter expressions using the following symbols: + - x / ^ and the following functions: sqrt() fact()""")
            last_command = '!help'
    msg = message.content
    if msg.startswith('!calculate'):
        global calculated
        modulus = None
        params = msg.replace('modulo', 'mod').split(' mod ')
        if len(params) == 2:
            modulus = params[1].lstrip('0')
        msg = message.content
        #else:
        #    modulus = str(random.randint(2, 10))
        #exec('calculated = ' +  ' '.join(msg.replace('x', '*')[11:]).replace('x', '*'))
        try:
            if modulus == None:
                exec('global calculated\ncalculated = "' + msg[11:] + ' = " + str((' + remove_zeroes(params[0].lower().replace('x', '*').replace('sqrt', 'math.sqrt').replace('fact', 'math.factorial').replace('^', '**')[11:]) + '))')
            else:
                exec('global calculated\ncalculated = "' + msg[11:] + ' = " + str((' + remove_zeroes(msg.lower().replace('mod', '%').replace('x', '*').replace('sqrt', 'math.sqrt').replace('fact', 'math.factorial').replace('^', '**')[11:]) + ')) + " (modulo ' + modulus + ')"')
        except Exception:
            calculated = '```' + traceback.format_exc() + '```'
        #await client.send_message(message.channel, 'calculated = ' +  ' '.join(msg.replace('x', '*')[11:]).replace('x', '*'))
        msg = message.content
        if len(calculated) < 1800:
            await client.send_message(message.channel, str(calculated))
        else:
            with open('answer.txt', 'w') as file:
                file.write(calculated)
            await client.send_file(message.channel, './answer.txt', filename='answer to '+msg[11:], content=msg[11:])
        msg = message.content
        last_command = 'Calculating ' + msg[11:]
    time.sleep(1)
    await client.change_presence(status=discord.Status.online, game=discord.Game(name='type !help - Last completed command: '+last_command))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
