import telebot
from dotenv.main import load_dotenv
import os
from twt_dl import twitter_dl_video

load_dotenv()
API_KEY = os.environ.get('API_KEY')
bot = telebot.TeleBot(API_KEY)

# decorator


@bot.message_handler(commands=['start'])
def response(message):
    # print(message)
    bot.reply_to(message, "Hello, I'm a bot")


@bot.message_handler(commands=['mensagem'])
def response(message):
    # print(message)
    text = """
    oi bobão, eu sou um bot (eu sei seu endereço)
    """
    bot.reply_to(message, text)


def itboy(message):
    if message.text == "Quem é o it boy da quarta geração?":
        return True
    else:
        return False


@bot.message_handler(func=itboy)
def response(mensagem):
    print(mensagem)
    text = """O it boy da quarta geração é Choi Yeonjun, do grupo TXT"""
    bot.reply_to(mensagem, text)


def verifyTwitterLink(message):
    if message.text[0:19] == "https://twitter.com":
        return True
    else:
        return False


@bot.message_handler(func=verifyTwitterLink)
def response(mensagem):
    print(mensagem)
    path_arr = twitter_dl_video(mensagem.text)
    text = """
    legao esse link do twitter hein"""
    bot.reply_to(mensagem, text)
    bot.send_video(mensagem.chat.id, open(path_arr[0], 'rb'))
    bot.send_audio(mensagem.chat.id, open(path_arr[1], 'rb'))


# MENSAGEM PADRAO 
def verify(message):
    return True


@bot.message_handler(func=verify)
def response(mensagem):
    print(mensagem)

    text = """
    Escolha uma das opções abaixo:
/start - Iniciar
/mensagem - Ver uma mensagem fofa
Não tem outros comandos"""
    bot.reply_to(mensagem, text)
    


bot.polling()
 