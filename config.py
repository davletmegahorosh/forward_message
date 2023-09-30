admins = [661114436, 1154757842]
words = ['Ищем заказщиков',
'Ищю производство',
'Ищу производство',
'Нужно отшить',
'Ищу швейный цех',
'Ищу цех',
'Ищу поставщика',
'Ищу байера',
'Ищу швейное производство',
'Ищу фулфилмент в Бишкеке']

from decouple import config
from pyrogram import Client
API_ID = config('api_id')
API_HASH=config('api_hash')
client = Client("my_bot", api_id=API_ID, api_hash=API_HASH)
