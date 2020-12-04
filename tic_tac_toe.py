from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

def disable_all():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)

	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)

	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)

def is_winner():
	global winner
	winner = False
	if b1["text"] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
		b1.config(bg='light green')
		b2.config(bg='light green')
		b3.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "X wins!!")
		disable_all()
	elif b4["text"] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
		b4.config(bg='light green')
		b5.config(bg='light green')
		b6.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "X wins!!")
		disable_all()		
	elif b7["text"] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
		b7.config(bg='light green')
		b8.config(bg='light green')
		b9.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "X wins!!")
		disable_all()		

	elif b1["text"] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
		b1.config(bg='light green')
		b4.config(bg='light green')
		b7.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "X wins!!")
		disable_all()		

	elif b2["text"] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
		b2.config(bg='light green')
		b5.config(bg='light green')
		b8.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "X wins!!")
		disable_all()	

	elif b3["text"] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
		b3.config(bg='light green')
		b6.config(bg='light green')
		b9.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "X wins!!")
		disable_all()	

	elif b1["text"] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
		b1.config(bg='light green')
		b5.config(bg='light green')
		b9.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "X wins!!")
		disable_all()		

	elif b3["text"] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
		b3.config(bg='light green')
		b5.config(bg='light green')
		b7.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "X wins!!")
		disable_all()			

	# For O's	

	if b1["text"] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
		b1.config(bg='light green')
		b2.config(bg='light green')
		b3.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "O wins!!")
		disable_all()
	elif b4["text"] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
		b4.config(bg='light green')
		b5.config(bg='light green')
		b6.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "O wins!!")
		disable_all()		
	elif b7["text"] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
		b7.config(bg='light green')
		b8.config(bg='light green')
		b9.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "O wins!!")
		disable_all()		

	elif b1["text"] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
		b1.config(bg='light green')
		b4.config(bg='light green')
		b7.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "O wins!!")
		disable_all()		

	elif b2["text"] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
		b2.config(bg='light green')
		b5.config(bg='light green')
		b8.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "O wins!!")
		disable_all()	

	elif b3["text"] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
		b3.config(bg='light green')
		b6.config(bg='light green')
		b9.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "O wins!!")
		disable_all()	

	elif b1["text"] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
		b1.config(bg='light green')
		b5.config(bg='light green')
		b9.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "O wins!!")
		disable_all()		

	elif b3["text"] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
		b3.config(bg='light green')
		b5.config(bg='light green')
		b7.config(bg='light green')
		winner = True
		messagebox.showinfo("Tic Tac Toe", "O wins!!")
		disable_all()	

	if count == 9 and winner == False:
		messagebox.showinfo("Tic Tac Toe", "Its a tie!")
		disable_all()
		print(count)

def clicko(btn):
	global clicked, count
	if btn['text'] == " " and clicked == True:
		btn['text'] = "X"
		clicked = False
		count += 1
		is_winner()
	elif btn['text'] == " " and clicked == False:
		btn['text'] = "O"
		clicked = True
		count += 1
		is_winner()
	else:
		messagebox.showerror("Tic Tac Toe", "Hey! That box is already filled")


def reset():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9
	global clicked, count
	clicked = True
	count = 0
	b1 = Button(root, text=" ", height=3, width=6, font=("Helvetica", 20), bg="white", command=lambda: clicko(b1))
	b2 = Button(root, text=" ", height=3, width=6, font=("Helvetica", 20), bg="white", command=lambda: clicko(b2))
	b3 = Button(root, text=" ", height=3, width=6, font=("Helvetica", 20), bg="white", command=lambda: clicko(b3)) 

	b4 = Button(root, text=" ", height=3, width=6, font=("Helvetica", 20), bg="white", command=lambda: clicko(b4))
	b5 = Button(root, text=" ", height=3, width=6, font=("Helvetica", 20), bg="white", command=lambda: clicko(b5))
	b6 = Button(root, text=" ", height=3, width=6, font=("Helvetica", 20), bg="white", command=lambda: clicko(b6))

	b7 = Button(root, text=" ", height=3, width=6, font=("Helvetica", 20), bg="white", command=lambda: clicko(b7))
	b8 = Button(root, text=" ", height=3, width=6, font=("Helvetica", 20), bg="white", command=lambda: clicko(b8))
	b9 = Button(root, text=" ", height=3, width=6, font=("Helvetica", 20), bg="white", command=lambda: clicko(b9))

	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)

	b4.grid(row=1, column=0)
	b5.grid(row=1, column=1)
	b6.grid(row=1, column=2)

	b7.grid(row=2, column=0)
	b8.grid(row=2, column=1)
	b9.grid(row=2, column=2)

res_menu = Menu(root)
root.config(menu=res_menu)

options_menu = Menu(res_menu, tearoff=False)
res_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset game", command=reset)

reset()
root.mainloop()
