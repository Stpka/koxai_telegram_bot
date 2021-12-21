from config import admin_id, bot, dp


	
async def db_now(x):
	'''Status DB Now'''
	if x != 0:
		await bot.send_message(chat_id=admin_id,text='БД сейчас: '+str(x))
		return 1
	else:
		await bot.send_message(chat_id=admin_id,text='В БД ничего нет((')
		return 0


async def chmod(user_id):
	'''Mod User'''
	if user_id != admin_id:
		await bot.send_message(chat_id=user_id, text='У вас нет прав администратора для выполнения этой команды!')
		return 0
	else: return 1