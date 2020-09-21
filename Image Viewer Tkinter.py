# Python Program to Design a Image Viewer

from tkinter import *
from PIL import ImageTk, Image 
from keyboard import on_press_key

window = Tk()
window.title("Python sImage Viewer")

window.iconbitmap("favicon.ico")

window.geometry("810x500")

img_on_screen = 1


def back_forward_part():
	label = Label(image = image_list[img_on_screen%5])
	label.grid(row=2,column=1,columnspan=3)
	
	forward_button.grid(row=2,column=4,padx=5,pady=5)
	back_button.grid(row=2,column=0,padx=5,pady=5)
	exit_button.grid(row=3,column=2,pady=5)

def forward():

	global img_on_screen, label
	label.grid_forget()

	img_on_screen += 1

	back_forward_part()

def back():
	global img_on_screen, label
	label.grid_forget()
	img_on_screen -= 1
	
	back_forward_part()

empty_line = Label(window, text="\n")
header = Label(window, text = "Image Viewer", font=("Arial Bold",20,'underline'))
back_button = Button(window, text = "<<", command = lambda: back(), fg="yellow", bg="black")
forward_button = Button(window, text = ">>", command = lambda: forward(), fg="yellow", bg="black")
exit_button = Button(window, text = "Exit", command = window.quit, fg="yellow", bg="black")

image_1 = ImageTk.PhotoImage(Image.open("India.jpg"))
image_2 = ImageTk.PhotoImage(Image.open("United Kingdom.png"))
image_3 = ImageTk.PhotoImage(Image.open("Canada.jpg"))
image_4 = ImageTk.PhotoImage(Image.open("USA.jpg"))
image_5 = ImageTk.PhotoImage(Image.open("Australia.jpg"))

label = Label(image = image_1)

image_list = [image_1, image_2, image_3, image_4, image_5]

empty_line.grid(row=1,column=0)
header.place(x=315,y=0)
label.grid(row=2,column=1, columnspan=3)
forward_button.grid(row=2,column=4,padx=5,pady=5)
back_button.grid(row=2,column=0,padx=5,pady=5)
exit_button.grid(row=3,column=2,pady=5)

on_press_key("right", lambda _: forward())
on_press_key("left", lambda _: back())
on_press_key("esc", lambda _:window.quit())

window.mainloop()