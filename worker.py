# Work with Python 3.6
import discord
import random
import math

def remove_zeroes(exp):
    expression = exp.lstrip('0')
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
    return(expression.replace('!"zero"!', '0'))

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
    if message.content.startswith('!help'):
        if message.content == '!help':
            await client.send_message(message.channel, """I am Martin, I like to shuffle (!shuffle)
I also like modular arithmetic! (!calculate [ mod <modulus>])
    Enter expressions using the following symbols: + - x / ^ and the following functions: sqrt() fact()""")
    if message.content.startswith('!calculate'):
        params = message.content.replace('modulo', 'mod').split(' mod ')
        if len(params) == 2:
            modulus = params[1].lstrip('0')
        else:
            modulus = str(random.randint(2, 10))
        #exec('calculated = ' +  ' '.join(message.content.replace('x', '*')[11:]).replace('x', '*'))
        exec('global calculated\ncalculated = str((' + remove_zeroes(params[0].lower().replace('x', '*').replace('sqrt', 'math.sqrt').replace('^', '**').replace('fact', 'math.factorial')[11:]) + ') % ' + modulus + ') + " (modulo ' + modulus + ')"')
        #await client.send_message(message.channel, 'calculated = ' +  ' '.join(message.content.replace('x', '*')[11:]).replace('x', '*'))
        await client.send_message(message.channel, message.content[11:] + ' = ' + str(calculated))
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
