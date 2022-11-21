  ################################
 #                                #
# Application: BAALI Abdessabour RT2 #
 #                                #
  ################################

from tkinter import *
import tkinter as tk
from tkinter import ttk

fen = Tk()
fen.geometry("1500x800")
fen.title("GNS4 Topolgy")

pkt = Canvas(fen, width=1500, height=800, bg='light blue')

#Create New File
def newfile():
    pass

PCImage = PhotoImage(file = "equipement/pc.png")
RouterImage = PhotoImage(file = "equipement/router.png")
SwitchImage = PhotoImage(file = "equipement/switch.png")

menubar = Menu(fen)
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Equipement", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="PC", image=PCImage, compound="bottom")
filemenu.add_separator()
filemenu.add_command(label="Router", image=RouterImage, compound="bottom")
filemenu.add_separator()
filemenu.add_command(label="Switch", image=SwitchImage, compound="bottom")

menubar.add_cascade(label="Lien", menu=editmenu)

fen.config(menu=menubar)

def add_labelPC():
   global label
   label=Label(fen, file = "equipement/pc.png")
   label.pack()

addPC=ttk.Button(fen, file = "equipement/pc.png", command=add_labelPC)
addPC.pack(anchor=W, pady=10)

def callback(event):
    global fichier
    #l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
    fichier = tk.PhotoImage(file = "equipement/pc.png") 
    image = pkt.create_image (event.x,event.y,image=fichier)

def callback1(event):
    global fichier1
    #l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
    fichier1 = tk.PhotoImage(file = "equipement/router.png") 
    image = pkt.create_image (event.x,event.y,image=fichier1)

def callback2(event):
    global fichier2
    #l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
    fichier2 = tk.PhotoImage(file = "equipement/switch.png") 
    image = pkt.create_image (event.x,event.y,image=fichier2)
     

#l1=tk.Label(fen,text='to Display',bg='yellow',font=30)
#l1.pack(padx=10,pady=5)

#Redimmensionnement des images

#image = Image.open("equipement/pc.png")         # Read the Image

#resize_image = image.resize(width=100, height=100)    # Resize the image using resize() method

#img = ImageTk.PhotoImage(resize_image)

#label1 = Label(image=img)
#label1.image = img
#label1.pack()

#PC

#fichier = tk.PhotoImage(file = "equipement/pc.png")

#fichier = PhotoImage(file="equipement/pc.png")
#image = pkt.create_image(180, 50,  image=fichier,anchor="nw")

#Router

#fichier1 = tk.PhotoImage(file = "equipement/router.png")
#fichier1 = PhotoImage(file="equipement/router.png")

#image = pkt.create_image(500, 50, image=fichier1, anchor="nw")

#Switch

#fichier2 = tk.PhotoImage(file = "equipement/switch.png")
#fichier2 = PhotoImage(file="equipement/switch.png")

#image = pkt.create_image(1200, 50, image=fichier2, anchor="nw")

fen.bind('<B1-Motion>',callback)
fen.bind('<B1-Motion>',callback1)
fen.bind('<B1-Motion>',callback2)    # Mouse left button pressed movemy_w.mainloop()
pkt.pack()
fen.mainloop()