from background import keep_alive
from aiogram import Bot, Dispatcher, executor, types
from create_bot import dp
from data_base import sqlite_db
import requests
import mate

async def on_startup(_):
	print('Бот - работает!')
	sqlite_db.sql_start()

from handlers import client, admin, other
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
# other.register_handlers_other(dp)


# мат блокировка
@dp.message_handler()
async def mess_handler(message: types.Message):
    text = message.text.lower()
    for world in mate.WORDS:
        if world in text:
            await message.reply('Держи себя в руках засранец!!! - Маты запрещены! 👈')
            await message.delete()

    if message.text.lower() == 'ку':
        await message.answer('И тебе привет бро!')        
    elif message.text.lower() == 'хай':
        await message.answer('И тебе привет!')
            
    elif message.text.lower() == '2':
        await message.answer('Пиши мне в лс - всё расскажу\nхак обновлён')
    # else:
    #      await message.answer('Не понял Вас!Опишите проблему!')

keep_alive()
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
