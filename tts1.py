#importing modules (download using pip install)
from tkinter import *
from gtts import gTTS
from playsound import playsound

#Initializing window
root=Tk() #Initialized tkinter to use as GUI
root.geometry("350x300") #setting width and height of the window
root.resizable(0,0)
root.configure(bg='ghost white') #to access the attributes in my window
root.title("Text-To-Speech")
 
#Giving heading
Label(root,text="Text To Speech",font="calibri 20 bold", bg='white smoke').pack()
Label(text="Aryan Kochhar",font="calibri 16 bold",bg='white smoke').pack(side='bottom')

#root is name of window
#pack is widget in the block
#msg is string type variable
#text variable is used to retrieve the current text to entry widget
#place puts widgets in specific x,y coords in parent widget

Label(root,text="                 Enter the Text",font="calibri 16 bold",bg='white smoke').place(x=20,y=60)

#text variable 
Msg=StringVar()


#Entry
entry_field=Entry(root,textvariable=Msg,width='50')
entry_field.place(x=20,y=100)

#Creating a function to convert Text to Speech
def Text_to_speech():
    Message=entry_field.get()
    speech=gTTS(text=Message)
    speech.save("Speech.mp3")
    playsound("Speech.mp3")

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Defining button
Button(root,text="PLAY",font='calibri 15 bold',command=Text_to_speech,bg='cyan',width=4).place(x=25,y=140)
Button(root,text="EXIT",font='calibri 15 bold',command=Exit,bg='OrangeRed1').place(x=100,y=140)
Button(root,text="RESET",font='calibri 15 bold',command=Reset,bg='pink',width=6).place(x=175,y=140)

#Infinite loop to run the program

root.mainloop()

