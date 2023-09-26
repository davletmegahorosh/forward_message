from aiogram.utils import executor
from config import dp
import logging
from handlers import forward_from_chat, call_back
from database.sql_commands import Database

call_back.register_callback_query_handler(dp=dp)
forward_from_chat.register_forward_message_handlers(dp=dp)

async def on_start_up(_):
    db = Database()
    db.sql_create_db()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True, on_startup=on_start_up)
