from pyrogram import types
import logging
from config import words, client
from datetime import datetime
from db import quries
import asyncio
async def send_message(text, time, username, client):
    if text is not None:
        for word in words:
            if word.lower() in text.lower():
                send_text = (f'{text}\n'
                        f'{time}\n'
                        f'<a href="https://t.me/{username}">Перейти в личку</a>\n')
                await client.send_message(-1001989879370, send_text)  # -1001819329546
                print('nigaday')

def check_db(send_text):
    for text in quries.get_text():
        if list(text)[1] == send_text:
            return False
    return True

@client.on_message()
async def forward_messages_to_channel(client, message: types.Message):
    quries.drop_db()
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace('-', '.')
    if message.chat.id != -1001989879370 and message.from_user.username\
        and check_db(message.text) :#-1001819329546
        if message.photo and message.caption:
            await send_message(message.caption,current_time_str, message.from_user.username, client)
            quries.save_text(message.text)
        else:
            await send_message(message.text,current_time_str, message.from_user.username, client)
            quries.save_text(message.text)



if __name__ == "__main__":
    quries.init_db()
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    client.run()


