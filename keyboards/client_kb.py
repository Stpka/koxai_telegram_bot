from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/db')
b2 = KeyboardButton('/alleq')
b3 = KeyboardButton('/eq')
b4 = KeyboardButton('/upt')
b5 = KeyboardButton('/nkit')
b6 = KeyboardButton('/mkit')
b7 = KeyboardButton('/akit')


kb_client = ReplyKeyboardMarkup()

kb_client.add(b4).row(b1,b2).row(b3,b5,b6,b7) # Добавить кнопки с новой строки