from pyrogram import filters, types
import logging
from pyrogram.enums import ParseMode
from config import words, client


@client.on_message()
async def forward_messages_to_channel(client, message: types.Message):
    if message.chat.id != -4035690060:
        if message.photo and message.caption:
            text = (f'@{message.from_user.username}\n'
                    f'{message.caption}\n'
                    f'<a href="{message.link}">Перейти к сообщению</a>\n')
            await client.send_message(-4035690060,text)
        else:
            for word in words:
                if word.lower() in message.text.lower():
                    text = (f'@{message.from_user.username}\n'
                            f'{message.text}\n'
                            f'<a href="{message.link}">Перейти к сообщению</a>\n')
                    await client.send_message(-4035690060, text)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    client.run()
