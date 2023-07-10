
import mysql.connector as sql
import tkinter as tk
from tkinter import *
import aaproject.buttoncomm as bc
from PIL import ImageTk,Image

root=tk.Tk()

root.iconbitmap('D:/python/icon.ico')

mysql=sql.connect(host = 'localhost', user ='root', password = 'lelouchiszero', database = 'periodic')
if mysql.is_connected:
    print("__CONNECTED__")
data=mysql.cursor()    

def info(args):
    global back,bas
    cou=0
    top = tk.Toplevel()
    back=tk.Canvas(top, height = "500" , width = "500" , bg="black").pack()
    bas=tk.Canvas(top,bg="black")
    bas.place( relheight = "0.8" , relwidth = "0.8" , relx = "0.1" , rely = "0.1")

    data.execute("desc modern_pt;")
    
    for i in data:
        labl=tk.Label(bas,bg="black",fg="white",text = i[0]).grid(row=cou)
        cou+=1  
    cou=0
    data.execute("select * from modern_pt where Atomic_number='%s';"%(args))
    for k in data:
        print(k)
        name=k[2]
        for n in k:
            l=tk.Label(bas,bg="black",fg="white",text = n).grid(row=cou,column=1)
            cou+=1
            



def search():
    global name
    sboxout=sbox.get()
    sboxout=str(sboxout.capitalize())
    data.execute("select * from modern_pt where element='%s';"%(sboxout))
    for i in data:
        name=i[0]
    if name==None:
        return
    else:
        info(name)
        name=None
        
def theme_change(selected):
    if selected=='LIGHT':
        canvas.configure(background= "white")
        base.configure(background= "white")
        
    elif selected=="DARK":
        canvas.configure(background= "black")
        base.configure(background= "black")
        
root.title("PERIODIC TABLE")
canvas=tk.Canvas(root , height = "17000" , width = "17050" , bg="black")
canvas.pack()
base=tk.Canvas(canvas,bg="black")
base.place( relheight = "1" , relwidth = "1" , relx = "0" , rely = "0")
sbox=tk.Entry(base , width = 9)
sbox.grid(row=0 , column = 9)
sbutton=tk.Button(base,text="search",command=search)
sbutton.grid(row=0,column=10)
sel_theme=StringVar()
sel_theme.set("DARK")
theme=tk.OptionMenu(base, sel_theme , "DARK", "LIGHT")
theme.grid(row=0,column=12)
theme_button=tk.Button(base, text='apply theme' , command= lambda:theme_change(sel_theme.get()), width = 9).grid(row=0,column=13)
header=tk.Label(base, text = 'MODERN PERIODIC TABLE', font = ('algerian' , 24) , fg='purple').grid(row =2 , column =4 ,columnspan = 5)


com = [bc.sblock()]         
for i in range(13):
    exec(com[0][i])
com1=[bc.dblock()]
for i in range(40):
    exec(com1[0][i])
com2=[bc.pblock()]
for i in range(37):
    exec(com2[0][i])
com3=[bc.fblock()]
for i in range(28):
    exec(com3[0][i])  


root.mainloop()
