import telebot
import time

TOKEN="5142313823:AAEc5eWjzbNR4nbKF9w6chCVqVJVDZSiz7I"
bot = telebot.TeleBot(TOKEN)

def getargs(text):
    _args = text.split()[1:]
    return _args

@bot.message.handler(command=['start'])
def sayhello(message):
    bot.send_message(message.chat_id, 'Hello,Im travamaker ofc bot')

@bot.message.handler(command=['help'])
def sayhelp(message):
    bot.send_message(message.chat_id, 'fuck you')

@bot.message.handler(command=["s", "say"])
def texttospeak(message):
    args = getargs(message.tetx)
    text = " ".join(args[0:])
    try:
        bot.send_message(message.chat.id, text)
    except Exception as e:
        bot.send_message(message.chat.id, f"Suprice mf")

while True:
    try:
        bot.pollong()
    except:
        time.sleep(5)        