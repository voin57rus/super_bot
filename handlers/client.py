from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
parse_mode=types.ParseMode.HTML

# @dp.message_handler(commands=['start', 'help'])
# курсив <i> </i>
# жирный <b> </b> после reply_markup=kb_client, parse_mode=types.ParseMode.HTML
async def command_start(message : types.Message):
    try:
        await message.answer(f"<i>Здраствуйте!</i> <b>{message.from_user.full_name}</b> <i>рады Вас видеть у нас в группе!</i>", parse_mode=types.ParseMode.HTML, reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/gggwejgy')

    	

		
#@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00', reply_markup=kb_client)

	#@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Телеграм группа https://t.me/+cOyHU6tXxQg2ODIy', reply_markup=ReplyKeyboardRemove())

#@dp.message_handler(commands=['Цены'])
async def pizza_price_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Цены:\n1)день = 70р\n3)дня = 120р\n7)дней = 220р\n30)дней = 360р\n60)дней = 550р', reply_markup=kb_client)
	await bot.send_message(message.from_user.id, ' 💸', reply_markup=kb_client)


#@dp.message_handler(commands=['Реквезиты'])
async def pizza_requisites_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'сбер - 2202 2021 9681 2352  \nкиви +79536157290  \nЮ.Money — https://money.yandex.ru/to/4100111524920305', reply_markup=kb_client)		


#@dp.message_handler(commands=['Группа'])
async def pizza_group_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'https://vk.com/alteza_hack',reply_markup=kb_client)#, reply_markup=ReplyKeyboardRemove())

#@dp.message_handler(commands=['Для_запуска'])
async def pizza_launch_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'визуалки', reply_markup=kb_client)


#@dp.message_handler(commands=['Добавить1'])
async def pizza_add_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'цены', reply_markup=kb_client)


#@dp.message_handler(commands=['Добавить_2'])
async def pizza_add_2_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'видос', reply_markup=kb_client)

@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
	await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])

	dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
	dp.register_message_handler(pizza_place_command, commands=['Расположение']) 
	dp.register_message_handler(pizza_price_command, commands=['Цены'])
	dp.register_message_handler(pizza_requisites_command, commands=['Реквизиты'])
	dp.register_message_handler(pizza_group_command, commands=['Группа']) 
	dp.register_message_handler(pizza_launch_command, commands=['Для_запуска'])
	dp.register_message_handler(pizza_add_command, commands=['Добавить1'])
	dp.register_message_handler(pizza_add_2_command, commands=['Добавить2'])
	dp.register_edited_message_handler(pizza_menu_command, commands=['Меню'])
