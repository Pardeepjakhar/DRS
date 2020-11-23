import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading 
import time
import imutils

#set width and height of screen
SET_WIDTH=650
SET_HEIGHT=368

#Tkinder gui start here
window = tkinter.TK()
window.title("DRS System by pardeep jakhar")
cv_img=cv2.cvtColor(cv2.imread("logo.png"), cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()
window.mainloop()