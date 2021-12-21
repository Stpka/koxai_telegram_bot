from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from config import dp 

import sys
sys.path.append('..')
from db import dbFunc
import botFunc


class FSMAdmin(StatesGroup):
	Q1 = State()
	Q2 = State()
	Q3 = State()


#@dp.message_handler(commands='da', state=None)
async def cm_start(message : types.Message):
	await FSMAdmin.Q1.set()
	if await botFunc.chmod(message.from_user.id):
		await message.answer('Зай, введи айдишник человека)')
	else: await state.finish()


#@dp.message_handler(state=FSMAdmin)
async def cm_sec(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['Q1']=message.text
	await FSMAdmin.next()
	await message.answer('Теперь введи новое имя)')


#@dp.message_handler(state=FSMAdmin)
async def cm_therd(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['Q2']=message.text

	await message.answer('Ок :3')
	dbFunc.up_title(data['Q1'], data['Q2'])

	await state.finish()


def register_handlers_admin(dp : Dispatcher):
	dp.register_message_handler(cm_start, commands=['upt'],state=None)
	dp.register_message_handler(cm_sec, state=FSMAdmin.Q1)
	dp.register_message_handler(cm_therd, state=FSMAdmin.Q2)