from telebot.types import Message

from loader import bot
from database.database import History


@bot.message_handler(commands=["history"])
def history(message: Message) -> None:
    user_id = message.from_user.id
    res = ""
    historys = History.select().where(History.user_id == user_id)
    cnt = 0
    for i in reversed(historys):
        if cnt < 10:
            res += f"{i.command}\n"
            cnt += 1
        else:
            break
    bot.reply_to(message, res)
