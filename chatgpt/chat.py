import openai
import telebot
import json
import logging
import sys
import os
import time

logging.basicConfig(level=logging.INFO)

def check_config():
    if not os.path.exists('config'):
        logging.info("Creating config directory...")
        os.makedirs('config')
        logging.info(f"config directory created at {time.ctime()}")
    if not os.path.exists('config/config.json'):
        logging.info("Creating config.json file...")
        data = {
            "openai_api_key": "YOUR_OPENAI_API_KEY",
            "telegram_bot_token": "YOUR_TELEGRAM_BOT_TOKEN"
        }
        with open('config/config.json', 'w') as f:
            json.dump(data, f, indent=4, separators=(',', ': '))
        logging.info(f"config.config file created at {time.ctime()}")

# Call the function here
check_config()

with open('config/config.json') as f:
    config = json.load(f)

openai_api_key = config['openai_api_key']
telegram_bot_token = config['telegram_bot_token']

# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = openai_api_key

# Replace YOUR_BOT_TOKEN with the token for your Telegram bot
bot = telebot.TeleBot(telegram_bot_token)

@bot.message_handler(commands=['^(?!start|help|reboot).*'])
def handle_invalid_command(message):
    chat_id = message.chat.id
    logging.info(f"User {chat_id} sent invalid command")
    bot.send_message(chat_id, "Sorry, that is an invalid command. Please type '/help' for a list of available commands.")

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    logging.info(f"User {chat_id} started the bot")
    bot.send_message(chat_id, "Welcome to our Bot, we hope you have a great experience")
    bot.send_message(chat_id, "How can I help you today?")
    logging.info(f"User {chat_id} started the bot at {time.ctime()}")

def reboot_done():
    """This function sends a message to the user when the reboot is done"""
    try:
        with open("tmp/reboot_chat_id.txt", "r") as f:
            chat_id = f.read()
            reboot_done_msg = "Reboot Done"
            bot.send_message(chat_id, reboot_done_msg)
    except:
        pass

@bot.message_handler(commands=['reboot'])
def reboot(message):
    chat_id = message.chat.id
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    with open("tmp/reboot_chat_id.txt", "w") as f:
        f.write(str(chat_id))
    logging.info(f"User {chat_id} requested reboot")
    bot.send_message(chat_id, "Rebooting, please wait...")
    logging.info("Bot replied to user and starting reboot.")
    python = sys.executable
    os.execl(python, python, * sys.argv)

# calling the function after reboot
reboot_done()

@bot.message_handler(commands=['help'])
def help(message):
    chat_id = message.chat.id
    logging.info(f"User {chat_id} requested help")
    bot.send_message(chat_id, "I am a bot that can answer your questions using the OpenAI API. Try asking me something!")
    logging.info(f"User {chat_id} used help at {time.ctime()}")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    if message.text.startswith('/'):
        bot.send_message(chat_id, "This function does not handle commands. Please type '/help' for a list of available commands.")
    else:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{message.text}",
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response_text = response.choices[0].text
        if len(response_text) > 4096:
            response_text = response_text[:4096]
        bot.send_message(chat_id, response_text)
        logging.info(f"replied a message to User {chat_id} at {time.ctime()}")

if __name__ == '__main__':
    logging.info(f"Bot started successfully at {time.ctime()}")
    bot.polling()
