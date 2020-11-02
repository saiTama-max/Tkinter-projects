import random
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tic_tac_toe import TicTac

root = Tk()
root.title("Login system")
root.geometry('250x250')
root.config(bg='#42f5b6')

login_img = ImageTk.PhotoImage(Image.open('images/login_btn2.png'))
signUp_img = ImageTk.PhotoImage(Image.open('images/register_btn3.png'))
del_img = ImageTk.PhotoImage(Image.open('images/delete_btn.png'))

conn = sqlite3.connect('username_login.db')
c = conn.cursor()

# comment after creating one time
conn.execute("""CREATE TABLE usernames (
            user_name text,
            pass_word text)""")
conn.execute("ALTER TABLE usernames ADD COLUMN email text")


def submit():
	# connect to a database or create
	conn = sqlite3.connect('username_login.db')
	c = conn.cursor()

	c.execute("""SELECT user_name from usernames where user_name is :user_name""",
			{
				'user_name': u_ent.get()

			})
	name = c.fetchall()
	if name != []:
		messagebox.showerror("Login", "Username already in use")
	else:
		c.execute("INSERT INTO usernames VALUES (:u_ent, :p_ent, :email)",
				{
					'u_ent': u_ent.get(),
					'p_ent': p_ent.get(),
					'email': e_ent.get()

				})

		
		messagebox.showinfo("Login", "Username created successfuly")

	conn.commit()
	conn.close()
	u_ent.delete(0, END)
	p_ent.delete(0, END)
	e_ent.delete(0, END)


def login():
	conn = sqlite3.connect('username_login.db')
	c = conn.cursor()

	c.execute("""SELECT user_name, pass_word from usernames where user_name is :user_name and pass_word is :pass_word""", 
			{
				'user_name': u_ent2.get(),
				'pass_word': p_ent2.get()
			})
	
	record = c.fetchall()
	if record == []:
		messagebox.showerror("Invalid", "Username or Password wrong")
	else:
		master.destroy()
		root.destroy()
		TicTac()

	

	print(record)


def login_create():
	global u_ent2, p_ent2, master
	master = Toplevel()
	master.geometry('250x250')
	master.configure(bg='#42f5b6')

	u_ent2 = Entry(master, width=18)
	u_ent2.place(x=85, y=35)

	u_lbl2 = Label(master, text='Username', bg='#42f5b6', font='Helventica 10')
	u_lbl2.place(x=5, y=35)

	p_ent2 = Entry(master, width=18, show='*')
	p_ent2.place(x=85, y=60)

	p_lbl2 = Label(master, text='Password', bg='#42f5b6', font='Helventica 10')
	p_lbl2.place(x=5, y=60)
	LogIn_btn2 = Button(master, image=login_img, bg='#42f5b6', borderwidth=0, activebackground='#42f5b6', command=login)
	LogIn_btn2.place(x=90, y=120)



def delete():

	conn = sqlite3.connect('username_login.db')
	c = conn.cursor()

	c.execute("""DELETE from usernames where user_name is :user_name and pass_word is :pass_word""", 
			{
				'user_name': u_ent3.get(),
				'pass_word': p_ent3.get()
			})


	names = c.rowcount
	if names == 0:
		messagebox.showerror("Login", "Invalid Account")
	else:
		messagebox.showinfo("Login", "Account Deleted")

	window.destroy()
	conn.commit()
	conn.close()

	

def delete_show():
	global u_ent3, p_ent3, window
	window = Toplevel()
	window.geometry('250x250')
	window.configure(bg='#42f5b6')
	u_ent3 = Entry(window, width=18)
	u_ent3.place(x=85, y=35)

	u_lbl3 = Label(window, text='Username', bg='#42f5b6', font='Helventica 10')
	u_lbl3.place(x=5, y=35)

	p_ent3 = Entry(window, width=18, show='*')
	p_ent3.place(x=85, y=60)

	p_lbl3 = Label(window, text='Password', bg='#42f5b6', font='Helventica 10')
	p_lbl3.place(x=5, y=60)

	del_big = Button(window, image=del_img, bg='#42f5b6', activebackground='#42f5b6', borderwidth=0,  command=delete)
	del_big.place(x=100, y=100)



u_ent = Entry(root, width=18)
u_ent.place(x=85, y=35)

u_lbl = Label(root, text='Username', bg='#42f5b6', font='Helventica 10')
u_lbl.place(x=5, y=33)

p_ent = Entry(root, width=18, show='*')
p_ent.place(x=85, y=60)

e_ent = Entry(root, width=18)
e_ent.place(x=85, y=86)

p_lbl = Label(root, text='Password', bg='#42f5b6', font='Helventica 10')
p_lbl.place(x=5, y=57)

e_lbl = Label(root, text='Email', bg='#42f5b6', font='Helventica 10')
e_lbl.place(x=5, y=81)

signUp_btn = Button(root, image=signUp_img, bg='#42f5b6', borderwidth=0, activebackground='#42f5b6', command=submit)
signUp_btn.place(x=80, y=120)

LogIn_btn = Button(root, image=login_img, bg='#42f5b6', borderwidth=0, activebackground='#42f5b6', command=login_create)
LogIn_btn.place( x=92, y=170)

conn.commit()
conn.close()

res_menu = Menu(root)
root.config(menu=res_menu)

options_menu = Menu(res_menu, tearoff=False)
res_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Delete Account", command=delete_show)


root.mainloop()


