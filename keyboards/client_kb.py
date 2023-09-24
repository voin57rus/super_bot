from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2= KeyboardButton('/Расположение')
b3 = KeyboardButton('/Цены')
b4 = KeyboardButton('/Реквизиты')
b5 = KeyboardButton('/Группа')
b6 = KeyboardButton('/Для_запуска')
b7 = KeyboardButton('/Добавить1')
b8 = KeyboardButton('/Добавить2')
b9 = KeyboardButton('/Меню')






#b4 = KeyboardButton('Поделиться ссылкой', request_contact=True)
#b5 = KeyboardButton('Место положения', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1,).add(b2, b3, b9).add(b4, b5).add(b6, b7, b8,)

#kb_client.add(b1).add(b2).insert(b3).add(b4).add(b5).insert(b6).add(b7).insert(b8)

#kb_client.row(b1, b2, b3, b4, b5, b6, b7, b8)insert