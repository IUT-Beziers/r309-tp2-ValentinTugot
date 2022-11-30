from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

#-----------------------------------#
#Définition de la fenêtre principale
#-----------------------------------#
root = Tk()
root.geometry("1280x720")
root.title('Network Plan')

#-----------------------------------#
#Définition de la fenêtre d'aide
#-----------------------------------#
help_window = Toplevel(root)
help_window.title("Help")
help_window.geometry("500x500")
help_window.resizable(False,False)
label_text= """

Liste des commandes disponibles:

Clique Gauche - Permet de placer les éléments après les avoir selectionnés.
R - Séléctionne les Routers
C - Séléctionne les clients
S - Sélectionne les Switchs
N - Enlever la sélection

La sélection peut également s'éffectuer depuis le menu \"Add".

Un clique droit sur un élément permet de le modifier:
- Renommer
- Supprimer
- Changer son icône

Il faut être en mode Séléction pour déplacer les éléments.
            """
help_window_label = Label(help_window,text=label_text)
help_window_label.place(x=30,y=100)
help_window_button = Button(help_window,text="OK",command=help_window.destroy)
help_window_button.pack(side=BOTTOM)

#-----------------------------------#
#Définition du caneva
#-----------------------------------#
canva = Canvas(root,width=1920,height=1080,bg="ivory")
canva.pack()

#-----------------------------------#
#Fonctions permettant le changement de séléction
#-----------------------------------#
def setRouter():
    sel.etat = "Router"
    
def setClient():
    sel.etat = "Client"
    
def setSwitch():
    sel.etat = "Switch"
    
def setDefault():
    sel.etat = "Selection"
    
#-----------------------------------#
#Définition de l'objet sélécteur
#-----------------------------------#
class Selector():
    def __init__(self) -> None:
        self.etat = "Selection"

#-----------------------------------#
#Différentes listes qui répertories les objets placés
#-----------------------------------#
routerList = []
clientList = []
switchList = []

#-----------------------------------------------------------------#
#Définition des objets
#-----------------------------------------------------------------#

#-----------------------------------#
#Définition de la superclasse Elements
#-----------------------------------#
class Elements():
    def __init__(self) -> None:
        #Menu d'édition (Clique droit)
        self.edit_menu = Menu(root)
        self.edit_menu.add_command(label="Rename",command=self.rename_menu)
        self.edit_menu.add_command(label="Delete",command=self.remove)
        self.edit_menu.add_command(label="Icon",command=self.icon_menu)
    
    #Fonction qui place les éléments sur le schéma
    def place(self,x,y):
        self.placeimg = canva.create_image(x,y,image=self.image,anchor=CENTER)
        self.name = canva.create_text(x,y+60,text=self.displayname)
        canva.tag_bind(self.placeimg,"<Button-3>",self.edit)
        canva.tag_bind(self.placeimg,"<B1-Motion>",self.move)
    
    #Menu permettant de renommer l'élément
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
    
    #Menu permettant de gérer l'icone
    def icon_menu(self):
        self.icon_window = Toplevel(root)
        self.icon_window.title("Icon Informations")
        self.icon_window.geometry("200x200")
        self.icon_window.resizable(False,False)
        self.canvaicon = Canvas(self.icon_window,width=100,height=100)
        self.canvaicon.pack(side=TOP)
        self.canvaicon.create_image(0,0,image=self.image,anchor=NW)
        self.upload_button = Button(self.icon_window,text="Modify Image",command=self.set_icon)
        self.upload_button.place(x=45,y=100)
    
    #Fonction affichant le menu d'édition    
    def edit(self,e):
        try:
            #Bind la popup du menu clique droit
            self.edit_menu.tk_popup(e.x_root,e.y_root)
        finally:
            #Revient à la normal après l'utilisation
            self.edit_menu.grab_release()

    #Fonction permettant de renommer l'élément placé
    def rename(self):
        self.new_name = self.rename_entry.get()
        canva.itemconfig(self.name,text=self.new_name)
        self.rename_window.destroy()
    
    #Fonction permettant de supprimer l'élément placé
    def remove(self):
        canva.delete(self.placeimg)
        canva.delete(self.name)
    
    #Fonction permettant de redéfinir un nouvel icône à l'élément placé
    def set_icon(self):
        self.image_type = [('Png Files', '*.png'),('Jpg Files', '*jpg')] #Type d'extension pour l'icône
        self.filename= filedialog.askopenfilename(filetypes=self.image_type) #On ouvre une fenêtre permettant à l'utilisateur de choisir une image sur son PC
        self.image = ImageTk.PhotoImage((Image.open(self.filename)).resize((100,100)))
        canva.itemconfig(self.placeimg,image=self.image)
        self.icon_window.destroy()
    
    #Fonction permettant le déplacement de l'élément    
    def move(self,e):
        if sel.etat != "Selection":
            return
        canva.coords(self.placeimg,e.x,e.y)
        canva.coords(self.name,e.x,e.y+60)
        
