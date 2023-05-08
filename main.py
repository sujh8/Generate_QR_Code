from re import L
from tkinter import * 
import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import qrcode
import time
from tkinter import messagebox
import subprocess
import customtkinter
import io
import pyautogui
import os
from PIL import Image, ImageTk


root = Tk()
root.title('Empolyee QR code')
root.geometry('370x470+500+100')
root.resizable(False,False)
im = Image.open('profile.png')
photo = ImageTk.PhotoImage(im)
root.wm_iconphoto(True, photo)


def welcome():
    music=AudioSegment.from_mp3('sounds/Welcome.mp3')
    play(music)

wel = pyttsx3.init()
voices = wel.getProperty('voices')
wel.setProperty('voice',voices[1].id)

def Speak(audio):
    wel.say(audio)
    wel.runAndWait()

def TakeCommands():
    command= sr.Recognizer()
    with sr.Microphone() as mic:
        command.phrase_threshold= 0.1
        audio = command.listen(mic)
        query = "Not recognized"
        try:
            query = command.recognize_google(audio, language='en-us')
        except Exception as Error:
            print(Error)
        return query.lower()  # type: ignore

def b1():
    query = TakeCommands()
    name = query
    E1.insert(0,name)
def b2():
    query = TakeCommands()
    name = query
    E2.insert(0,name)
def b3():
    query = TakeCommands()
    name = query
    E3.insert(0,name)
def Sv():
    namefile = En_save.get()
    name = E1.get()
    co   = E2.get()
    job  = E3.get()
    info = qrcode.make(name + co + job)
    info.save('employee/'+namefile+'.jpg')
    messagebox.showinfo('Save','Save [' +namefile+ '] employee')

#logo 
photo =PhotoImage(file='EMPLOYEE.png')
l_img = Label(root,image=photo)
l_img.place(x=1,y=1,width=365,height=270)
#form
#text_emp
l=Label(root,text="Full_Name" , font=('Arial',12))
l.place(x=10,y=280)
#country
l1 = Label(root, text='Country',font=('Arial',12))
l1.place(x=10,y=310)
#job 
l2 = Label(root, text='Job',font=('Arial',12))
l2.place(x=10,y=340)
#button_frame
E1 = Entry(root,font=('Arial',12))
E1.place(x=130,y=280)
#button_frame
E2 = Entry(root,font=('Arial',12))
E2.place(x=130,y=310)
#button_frame
E3 = Entry(root,font=('Arial',12))
E3.place(x=130,y=340)
#button1
b1=Button(root,text='🎶',bg='black',fg='white',font=('Arial',9),command=b1) # type: ignore
b1.place(x=340,y=280)
#button2
b2=Button(root,text='🎶',bg='black',fg='white',font=('Arial',9),command=b2) # type: ignore
b2.place(x=340,y=310)
#button3
b3=Button(root,text='🎶',bg='black',fg='white',font=('Arial',9),command=b3) # type: ignore
b3.place(x=340,y=340)


#save_and_exit_frame 
#save_button_text
l_save = Label(root, text='file Save',font=('Arial',12),highlightcolor='yellow') 
l_save.place(x=10,y=390)
#button_frame
En_save= Entry(root,font=('Arial',16),width=11)
En_save.place(x=137,y=390)
#button
b_save=Button(root,text='Register',fg='white',bg='black',font=('Arial',10,'bold'),command=Sv,padx=3,pady=1)
b_save.place(x=220,y=425)
#exit
exitButton=Button(root,text="Exit program",command=root.destroy,  
padx=3,pady=1) 
exitButton.configure(background='black', foreground='white',font=('arial',10,'bold'))
exitButton.place(x=100,y=425 )

#l_copy =Label(root,text='suha ',font=('Tajawal',14))
#l_copy.place(x=130,y=435)


#welcome()
root.mainloop()









