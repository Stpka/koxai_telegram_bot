from aiogram import Bot, types
from aiogram.utils import executor

from config import dp, admin_id, bot
from handlers import EqList

from handlers import commands, other, admin
admin.register_handlers_admin(dp)
EqList.register_handlers_equipment(dp)
commands.register_handlers(dp)
other.register_handlers_other(dp)



async def send_to_admin(dp):
	await bot.send_message(chat_id=admin_id, text="Добрый вечер зая)") # отправка админу сообщения при запуске бота


executor.start_polling(dp,skip_updates=True,on_startup=send_to_admin)
# skip_updates нужно для того, что бы бот не отвечал на те сообщения, которые ему
# отпровляли, когда он был не онлайн