import tkinter as tk
import random
from time import sleep
##################
width=80
height=50
pixel_size=20
ran=0.1 #chance for every block to be "True"
delay=0.2 #refresh time for every frame
##################
win=tk.Tk()
win.geometry("%sx%s"%(pixel_size*width,pixel_size*height))
win.resizable("False","False")
win.title("Game_Of_Life")
cells=[]
pixels=[]
for y in range(height):
    for x in range(width):
        X=x*pixel_size
        Y=y*pixel_size
        if random.random()<ran:
            cells.append(True)
            color="black"
        else:
            cells.append(False)
            color="gray"
        pixels.append(tk.LabelFrame(win,bg=color,borderwidth=0.5))
        pixels[(y*width)+x].place(x=X,y=Y,width=pixel_size,height=pixel_size)
def check(_X,_Y):
    check=0
    for y in range(-1,2):
        for x in range(-1,2):
            X,Y=0,0
            if (_Y+y)<0:
                Y=height+(_Y+y)
            elif (_Y+y)>=height:
                Y=(_Y+y)-height
            else:
                Y=_Y+y
            if (_X+x)<0:
                X=width+(_X+x)
            elif (_X+x)>=width:
                X=(_X+x)-width
            else:
                X=_X+x
            if (x*4)+y!=0:
                if cells[(Y*width)+X]:
                    check+=1
    if check<2 or check>3:
        return 1
    if check==3:
        return 2
while True:
    for y in range(height):
        for x in range(width):
            get=check(x,y)
            if get==1:
                pixels[(y*width)+x]["bg"]="gray"
                cells[(y*width)+x]=False
            elif get==2:
                pixels[(y*width)+x]["bg"]="black"
                cells[(y*width)+x]=True
    win.update()
    sleep(delay)
