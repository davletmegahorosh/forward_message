from config import bot, admins
from aiogram import types, Dispatcher
from database.sql_commands import Database
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


my_files = types.KeyboardButton('/my_words')
insert = types.KeyboardButton('/insert')
general_mark_up = types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=3).add(my_files, insert)

async def start(message: types.Message):
    await message.answer('бот работает', reply_markup=general_mark_up)

async def forward(message: types.Message):
    if message.chat.type != 'private':
        for i in message.text.split():
            if i in Database().sql_select_word():
                bot.forward_message(1154757842, message.chat.id, message.message_id)

async def my_words(message: types.Message):
    my_words = Database().sql_select_word()
    for word in my_words:
        but=types.InlineKeyboardButton('удалить', callback_data=f"del_{word['id']}")
        markup=types.InlineKeyboardMarkup().add(but)

        await message.answer(word['word'],reply_markup=markup)



class FSMadmin(StatesGroup):
    word = State()
async def insert_word(message: types.Message):
    if message.from_user.id in admins:
        if message.chat.type == 'private':
            await message.answer('напишите слово')
            await FSMadmin.word.set()


async def insert_word2(message: types.Message, state: FSMContext):
    Database().sql_insert_word(message.text)
    await state.finish()
    await message.answer('слово добалено в базу данных')
    for message_id in range(message.message_id-2, message.message_id+1):
        await bot.delete_message(message.chat.id, message_id)

def register_forward_message_handlers(dp:Dispatcher):
    dp.register_message_handler(insert_word, commands=['insert'])
    dp.register_message_handler(insert_word2, state=FSMadmin.word)
    dp.register_message_handler(my_words, commands=['my_words'])
    dp.register_message_handler(start, commands=['start'])

    dp.register_message_handler(forward)
