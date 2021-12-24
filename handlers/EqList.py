from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from config import dp, bot, admin_id

import db.eqipDbFunc as eqipDbFunc
import db.dbFunc as dbFunc



class FSMAdmin(StatesGroup):
	eq_name = State()
	eq_id = State()
	eq_cords = State()


#		Добовление нового оборудования
async def frst(message : types.Message):
	await FSMAdmin.eq_name.set()
	await message.answer('Введите название оборудования')


async def secnd(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['eq_name']=message.text
	await FSMAdmin.next()
	await message.answer('Введите id оборудования')


async def therd(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['eq_id']=message.text
	await FSMAdmin.next()
	await message.answer('Введите местоположение оборудования')


async def final(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['eq_cords']=message.text
	
	if eqipDbFunc.new_line(data['eq_id'], data['eq_name'], data['eq_cords']):
		await message.answer('Учтём!')
		if message.from_user.id != admin_id:
			await bot.send_message(chat_id=admin_id, text=f"Котик, {dbFunc.po_familii(message.from_user.id)} добавил новое оборудование!")

	await state.finish()


def register_handlers_equipment(dp : Dispatcher):
	dp.register_message_handler(frst, commands=['eq'],state=None)
	dp.register_message_handler(secnd, state=FSMAdmin.eq_name)
	dp.register_message_handler(therd, state=FSMAdmin.eq_id) 
	dp.register_message_handler(final, state=FSMAdmin.eq_cords)