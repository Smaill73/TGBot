from peewee import (
    CharField,
    Model,
    SqliteDatabase,
)

from config_data.config import DB_PATH

db = SqliteDatabase(DB_PATH)


class History(Model):
    user_id = CharField()
    command = CharField()

    class Meta:
        database = db
