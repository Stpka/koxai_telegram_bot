import sqlite3

global db
global cursor

db = sqlite3.connect("data_base.db")
cursor = db.cursor()

#Создание таблицы
# поддерживаемые типы данных -null, integer, real, text и blob
cursor.execute("""CREATE TABLE IF NOT EXISTS users 
				  (id INT,
				   title)
			   """)


# Рабочие функции
def oformlenie_protocola(user_id, user_title):
	cursor.execute(f'SELECT id FROM users WHERE id = {user_id}')
	if cursor.fetchone() is None:
		cursor.execute(f'INSERT INTO users VALUES(?, ?)', (user_id, user_title))
		db.commit()
		return 1
	else: return 0

def up_title(user_id, new_title):
	cursor.execute(f'UPDATE users SET title = ? WHERE id = ?',(new_title,user_id))
	db.commit()
	return 1

def po_familii(user_id):
	out = []
	for i in cursor.execute(f' SELECT title FROM users WHERE id = {user_id}'):
		out+=[i]
	return (out[-1])

def doclad():
	out = []
	for i in cursor.execute('SELECT id, title FROM users'):
		out+=[i]
	#print(out)
	if len(out)>0:
		return out
	else: return 0


def delete_protocol(user_id):
	cursor.execute(f'SELECT id FROM users WHERE id = {user_id}')
	if cursor.fetchone() is None:
		return 0
	else:
		sql = f'DELETE FROM users WHERE id = {user_id}'
		cursor.execute(sql)
		db.commit()
		return 1


# Консольные функции
def protocol():
	user_id = input('ID:')
	user_title = input('TITLE:')
	cursor.execute(f'INSERT INTO users VALUES({user_id},{user_title})')# перемеенные из форматирования можно брать в ковачки, тогда всё будет ок
	db.commit()

def update_protocol():
	LastID = input('last: ')
	NewID = input('New: ')
	sql = f'UPDATE users SET id = {NewID} WHERE id = {LastID}'
	cursor.execute(sql)
	db.commit()


def delete_protocol_console():
	user_id = input("ID: ")
	sql = f'DELETE FROM users WHERE id = {user_id}'
	cursor.execute(sql)
	db.commit()


def donos():
	user_id = input('DONOS NA:')
	for i in cursor.execute(f'SELECT title FROM users WHERE id = {user_id}'):
		i = i[0]
		print(i)


