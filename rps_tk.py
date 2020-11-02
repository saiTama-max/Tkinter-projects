from tkinter import *
import random

root = Tk()

root.title("RPS")
root.geometry('500x300')
root.configure(bg='light grey')

options = ['rock', 'paper', 'scissors']
score = 0
comp_score = 0
colors = ['orange', 'red', 'blue', 'green', 'yellow', 'purple']


win_lbl = Label(root, font="Verdana 10", bg='light grey')
comp_lbl = Label(root, font="Verdana 10", bg='light grey')
score_lbl = Label(root, text='Your score - 0', font="Verdana 10", bg='light grey')
comp_scr_lbl = Label(root, text='CPU score - 0', font="Verdana 10", bg='light grey')


def rock():
	global score, comp_score
	if random.choice(options) == 'scissors':
		comp_lbl.config(text=f'Computer chose scissors', font="Verdana 10", fg=random.choice(colors))
		win_lbl.config(text='You win!', font="Verdana 10", justify='center')
		score += 1
		score_lbl.config(text=f'Your score - {score}', font="Verdana 10", bg='light grey')

	elif random.choice(options) == 'rock':
		comp_lbl.config(text=f'Computer chose rock', font="Verdana 10", fg=random.choice(colors))
		win_lbl.config(text='  Tie!', font="Verdana 10", justify='center')
		
	else:
		comp_lbl.config(text=f'Computer chose paper', font="Verdana 10", fg=random.choice(colors))
		win_lbl.config(text='You lose!', font="Verdana 10", justify='center')
		comp_score += 1
		comp_scr_lbl.config(text=f'CPU score - {comp_score}', font="Verdana 10", bg='light grey')



def paper():
	global score, comp_score
	if random.choice(options) == 'rock':
		comp_lbl.config(text=f'Computer chose rock', font="Verdana 10", fg=random.choice(colors))
		win_lbl.config(text='You win!', font="Verdana 10", justify='center')
		score += 1
		score_lbl.config(text=f'Your score - {score}', font="Verdana 10", bg='light grey')
	elif random.choice(options) == 'paper':
		comp_lbl.config(text=f'Computer chose paper', font="Verdana 10", fg=random.choice(colors))
		win_lbl.config(text='  Tie!', font="Verdana 10", justify='center')
	
	else:
		comp_lbl.config(text=f'Computer chose scissors', font="Verdana 10", fg=random.choice(colors))
		win_lbl.config(text='You lose!', font="Verdana 10", justify='center')
		comp_score += 1
		comp_scr_lbl.config(text=f'CPU score - {comp_score}', font="Verdana 10", bg='light grey')

def scissors():
	global score, comp_score
	if random.choice(options) == 'paper':
		comp_lbl.config(text=f'Computer chose paper', font="Verdana 10", fg=random.choice(colors))
		win_lbl.config(text='You win!', font="Verdana 10", justify='center')
		score += 1
		score_lbl.config(text=f'Your score - {score}', font="Verdana 10", bg='light grey')
	elif random.choice(options) == 'scissors':
		comp_lbl.config(text=f'Computer chose scissors', font="Verdana 10", fg=random.choice(colors))
		win_lbl.config(text='  Tie!', font="Verdana 10", justify='center')
		
	else:
		comp_lbl.config(text=f'Computer chose rock', font="Verdana 10", fg=random.choice(colors))
		win_lbl.config(text='You lose!', font="Verdana 10", justify='center')
		comp_score += 1
		comp_scr_lbl.config(text=f'CPU score - {comp_score}', font="Verdana 10", bg='light grey')


select_lbl = Label(root, text="Choose from below (Rock, Paper, Scissor)", font="Verdana 14 bold", fg=random.choice(colors), bg='light grey')
select_lbl.place(x=30, y=10)

rock_btn = Button(root, text="Rock", bg='light pink', activebackground='light pink', command=rock)
rock_btn.place(width=70, height=35, x=70, y=80)

paper_btn = Button(root, text="Paper", bg='light green', activebackground='light green', command=paper)
paper_btn.place(width=70, height=35,x=215, y=80)

scissors_btn = Button(root, text="Scissors", bg='light blue', activebackground='light blue', command=scissors)
scissors_btn.place(width=70, height=35,x=360, y=80)

win_lbl.place(x=218, y=190)
comp_lbl.place(x=170, y=150)

score_lbl.place(x=10, y=250)
comp_scr_lbl.place(x=120, y=250)

root.mainloop()
