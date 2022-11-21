from tkinter import *
from PIL import Image,ImageTk

routerList=[]


#Definition de la fenêtre et du canva
root = Tk()
root.geometry("1280x720")
root.title('NetworkSchem')
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
     
     
class Elements():
    
    def __init__(self) -> None:
        self.routerList = []
        self.clientList = []
        self.SwitchList = []
         
    class Router():
        def __init__(self) -> None:
            self.img = (Image.open("assets/router.png"))
            self.resize = self.img.resize((100,100))
            self.image = ImageTk.PhotoImage(self.resize)
            self.id = len(routerList)
            self.displayname=f'router{self.getID()}'
            self.edit_menu = Menu(root)
            self.edit_menu.add_command(label="Rename",command=self.rename_menu)
            self.edit_menu.add_command(label="Delete",command=self.remove)
        
        def getID(self):
            return self.id

        def place(self,x,y):
            self.placeimg = canva.create_image(x,y,image=self.image,anchor=CENTER)
            self.name = canva.create_text(x,y+40,text=self.displayname)
            routerList.append(self.displayname)
            canva.tag_bind(self.placeimg,"<Button-3>",self.edit)
            
        
        def edit(self,e):
            #Bind la popup du menu clique droit
            try:
                self.edit_menu.tk_popup(e.x_root,e.y_root)
            finally:
                #Revient à la normal après l'utilisation
                self.edit_menu.grab_release()
        
        def rename_menu(self):
            self.rename_window = Toplevel(root)
            self.rename_window.title("Rename")
            self.rename_window.geometry("200x150")
            self.rename_entry = Entry(self.rename_window)
            self.rename_entry.insert(0,canva.itemcget(self.name,'text'))
            self.rename_entry.pack(side="top")
            self.confirm_button = Button(self.rename_window,text="Rename",command=self.rename)
            self.confirm_button.pack(side="bottom")
        
        def rename(self):
            self.new_name = self.rename_entry.get()
            canva.itemconfig(self.name,text=self.new_name)
            self.rename_window.destroy()
        
        def remove(self):
            canva.delete(self.placeimg)
            canva.delete(self.name)
            
        
    class Client():
        def __init__(self) -> None:
            self.img = (Image.open("assets/client.png"))
            self.resize = self.img.resize((100,100))
            self.image = ImageTk.PhotoImage(self.resize)
            self.id = 0
            self.edit_menu = Menu(root)
            self.edit_menu.add_command(label="Rename")
            self.edit_menu.add_command(label="Delete")
            
        def getID(self):
            return self.id
            
        def place(self,x,y):
            canva.create_image(x,y,image=self.image,anchor=CENTER)
            self.name = canva.create_text(x,y+60,text=f'client{self.getID()}')
            canva.tag_bind(self.placeimg,"<Button-3>",self.edit)
            self.id +=1
        
        def edit(self,e):
            #Bind la popup du menu
            try:
                self.edit_menu.tk_popup(e.x_root,e.y_root)
            finally:
                #Après l'utilisation de la popup, revient à la normal
                self.edit_menu.grab_release()
            

    class Switch():
        def __init__(self) -> None:
            self.img = (Image.open("assets/switch.png"))
            self.resize = self.img.resize((100,100))
            self.image = ImageTk.PhotoImage(self.resize)
            self.id = 0
            self.edit_menu = Menu(root)
            self.edit_menu.add_command(label="Rename")
            self.edit_menu.add_command(label="Delete")
            
        def getID(self):
            return self.id   
            
        def place(self,x,y):
            canva.create_image(x,y,image=self.image,anchor=CENTER)
            self.name = canva.create_text(x-15,y+35,text=f'switch{self.getID()}')
            canva.tag_bind(self.placeimg,"<Button-3>",self.edit)
            self.id +=1
            
        def edit(self,e):
            try:
                self.edit_menu.tk_popup(e.x_root,e.y_root)
            finally:
                self.edit_menu.grab_release()
            
        

#Instancie les objets
sel = Selector()
router = Router()
client = Client()
switch = Switch()

#Fonction qui place les elements en fonction de l'état du selecteur
def placeElmt(e):
    if sel.etat == "Router":
        rout = Router()
        rout.place(e.x,e.y)
    elif sel.etat == "Client":
        client.place(e.x,e.y)
    elif sel.etat == "Switch":
        switch.place(e.x,e.y)
    elif sel.etat == "Selection":
        return
        
#Gestion des Menu
toolbar = Menu(root)
root.config(menu=toolbar)
add_menu = Menu(toolbar)
add_menu.add_command(label="Selection",command=setDefault)
add_menu.add_command(label="Router",command=setRouter)
add_menu.add_command(label="Client",command=setClient)
add_menu.add_command(label="Switch",command=setSwitch)
toolbar.add_cascade(label="Ajouter",menu=add_menu)

##Menu clique droit


root.bind("<ButtonPress-1>",placeElmt)
root.mainloop()