#-----------------------------------#
#Définition de la classe Router (héritant de la superclasse)
#-----------------------------------#    
class Router(Elements):
    def __init__(self) -> None:
        super().__init__()
        self.image = ImageTk.PhotoImage((Image.open("assets/router.png")).resize((100,100)))
        self.type = "router"
        self.id = len(routerList)
        self.displayname = f'router{self.id}'
            
    def place(self,x,y):
        super().place(x,y)
        routerList.append(self.displayname)
        self.index = routerList.index(self.displayname)
        
    def rename(self):
        super().rename()
        routerList[self.index] = self.new_name
    
    def remove(self):
        super().remove()
        routerList.remove(self.displayname)
#-----------------------------------#
#Définition de la classe Client (héritant de la superclasse)
#-----------------------------------#          
class Client(Elements):
    def __init__(self) -> None:
        super().__init__()
        self.image = ImageTk.PhotoImage((Image.open("assets/client.png")).resize((100,100)))
        self.id = len(clientList)
        self.displayname=f'client{self.id}'
        
    def place(self,x,y):
        super().place(x,y)
        clientList.append(self.displayname)
        self.index = clientList.index(self.displayname)
    
    def rename(self):
        super().rename()
        clientList[self.index] = self.new_name
    
    def remove(self):
        super().remove()
        clientList.remove(self.displayname)
 
#-----------------------------------#
#Définition de la classe Switch (héritant de la superclasse)
#-----------------------------------#               
class Switch(Elements):
    def __init__(self) -> None:
        super().__init__()
        self.image = ImageTk.PhotoImage((Image.open("assets/switch.png")).resize((100,100)))
        self.id = len(switchList)
        self.displayname=f'switch{self.id}'   
        
    def place(self,x,y):
        super().place(x,y)
        switchList.append(self.displayname)
        self.index= switchList.index(self.displayname)
        
    def rename(self):
        super().rename()
        switchList[self.index] = self.new_name
    
    def remove(self):
        super().remove()
        switchList.remove(self.displayname)
         
        
#-----------------------------------#
#On instancie le selecteur
#-----------------------------------#    
sel = Selector()

#-----------------------------------#
#Fonction plaçant les éléments en fonction de l'état du selecteur
#-----------------------------------#    
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
    
#-----------------------------------#
#Fonction permettant le changement de selecteur avec le clavier
#-----------------------------------#    
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
    
#-----------------------------------#
#Définition du Menu (toolbar)
#-----------------------------------#    
toolbar = Menu(root)
root.config(menu=toolbar)
add_menu = Menu(toolbar)
add_menu.add_command(label="Selection",command=setDefault)
add_menu.add_command(label="Router",command=setRouter)
add_menu.add_command(label="Client",command=setClient)
add_menu.add_command(label="Switch",command=setSwitch)
toolbar.add_cascade(label="Add",menu=add_menu)

#-----------------------------------#
#Gestion des Callbacks
#-----------------------------------#    
root.bind("<ButtonPress-1>",placeElmt)
root.bind("<KeyPress>",changeSelector)
root.mainloop()