import requests
from telebot.types import Message
from telebot import types

from config_data.config import (
    RAPID_API_KEY,
    URL_CUSTOM_RU,
    URL_CUSTOM_UK,
    URL_CUSTOM_USA,
    URL_CUSTOM_FR,
    ACCEPT,
)
from loader import bot
from database.database import History


headers = {"accept": ACCEPT, "X-API-KEY": RAPID_API_KEY}


@bot.message_handler(commands=["custom"])
def search_by_genre(message: Message):
    user_id = message.from_user.id
    command = "custom"
    History.create(user_id=user_id, command=command)
    keyboard = types.InlineKeyboardMarkup()
    key_ru = types.InlineKeyboardButton(text="Россия", callback_data="RU")
    keyboard.add(key_ru)
    key_usa = types.InlineKeyboardButton(text="США", callback_data="USA")
    keyboard.add(key_usa)
    key_uk = types.InlineKeyboardButton(text="Великобритания", callback_data="UK")
    keyboard.add(key_uk)
    key_fr = types.InlineKeyboardButton(text="Франция", callback_data="FR")
    keyboard.add(key_fr)
    bot.send_message(
        message.from_user.id, text="Выберите страну", reply_markup=keyboard
    )

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "RU":
            response = requests.get(URL_CUSTOM_RU, headers=headers)

            if response.status_code == 200:
                data = response.json()
                text_list = []
                for i in range(10):
                    text_list.append(data["docs"][i]["name"])
                bot.reply_to(message, "\n".join(text_list))
            else:
                bot.reply_to(message, response.status_code)

        if call.data == "USA":
            response = requests.get(URL_CUSTOM_USA, headers=headers)

            if response.status_code == 200:
                data = response.json()
                text_list = []
                for i in range(10):
                    text_list.append(data["docs"][i]["name"])
                bot.reply_to(message, "\n".join(text_list))
            else:
                bot.reply_to(message, response.status_code)

        if call.data == "UK":
            response = requests.get(URL_CUSTOM_UK, headers=headers)

            if response.status_code == 200:
                data = response.json()
                text_list = []
                for i in range(10):
                    text_list.append(data["docs"][i]["name"])
                bot.reply_to(message, "\n".join(text_list))
            else:
                bot.reply_to(message, response.status_code)

        if call.data == "FR":
            response = requests.get(URL_CUSTOM_FR, headers=headers)

            if response.status_code == 200:
                data = response.json()
                text_list = []
                for i in range(10):
                    text_list.append(data["docs"][i]["name"])
                bot.reply_to(message, "\n".join(text_list))
            else:
                bot.reply_to(message, response.status_code)
