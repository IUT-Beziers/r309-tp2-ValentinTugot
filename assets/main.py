from tkinter import *
from PIL import Image,ImageTk


root = Tk()
root.geometry("1280x720")

canva = Canvas(root,width=1280,height=720,bg="ivory")
canva.pack()

#Importation des images
router_img = (Image.open("assets/router.png"))
resize_router = router_img.resize((100,100), Image.ANTIALIAS)
router= ImageTk.PhotoImage(resize_router)

client_img = (Image.open("assets/client.png"))
resize_client = client_img.resize((100,100),Image.ANTIALIAS)
client= ImageTk.PhotoImage(resize_client)

switch_img = (Image.open("assets/switch.png"))
resize_switch = switch_img.resize((100,100),Image.ANTIALIAS)
switch= ImageTk.PhotoImage(resize_switch)

canva.create_image(50,50,image=router,anchor=NW)


root.mainloop()