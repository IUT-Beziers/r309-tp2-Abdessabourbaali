  ################################
 #                                #
# Application: BAALI Abdessabour RT2 #
 #                                #
  ################################

from tkinter import *
import tkinter as tk
from tkinter import ttk
import random

fen = Tk()
fen.geometry("1500x800")
fen.title("GNS4 Topolgy")

reseau = Canvas(fen, width=1500, height=800, bg="light blue")

#Create New File
def newfile():
    pass

PCImage = PhotoImage(file = "equipement/pc.png")
RouterImage = PhotoImage(file = "equipement/router.png")
SwitchImage = PhotoImage(file = "equipement/switch.png")

menubar = Menu(fen, bg = "light green")
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Equipement", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="PC", image=PCImage, compound="bottom", command=lambda: add_PC())
filemenu.add_separator()
filemenu.add_command(label="Router", image=RouterImage, compound="bottom", command=lambda: add_router())
filemenu.add_separator()
filemenu.add_command(label="Switch", image=SwitchImage, compound="bottom", command=lambda: add_switch())

menubar.add_cascade(label="Lien", menu=editmenu)

fen.config(menu=menubar)

def add_PC():
    global image1, PC
    image1 = tk.PhotoImage(file = "equipement/pc.png") 
    PC = reseau.create_image (random.randint(0,600), random.randint (0,500), image=image1)
    

def add_router():
    global image2, router
    image2 = tk.PhotoImage(file = "equipement/router.png") 
    router = reseau.create_image (random.randint(0,600), random.randint (0,500), image=image2)

def add_switch():
    global image3, switch
    image3 = tk.PhotoImage(file = "equipement/switch.png")
    switch = reseau.create_image (random.randint(0,600), random.randint (0,500), image=image3)

def callback(event):
    global fichier
    #l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
    fichier = tk.PhotoImage(file = "equipement/pc.png") 

def callback1(event):
    global fichier1
    #l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
    fichier1 = tk.PhotoImage(file = "equipement/router.png") 

def callback2(event):
    global fichier2
    #l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
    fichier2 = tk.PhotoImage(file = "equipement/switch.png")
     

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
#image = reseau.create_image(180, 50,  image=fichier,anchor="nw")

#Router

#fichier1 = tk.PhotoImage(file = "equipement/router.png")
#fichier1 = PhotoImage(file="equipement/router.png")

#image = reseau.create_image(500, 50, image=fichier1, anchor="nw")

#Switch

#fichier2 = tk.PhotoImage(file = "equipement/switch.png")
#fichier2 = PhotoImage(file="equipement/switch.png")

#image = reseau.create_image(1200, 50, image=fichier2, anchor="nw")

fen.bind('<B1-Motion>',add_PC)
fen.bind('<B1-Motion>',callback1)
fen.bind('<B1-Motion>',callback2)    # Mouse left button pressed movemy_w.mainloop()
reseau.pack()
fen.mainloop()