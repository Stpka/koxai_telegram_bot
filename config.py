from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = "2070520934:AAHgWpbtgR--FDMcWhYOI6PT7b-snJ3Etu8"
admin_id = 818968887
storage=MemoryStorage()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
