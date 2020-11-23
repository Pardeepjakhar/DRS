import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial
import threading
import time
import imutils

stream=cv2.VideoCapture("clip2.mp4")
flag = True
def play(speed):
    global flag
    print(f"play speed is {speed}")
    frame1=stream.get((cv2.CAP_PROP_POS_FRAMES))
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed,frame= stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame, width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134,26,fill="black",font=" Time 26 bold", text="Decision Pending")
    flag=not flag

def pending(decision):
    # Display decisiom pending image
    frame=cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # wait for 1 second
    time.sleep(2)

    #Display sponser image
    frame = cv2.cvtColor(cv2.imread("logo.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # wait for 1 second
    time.sleep(2.5)

    # Display out / not_out decision
    if decision=="out":
        decisionImg="out.png"
    else:
        decisionImg="not-out.png"

    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


def not_out():
    thread = threading.Thread(target=pending, args=(" not_out",))
    thread.daemon = 1
    thread.start()
    print("you are not_out")

def out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("You are out ")

#set width and height of screen
SET_WIDTH=650
SET_HEIGHT=368

#Tkinder gui start here
window=tkinter.Tk()
window.title("DRS System by pardeep jakhar")
cv_img=cv2.cvtColor(cv2.imread("logo.png"), cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

#Create button
btn=tkinter.Button(window,text="<< Previous (Fast)", width=50 , command=partial(play,-25))
btn.pack()

btn=tkinter.Button(window,text="<< Previous (Slow)", width=50, command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window,text=" Next (Fast) >>", width=50, command=partial(play,25))
btn.pack()

btn=tkinter.Button(window,text=" Next (Slow) >>", width=50, command=partial(play,2))
btn.pack()

btn=tkinter.Button(window,text=" Give Not Out", width=50,command= not_out)
btn.pack()

btn=tkinter.Button(window,text=" Give Out ", width=50,command= out)
btn.pack()
window.mainloop()