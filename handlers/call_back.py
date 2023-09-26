from config import bot
from aiogram import types, Dispatcher
from database.sql_commands import Database

async def delete_word(call: types.CallbackQuery):
    id = int(call.data.replace('del_',''))
    Database().sql_delete_word(id)
    await bot.send_message(call.message.chat.id, 'удалено')

async def empty(call: types.CallbackQuery):
    if call.data and call.data.startswith("del_"):
        await delete_word(call)
    else:
        await call.answer(call.data)
    await bot.delete_message(call.message.chat.id, call.message.message_id)

def register_callback_query_handler(dp: Dispatcher):
    dp.register_callback_query_handler(empty)
