import sqlite3

global db
global cursor

db = sqlite3.connect("equipment_list.db")
cursor = db.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS equipment 
				  (id INT,
				   name TEXT,
				   coord TEXT)
			   """)



def new_line(eq_id, eq_name, eq_cord):
	cursor.execute(f'INSERT INTO equipment VALUES(?, ?, ?)',(eq_id,eq_name,eq_cord))
	db.commit()
	return 1


def print_db():
	out = []
	for i in cursor.execute('SELECT id, name, coord FROM equipment'):
		out+=[i]
	#print(out)
	if len(out)>0:
		return out
	else: return 0


def print_coord_eq(eq_id):
	out = []
	for i in cursor.execute(f'SELECT coord FROM equipment WHERE id = ?',(eq_id,)):
		out+=[i]
	if len(out)>0:	return out[0][0]
	else:			return 0