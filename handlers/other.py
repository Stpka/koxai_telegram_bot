from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command

from config import admin_id, dp, bot

import sys
sys.path.append('..')
from db import dbFunc
from keyboards import kb_client


#		эхо функция
async def echo(message: Message):
	text = 'Я тебя люблю)'
	await message.reply(text=text, reply_markup=kb_client)
	if message.from_user.id != admin_id:
		await bot.send_message(chat_id=admin_id,text=f"Кто то строчит мне письма!\nID: {message.from_user.id}\n\
			Имя: {str(dbFunc.po_familii(int(message.from_user.id)))[2:-3]}\nТекст: {message.text}")



def register_handlers_other(dp : Dispatcher):
	dp.register_message_handler(echo)