import botFunc

import sys
sys.path.append('..')
from db import eqipDbFunc
import botFunc
from db import containerDbFunc
from db import dbFunc

from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command

from config import admin_id, dp, bot



async def all_protocols(message: types.Message):
	'''Output DB for eqipment'''
	if await botFunc.chmod(message.from_user.id):	await botFunc.db_now(dbFunc.doclad())


async def all_eqipment(message: types.Message):
	'''Output DB'''
	if await botFunc.chmod(message.from_user.id):	
		await message.answer(eqipDbFunc.print_db())


async def registration_user(message: types.Message):
	'''Registration'''
	if dbFunc.oformlenie_protocola(message.from_user.id, '-'):
		await bot.send_message(chat_id=admin_id, text="Зай, у тебя +1 раб))")


async def all_kits(message: types.Message):
	await message.answer(containerDbFunc.kits())




def register_handlers(dp : Dispatcher):
	dp.register_message_handler(all_protocols, commands=['all', 'db'])
	dp.register_message_handler(all_eqipment, commands=['alleq'])
	dp.register_message_handler(registration_user, commands=['start'])
	dp.register_message_handler(all_kits, commands=['akit'])	




