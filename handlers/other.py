# from aiogram import Bot, types, Dispatcher
# from create_bot import dp
# import json, string


# #@dp.message_handler()
# async def echo_send(message ):
# 	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
# 		.intersection(set(json.load(open('cenz.json')))) != set():
# 		await message.reply('Держи себя в руках засранец!!! - Маты запрещены! 👈')
# 		await message.delete()



# def register_handlers_other(dp : Dispatcher):
# 	dp.register_message_handler(echo_send)