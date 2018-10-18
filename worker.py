# Work with Python 3.6
import discord
import random
import math
import traceback
import re
import time
global last_command
global cards

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

def open_cards():
    global cards
    with open('cards.txt') as file:
        code = 'global cards\ncards = {"' + file.read().replace('\n', '"],"').replace(': ', '": [').replace('-', ',"')[:-2] + '}'
        exec(code)

def save_cards():
    global cards
    save_data = ''
    for i in cards:
        save_data += i + ': ' + str('-'.join([str(j) for j in cards[i]])) + '\n'
    with open('cards.txt', 'w') as file:
        file.write(save_data)

def give_cards(user, number, nick):
    global cards
    open_cards()
    try:
        cards[user][0] += number
        cards[user][1] = nick
    except:
        cards[user] = [number, nick]
        #cards[user][0] = number
        #cards[user][1] = nick
    save_cards()

global calculated
calculated = 'not calculated'

TOKEN = 'NTAxMDcxMDU0NTk3MjU5Mjkx.DqUCkg.eEeYjShgTCLY0ZHsI5ojy3yeQgQ'

client = discord.Client()

def reverse(string):
    return(''.join([string[len(string) - 1 - i] for i in range(len(string))]))

async def handle_message(message):
    global cards
    global last_command
    if message.author == client.user:
        return
    msg = message.content
    nick = message.author.nick
    if nick == None:
        message.author.nick = message.author.name
        nick = message.author.nick
    give_cards(message.author.name, 0, nick)
    await client.change_presence(status=discord.Status.dnd, game=discord.Game(name='Scanning / working on : '+msg))
    #await client.change_presence(game=discord.Game(name='type !help', type='Testing'))
    # we do not want the bot to reply to itself
    
    nick = message.author.nick
    if msg.startswith('!shuffle'):
        #msg = 'Shuffling'
        await client.send_file(message.channel, './ezgif.com-video-to-gif.gif')
        last_command = 'Shuffle'
    msg = message.content
    #if msg.startswith('!calculate 2x3'):
    #    await client.send_message(message.channel, '2x3=1 (modulo 5) obviously')
    msg = message.content
    nick = message.author.nick
    if msg.startswith('!cards'):
        """try:
            card_number = cards[msg[7:]]
            await client.send_message(message.channel, 'Player ' + msg[7:] + ' has ' + str(card_number) + ' cards.')
        except:
            await client.send_message(message.channel, 'Player ' + msg[7:] + ' not found.')
        """
        open_cards()
        if msg == '!cards':
            msg = '!cards ' + nick
        player_found = False
        for i in cards:
            if cards[i][1] == msg[7:]:
                await client.send_message(message.channel, '' + msg[7:] + ' has ' + str(cards[i][0]) + ' cards.')
                player_found = True
        if player_found == False:
            if msg == '!cards download':
                await client.send_file(message.channel, './cards.txt')
            else:
                await client.send_message(message.channel, '' + msg[7:] + ' not found.')
        last_command = 'Counting ' + msg[7:] + '\'s cards.'
    msg = message.content
    nick = message.author.nick
    if '7' in msg:
        occurences = len(msg.split('7')) - 1
        give_cards(message.author.name, 2 * occurences, nick)
        last_command = 'Wishing ' + nick + ' a nice day.'
        await client.send_message(message.channel, message.author.mention + ' Have a ' + ''.join(['very ' for i in range(occurences)]) + 'nice day. (+' + str(2 * occurences) + ' cards). You now have ' + str(cards[message.author.name][0]) + ' cards.')
    msg = message.content
    nick = message.author.nick
    if 'rule' in msg.lower():
        give_cards(message.author.name, 1, nick)
        last_command = 'Penalising ' + nick + ' for talking about the rules.'
        await client.send_message(message.channel, message.author.mention + ' Talking about the rules, +1 card. You now have ' + str(cards[message.author.name][0]) + ' cards.')
    msg = message.content
    nick = message.author.nick
    if 'mao' in msg.lower():
        give_cards(message.author.name, 5, nick)
        last_command = 'Penalising ' + nick + ' for taking Mao\'s name in vain.'
        await client.send_message(message.channel, message.author.mention + ' Taking Mao\'s name in vain, +5 cards. You now have ' + str(cards[message.author.name][0]) + ' cards.')
    msg = message.content
    nick = message.author.nick
    if '?' in msg.lower():
        occurences = len((' ' + msg + ' ').split('?')) - 1
        give_cards(message.author.name, 1 * occurences, nick)
        last_command = 'Penalising ' + nick + ' for asking questions.'
        await client.send_message(message.channel, message.author.mention + ' Asking questions, +' + str(1 * occurences) + ' cards. You now have ' + str(cards[message.author.name][0]) + ' cards.')
    msg = message.content
    nick = message.author.nick
    if 'martin' in msg.lower() and not('respect' in msg.lower()):
        give_cards(message.author.name, 1, nick)
        last_command = 'Penalising ' + nick + ' for failing to respect Martin.'
        await client.send_message(message.channel, message.author.mention + ' Failure to pay respect to Martin, +1 card. You now have ' + str(cards[message.author.name][0]) + ' cards.')
    msg = message.content
    nick = message.author.nick
    badger_rule_broken = False
    for i in [j.strip(' ') for j in msg.split('.')]:
        #print(i)
        try:
            if i[0] in [j for j in 'aBCDeFGHiJKLMNoPQRSTuVWXYZ']:
                badger_rule_broken = True
        except:
            pass
    if badger_rule_broken:
        give_cards(message.author.name, 1, nick)
        last_command = 'Penalising ' + nick + ' for failing to respect the badger.'
        await client.send_message(message.channel, message.author.mention + ' Failure to respect the badger, +1 card. You now have ' + str(cards[message.author.name][0]) + ' cards.')
    msg = message.content
    nick = message.author.nick
    if msg.startswith('!help'):
        if msg == '!help':
            await client.send_message(message.channel, """I am Martin, I like to shuffle (!shuffle)
I also like modular arithmetic! (!calculate [ mod <modulus>]) <- square brackets indicate optional parameter
    Enter expressions using the following symbols: + - x / ^ and the following functions: sqrt() fact()\nI also enforce the rules of a slightly modified game of Mao on this server. To view a player's card balance type: !cards <player_nickname>""")
            last_command = '!help'
    msg = message.content
    nick = message.author.nick
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
async def on_message_edit(before, after):
    await handle_message(after)

@client.event
async def on_message(message):
    await handle_message(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
