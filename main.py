from tkinter import *
from PIL import Image,ImageTk

#Definition de la fenêtre et du canva
root = Tk()
root.geometry("1280x720")
root.title('Schama')
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

#Listes des objets crées
routerList = []
clientList = []
switchList = []

class Elements():
    def __init__(self) -> None:
        self.edit_menu = Menu(root)
        self.edit_menu.add_command(label="Rename",command=self.rename_menu)
        self.edit_menu.add_command(label="Delete",command=self.remove)
        
    def rename_menu(self):
        self.rename_window = Toplevel(root)
        self.rename_window.title("Rename")
        self.rename_window.geometry("200x150")
        self.rename_window.resizable(False,False)
        self.rename_entry = Entry(self.rename_window)
        self.rename_entry.insert(0,canva.itemcget(self.name,'text'))
        self.rename_entry.place(x=26,y=50)
        self.confirm_button = Button(self.rename_window,text="Rename",command=self.rename)
        self.confirm_button.pack(side="bottom")
    
    def edit(self,e):
        try:
            #Bind la popup du menu clique droit
            self.edit_menu.tk_popup(e.x_root,e.y_root)
        finally:
            #Revient à la normal après l'utilisation
            self.edit_menu.grab_release()
    
    def rename(self):
        self.new_name = self.rename_entry.get()
        canva.itemconfig(self.name,text=self.new_name)
        self.rename_window.destroy()
    
    def remove(self):
        canva.delete(self.placeimg)
        canva.delete(self.name)
    
    
class Router(Elements):
    def __init__(self) -> None:
        super().__init__()
        self.image = ImageTk.PhotoImage((Image.open("assets/router.png")).resize((100,100)))
        self.id = len(routerList)
        self.displayname=f'router{self.id}'
            
    def place(self,x,y):
        self.placeimg = canva.create_image(x,y,image=self.image,anchor=CENTER)
        self.name = canva.create_text(x,y+40,text=self.displayname)
        routerList.append(self.displayname)
        self.index = routerList.index(self.displayname)
        canva.tag_bind(self.placeimg,"<Button-3>",super().edit)
        canva.tag_bind(self.placeimg,"<B1-Motion>",self.move)
        
    def rename(self):
        super().rename()
        routerList[self.index] = self.new_name
    
    def remove(self):
        super().remove()
        routerList.pop(self.index)
    
    def move(self,e):
        if sel.etat != "Selection":
            return
        canva.coords(self.placeimg,e.x,e.y)
        canva.coords(self.name,e.x,e.y+40)
          
class Client(Elements):
    def __init__(self) -> None:
        super().__init__()
        self.image = ImageTk.PhotoImage((Image.open("assets/client.png")).resize((100,100)))
        self.id = len(clientList)
        self.displayname=f'client{self.id}'
        
    def place(self,x,y):
        self.placeimg = canva.create_image(x,y,image=self.image,anchor=CENTER)
        self.name = canva.create_text(x,y+60,text=self.displayname)
        clientList.append(self.displayname)
        self.index = clientList.index(self.displayname)
        canva.tag_bind(self.placeimg,"<Button-3>",self.edit)
        canva.tag_bind(self.placeimg,"<B1-Motion>",self.move)
    
    def rename(self):
        super().rename()
        clientList[self.index] = self.new_name
    
    def remove(self):
        super().remove()
        clientList.pop(self.index)
        
    def move(self,e):
        if sel.etat != "Selection":
            return
        canva.coords(self.placeimg,e.x,e.y)
        canva.coords(self.name,e.x,e.y+60)
            
class Switch(Elements):
    def __init__(self) -> None:
        super().__init__()
        self.image = ImageTk.PhotoImage((Image.open("assets/switch.png")).resize((100,100)))
        self.id = len(switchList)
        self.displayname=f'switch{self.id}'   
        
    def place(self,x,y):
        self.placeimg = canva.create_image(x,y,image=self.image,anchor=CENTER)
        self.name = canva.create_text(x-15,y+35,text=self.displayname)
        switchList.append(self.displayname)
        self.index= switchList.index(self.displayname)
        canva.tag_bind(self.placeimg,"<Button-3>",self.edit)
        canva.tag_bind(self.placeimg,"<B1-Motion>",self.move)
        
    def rename(self):
        super().rename()
        switchList[self.index] = self.new_name
    
    def remove(self):
        super().remove()
        switchList.pop(self.index)
        
    def move(self,e):
        if sel.etat != "Selection":
            return
        canva.coords(self.placeimg,e.x,e.y)
        canva.coords(self.name,e.x-15,e.y+35)
            
#Instancie le selecteur
sel = Selector()

#Fonction qui place les elements en fonction de l'état du selecteur
def placeElmt(e):
    if sel.etat == "Router":
        router = Router()
        router.place(e.x,e.y)
    elif sel.etat == "Client":
        client = Client()
        client.place(e.x,e.y)
    elif sel.etat == "Switch":
        switch = Switch()
        switch.place(e.x,e.y)
    elif sel.etat == "Selection":
        return
    
#Selection des elements avec les touches du clavier
def changeSelector(e):
    if not e.char:
        return
    elif e.char == "c":
        sel.etat = "Client"
    elif e.char == "s":
        sel.etat = "Switch"
    elif e.char == "r":
        sel.etat = "Router"
    elif e.char == "n":
        sel.etat="Selection"
    
#Gestion du menu (toolbar)
toolbar = Menu(root)
root.config(menu=toolbar)
add_menu = Menu(toolbar)
add_menu.add_command(label="Selection",command=setDefault)
add_menu.add_command(label="Router",command=setRouter)
add_menu.add_command(label="Client",command=setClient)
add_menu.add_command(label="Switch",command=setSwitch)
toolbar.add_cascade(label="Ajouter",menu=add_menu)

#Gestion des callbacks
root.bind("<ButtonPress-1>",placeElmt)
root.bind("<KeyPress>",changeSelector)
root.mainloop()