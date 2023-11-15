from pyrogram import types
import logging
from config import words, client
from datetime import datetime
from db import quries
import asyncio

async def send_message(text, timee, username, client):
    for word in words:
        if word.lower() in text.lower():
            send_text = (f'{text}\n'
                    f'{timee}\n'
                    f'<a href="https://t.me/{username}">Перейти в личку</a>\n')
            await client.send_message(-1001819329546, send_text)
            quries.drop_db()
            quries.save_text(text)
            break

async def send_photo(photo_file_id, caption, time_str, username, client):
    for word in words:
        if word.lower() in caption.lower():
            photo = types.InputMediaPhoto(media=photo_file_id, caption=(f'{caption}\n{time_str}\n<a href="https://t.me/{username}">Перейти в личку</a>\n'))
            await client.send_media_group(chat_id=-1001819329546, media=[photo])
            quries.drop_db()
            quries.save_text(caption)
            break


def check_db(send_text):
    if quries.get_text() == []:
        return True
    for text in quries.get_text():
        if send_text != list(text)[1]:
            return True
    return False

@client.on_message()
async def forward_messages_to_channel(client, message: types.Message):
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace('-', '.')
    if message.from_user and message.chat.id != -1001819329546 and message.from_user.username and check_db(message.text if message.text else message.caption) :
        if message.photo and message.caption:
            await send_photo(message.photo.file_id, message.caption, current_time_str, message.from_user.username, client)
        elif message.text:
            await send_message(message.text,current_time_str, message.from_user.username, client)


if __name__ == "__main__":
    quries.init_db()
    quries.create_tables()
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    client.run()