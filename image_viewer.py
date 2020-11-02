from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image viewer")


def forward(image_num):
    global my_label
    global button_back
    global button_forward
    global status

    my_label.grid_forget()
    my_label = Label(image=img_list[image_num - 1])
    button_forward = Button(root, text=">>", padx=10, command=lambda: forward(image_num + 1))
    button_back = Button(root, text="<<", padx=10, command=lambda: back(image_num - 1))
    if image_num == 5:
        button_forward = Button(root, text=">>", state=DISABLED)
    
    status = Label(root, text="Image " + str(image_num) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1 ,column=2)
    button_back.grid(row=1, column=0)


def back(image_num):
    global my_label
    global button_back
    global button_forward
    global status

    my_label.grid_forget()
    my_label = Label(image=img_list[image_num - 1])
    button_forward = Button(root, text=">>", padx=10, command=lambda: forward(image_num + 1))
    button_back = Button(root, text="<<", padx=10, command=lambda: back(image_num - 1))
    if image_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    
    status = Label(root, text="Image " + str(image_num) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1 ,column=2)
    button_back.grid(row=1, column=0)

my_img1 = ImageTk.PhotoImage(Image.open('images/deadly_sins.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/todoriki.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('images/izuku.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('images/sasuke.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('images/inosuke.jpg'))


img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
status = Label(root, text="Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<", padx=10, command=back)
button_forward = Button(root, text=">>", padx=10, command=lambda: forward(2))
button_exit = Button(root, text="Exit", padx=20, command=root.quit)


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1 ,column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()