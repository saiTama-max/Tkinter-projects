from tkinter import *
import sqlite3
from PIL import ImageTk, Image

root = Tk()
root.title("Databases")
# root.geometry('350x350')
root.configure(bg='light grey')

# bg_img = ImageTk.PhotoImage(Image.open('images/deadly_sins.jpg'))
# img_lbl = Label(root, image=bg_img)
# img_lbl.grid(row=0, column=0)

conn = sqlite3.connect('address_book.db')
c = conn.cursor()
# Databases 

'''
 conn.execute("""CREATE TABLE addresses (
             first_name text,
             last_name text,
             address text,
             city text,
             state text,
             zipcode integer)""")'''

def update():
	# global editor
	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()

	record_id = delete_box.get()
	c.execute("""UPDATE addresses SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		state = :state,
		zipcode = :zipcode

		WHERE oid=:oid""",
		{
		'first': f_name_edit.get(),
		'last': l_name_edit.get(),
		'address': address_edit.get(),
		'city': city_edit.get(),
		'state': state_edit.get(),
		'zipcode': zipcode_edit.get(),
		'oid': record_id
		})


	conn.commit()
	conn.close()

	editor.destroy()

def edit():
	global editor
	global f_name_edit
	global l_name_edit
	global address_edit
	global city_edit
	global state_edit
	global zipcode_edit


	editor = Tk()
	editor.title("Edit Record")
	editor.configure(bg='light grey')
	editor.geometry('350x300')

	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()

	record_id = delete_box.get()
	c.execute("SELECT * FROM addresses WHERE oid= " + record_id)
	records = c.fetchall()

	f_name_edit = Entry(editor, width=30)
	f_name_edit.grid(row=0, column=1, padx=20, pady=(10, 0))

	l_name_edit = Entry(editor, width=30)
	l_name_edit.grid(row=1, column=1)

	address_edit = Entry(editor, width=30)
	address_edit.grid(row=2, column=1)

	city_edit = Entry(editor, width=30)
	city_edit.grid(row=3, column=1)

	state_edit = Entry(editor, width=30)
	state_edit.grid(row=4, column=1)

	zipcode_edit = Entry(editor, width=30)
	zipcode_edit.grid(row=5, column=1)


	f_name_lbl = Label(editor, text="First name", bg=('light grey'))
	f_name_lbl.grid(row=0, column=0, pady=(10, 0))

	l_name_lbl = Label(editor, text="Last name", bg=('light grey'))
	l_name_lbl.grid(row=1, column=0)

	address_lbl = Label(editor, text="Address", bg=('light grey'))
	address_lbl.grid(row=2, column=0)

	city_lbl = Label(editor, text="City", bg=('light grey'))
	city_lbl.grid(row=3, column=0)

	state_lbl = Label(editor, text="State", bg=('light grey'))
	state_lbl.grid(row=4, column=0)

	zipcode_lbl = Label(editor, text="Zipcode", bg=('light grey'))
	zipcode_lbl.grid(row=5, column=0)

	for record in records:
		f_name_edit.insert(0, record[0])
		l_name_edit.insert(0, record[1])
		address_edit.insert(0, record[2])
		city_edit.insert(0, record[3])
		state_edit.insert(0, record[4])
		zipcode_edit.insert(0, record[5])

	save_btn = Button(editor, text="Save record", command=update)
	save_btn.grid(row=6, column=1, pady=(0, 10))





def delete():
	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()

	c.execute("DELETE FROM addresses WHERE oid= " + delete_box.get())
	delete_box.delete(0, END)

	conn.commit()
	conn.close()

def submit():
	# connect to a database or create
	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()


	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'address': address.get(),
				'city': city.get(),
				'state': state.get(),
				'zipcode': zipcode.get()
			})

	conn.commit()
	conn.close()

	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)



def query():
	conn = sqlite3.connect('address_book.db')
	c = conn.cursor()


	c.execute("SELECT *, oid FROM addresses")
	records = c.fetchall()
	print_records = ''
	for record in records:
		print_records += str(record[0]) + ' ' + str(record[1]) + '\t' + str(record[6]) + '\n'

	query_lbl = Label(root, text=print_records, justify=LEFT)
	query_lbl.grid(row=12, column=0, columnspan=2)

	conn.commit()
	conn.close()

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

f_name_lbl = Label(root, text="First name", bg=('light grey'))
f_name_lbl.grid(row=0, column=0, pady=(10, 0))

l_name_lbl = Label(root, text="Last name", bg=('light grey'))
l_name_lbl.grid(row=1, column=0)

address_lbl = Label(root, text="Address", bg=('light grey'))
address_lbl.grid(row=2, column=0)

city_lbl = Label(root, text="City", bg=('light grey'))
city_lbl.grid(row=3, column=0)

state_lbl = Label(root, text="State", bg=('light grey'))
state_lbl.grid(row=4, column=0)

zipcode_lbl = Label(root, text="Zipcode", bg=('light grey'))
zipcode_lbl.grid(row=5, column=0)

del_lbl = Label(root, text='ID Number', bg=('light grey'))
del_lbl.grid(row=9, column=0)

submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=7, column=0, columnspan=3, pady=10, padx=10, ipadx=127)

del_btn = Button(root, text="Delete record", command=delete, bg=("red"))
del_btn.grid(row=11, column=1, pady=10)

edit_btn = Button(root, text="Edit record", command=edit)
edit_btn.grid(row=10, column=1, pady=(10, 10))


conn.commit()
conn.close()

root.mainloop()