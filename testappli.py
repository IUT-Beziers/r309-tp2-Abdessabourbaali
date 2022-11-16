  ################################
 #                                #
# Exercice4: BAALI Abdessabour RT2 #
 #                                #
  ################################

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

fen = Tk()
fen.geometry("2000x2000")
fen.title("Exercice 4")

chess = Canvas(fen, width=2000, height=2000, bg='light blue')

def callback(event):
    global fichier
    #l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
    fichier = tk.PhotoImage(file = "equipement/pc.png") 
    image = chess.create_image (event.x,event.y,image=fichier)

def callback1(event):
    global fichier1
    #l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
    fichier1 = tk.PhotoImage(file = "equipement/router.png") 
    image = chess.create_image (event.x,event.y,image=fichier1)

def callback2(event):
    global fichier2
    #l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))
    fichier2 = tk.PhotoImage(file = "equipement/switch.png") 
    image = chess.create_image (event.x,event.y,image=fichier2)
     

#l1=tk.Label(fen,text='to Display',bg='yellow',font=30)
#l1.pack(padx=10,pady=5)

#Redimmensionnement des images


image = Image.open("equipement/pc.png")         # Read the Image

resize_image = image.resize((width=100, height=100))    # Resize the image using resize() method

img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img)
label1.image = img
label1.pack()

#PC

fichier = tk.PhotoImage(file = "equipement/pc.png")

fichier = PhotoImage(file="equipement/pc.png")
image = chess.create_image(180, 50,  image=fichier,anchor="nw")

#Router

fichier1 = tk.PhotoImage(file = "equipement/router.png")
fichier1 = PhotoImage(file="equipement/router.png")

image = chess.create_image(500, 50, image=fichier1, anchor="nw")

#Switch

fichier2 = tk.PhotoImage(file = "equipement/switch.png")
fichier2 = PhotoImage(file="equipement/switch.png")

image = chess.create_image(1200, 50, image=fichier2, anchor="nw")

fen.bind('<B1-Motion>',callback)
fen.bind('<B1-Motion>',callback1)
fen.bind('<B1-Motion>',callback2)    # Mouse left button pressed movemy_w.mainloop()
chess.pack()
fen.mainloop()