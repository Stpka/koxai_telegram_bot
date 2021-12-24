from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from config import dp, bot, admin_id

import sys
sys.path.append('..')
from db import containerDbFunc
from db import dbFunc
from db import eqipDbFunc
'''
import db.containerDbFunc as containerDbFunc
from containerDbFunc import content_of_kit
import db.dbFunc as dbFunc

'''


class NewKit(StatesGroup):
	name_kit = State()
	id_kit = State()
	content_kit = State()
	id_content_kit = State()



async def frst(message : types.Message):
	await message.answer('ВНИМАНИЕ!\nВесь далее вводимый текст записывайте в ОДНУ строку')
	await NewKit.name_kit.set()
	await message.answer('Введите название нового набора')


async def secnd(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['name_kit']=message.text
	await NewKit.next()
	await message.delete()
	await message.answer('Введите id этого набора')


async def therd(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['id_kit']=message.text
	await NewKit.next()
	await message.delete()
	await message.answer('Введите содержимое набора <b>через запятую и пробел</b>', parse_mode=types.ParseMode.HTML)


async def forth(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['content_kit']=message.text
	await NewKit.next()
	await message.delete()
	await message.answer('Введите id каждого из оборудования по порядку <b>через запятую и пробел</b>', parse_mode=types.ParseMode.HTML)


async def final(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['id_content_kit']=message.text
	
	if containerDbFunc.new_kit(data['name_kit'], data['id_kit'], data['content_kit'], data['id_content_kit']):
		await message.delete()
		await message.answer('Учтём!')
		if message.from_user.id != admin_id:
			await bot.send_message(chat_id=admin_id, text=f"Котик, {dbFunc.po_familii(message.from_user.id)} добавил новоый набор!")

	await state.finish()


def register_handlers_kit(dp : Dispatcher):
	dp.register_message_handler(frst, commands=['nkit'],state=None)
	dp.register_message_handler(secnd, state=NewKit.name_kit)
	dp.register_message_handler(therd, state=NewKit.id_kit)
	dp.register_message_handler(forth, state=NewKit.content_kit)
	dp.register_message_handler(final, state=NewKit.id_content_kit)


class MadeKit(StatesGroup):
	name_kit = State()
	final_made_kit = State()

async def NameOfKit(message : types.Message):
	await MadeKit.name_kit.set()
	await MadeKit.next()
	await message.answer('Введите название набора')

async def Final(message: types.Message, state: FSMContext):
	out = containerDbFunc.content_of_kit(message.text)[0]
	ids = out[0].split(", ")	# Все индификаторы
	names = out[1].split(", ")	# Все имена

	for i in range(0,len(ids)):
		await message.answer(f'<b>{names[i]}</b> храниться в <b>{eqipDbFunc.print_coord_eq(ids[i])}</b>', parse_mode=types.ParseMode.HTML)
	await state.finish()


def register_handlers_collect_kit(dp: Dispatcher):
	dp.register_message_handler(NameOfKit, commands=['mkit'], state=None)
	dp.register_message_handler(Final, state=MadeKit.final_made_kit)