from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_default_commands

from database.database import History

if __name__ == "__main__":
    History.create_table()
    set_default_commands(bot)
    bot.infinity_polling()
