import sqlite3

global db
global cursor

db = sqlite3.connect("kitDb.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS kit 
					(id_kit INT,
					 name_kit TEXT,
					 content_kit TEXT,
					 id_content_kit TEXT)""")


def new_kit(name_kit, id_kit, content_kit, id_content_kit):
	cursor.execute(f'INSERT INTO kit VALUES(?, ?, ?, ?)',(id_kit,name_kit,content_kit,id_content_kit))
	db.commit()
	return 1


def kits():
	out = []
	for i in cursor.execute('SELECT id_kit, name_kit, content_kit FROM kit'):
		out+=[i]
	if len(out)>0:
		return out
	else: return 0


def content_of_kit(name_kit):
	out = []
	for i in cursor.execute(f'SELECT id_content_kit, content_kit FROM kit WHERE name_kit = ?',(name_kit,)):
		out+=[i]
	if len(out)>0:
		return out
	else: return 0
	
