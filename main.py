from tkinter import *
from PIL import Image,ImageTk

#Definition de la fenêtre et du canva
root = Tk()
root.geometry("1280x720")
root.title = ('NetworkSchem')
canva = Canvas(root,width=1280,height=720,bg="ivory")
canva.pack()

#Changer l'état du selecteur
def setRouter():
    sel.etat = "Router"
    
def setClient():
    sel.etat = "Client"
    
def setSwitch():
    sel.etat = "Switch"
    
def setDefault():
    sel.etat = "Selection"

#Definition des objets
class Selector():
    def __init__(self) -> None:
        self.etat = "Selection"
     
class Router():
    def __init__(self) -> None:
        self.img = (Image.open("assets/router.png"))
        self.resize = self.img.resize((100,100))
        self.image = ImageTk.PhotoImage(self.resize)
        
    def place(self,x,y):
        canva.create_image(x,y,image=self.image,anchor=CENTER)

class Client():
    def __init__(self) -> None:
        self.img = (Image.open("assets/client.png"))
        self.resize = self.img.resize((100,100))
        self.image = ImageTk.PhotoImage(self.resize)
        
    def place(self,x,y):
        canva.create_image(x,y,image=self.image,anchor=CENTER)

class Switch():
    def __init__(self) -> None:
        self.img = (Image.open("assets/switch.png"))
        self.resize = self.img.resize((100,100))
        self.image = ImageTk.PhotoImage(self.resize)
        
    def place(self,x,y):
        canva.create_image(x,y,image=self.image,anchor=CENTER)

    
#Instancie les objets
sel = Selector()
router = Router()
client = Client()
switch = Switch()

#Fonction qui place les elements en fonction de l'état du selecteur
def placeElmt(e):
    if sel.etat == "Router":
        router.place(e.x,e.y)
    elif sel.etat == "Client":
        client.place(e.x,e.y)
    elif sel.etat == "Switch":
        switch.place(e.x,e.y)
    elif sel.etat == "Selection":
        return
        
#Gestion du Menu
toolbar = Menu(root)
root.config(menu=toolbar)
add_menu = Menu(toolbar)
add_menu.add_command(label="Selection",command=setDefault)
add_menu.add_command(label="Router",command=setRouter)
add_menu.add_command(label="Client",command=setClient)
add_menu.add_command(label="Switch",command=setSwitch)
toolbar.add_cascade(label="Ajouter",menu=add_menu)


root.bind("<ButtonPress-1>",placeElmt)
root.mainloop()