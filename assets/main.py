from tkinter import *
from PIL import Image,ImageTk





routerSelected = False
switchSelected = False
clientSelected = False

def desactivateAll():
    global routerSelected
    global switchSelected
    global clientSelected
    routerSelected = False
    switchSelected = False
    clientSelected = False

#Change la valeur d'un booleen en fonction de sa valeur actuelle si Faux -> Vrai, si Vrai -> Faux
def activate(bool):
    desactivateAll()
    if bool != True:
        bool = True
    else:
        bool = False
    return bool

def elmtEvent(event,place):
    if event == True:
        canva.bind("<ButtonRelease-1>",place)
    else:
        canva.unbind("<ButtonRelease-1>")
    
#Gestion des Elements
def selectRouter():
    global routerSelected
    routerSelected = activate(routerSelected)
    elmtEvent(routerSelected,placeRouter)

def placeRouter(e):
    if(routerSelected == True):
        canva.create_image(e.x,e.y,image=router,anchor=CENTER)
    
def selectClient():
    global clientSelected
    clientSelected = activate(clientSelected)
    elmtEvent(clientSelected,placeClient)
    
def placeClient(e):
    if(clientSelected == True):
        canva.create_image(e.x,e.y,image=client,anchor=CENTER)
    
def selectSwitch():
    global switchSelected
    switchSelected = activate(switchSelected)
    elmtEvent(switchSelected,placeSwitch)
    
def placeSwitch(e):
    if(switchSelected == True):
        canva.create_image(e.x,e.y,image=switch,anchor=CENTER)    

    

root = Tk()
root.geometry("1280x720")


#Gestion du Menu
toolbar = Menu(root)
root.config(menu=toolbar)

add_menu = Menu(toolbar)
add_menu.add_command(label="Router",command=selectRouter)
add_menu.add_command(label="Client",command=selectClient)
add_menu.add_command(label="Switch",command=selectSwitch)
toolbar.add_cascade(label="Ajouter",menu=add_menu)


#Gestion du Canva
canva = Canvas(root,width=1280,height=720,bg="ivory")
canva.pack()

#Importation des images
router_img = (Image.open("assets/router.png"))
resize_router = router_img.resize((100,100), Image.LANCZOS)
router= ImageTk.PhotoImage(resize_router)

client_img = (Image.open("assets/client.png"))
resize_client = client_img.resize((100,100),Image.LANCZOS)
client= ImageTk.PhotoImage(resize_client)

switch_img = (Image.open("assets/switch.png"))
resize_switch = switch_img.resize((100,100),Image.LANCZOS)
switch= ImageTk.PhotoImage(resize_switch)




root.mainloop()