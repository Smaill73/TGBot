import requests
from telebot.types import Message

from config_data.config import RAPID_API_KEY, URL_LOW, ACCEPT
from loader import bot
from database.database import History


headers = {"accept": ACCEPT, "X-API-KEY": RAPID_API_KEY}


@bot.message_handler(commands=["low"])
def search_by_genre(message: Message):
    user_id = message.from_user.id
    command = "low"
    History.create(user_id=user_id, command=command)
    response = requests.get(URL_LOW, headers=headers)

    if response.status_code == 200:
        data = response.json()
        text_list = []
        for i in range(11):
            if i != 4:
                text_list.append(data["docs"][i]["name"])
        bot.reply_to(message, "\n".join(text_list))
    else:
        bot.reply_to(message, response.status_code)
