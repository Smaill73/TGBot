from telebot.types import Message

from loader import bot
from database.database import History


@bot.message_handler(commands=["start"])
def handle_start(message: Message) -> None:
    user_id = message.from_user.id
    command = "start"
    History.create(user_id=user_id, command=command)
    bot.reply_to(message, f"Добро пожаловать {message.from_user.first_name}")
