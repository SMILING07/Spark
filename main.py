from tkinter import *
from PIL  import ImageTk,Image 
import webbrowser as wb
import tkvideo.tkvideo
import wikipedia
import google.generativeai as genai
import pyttsx3
def microp():
    pass
def speak(response):
    engine.say(response)
    engine.runAndWait()
def run(e=None):
    global query ,response
    query=entry.get()
    entry.delete(0,100)
    response=commands(query)
    user_text=Text(frame1,font=('Ariel',12),wrap='word')
    user_text.insert('1.0',response)
    user_text.tag_config('justify',justify='left')
    user_text.tag_add('justify','1.0','end')
    user_text.place(relheight=0.999,relwidth=0.9998,relx=0.0001,rely=0.0001)
    user_text.config(state='disabled',background=fgc,foreground=bgc)

def soscall():
    wb.open("tel:112")
def commands(query):
    global wq ,response
    query=query.lower()
    wq=False
    if 'sos' in query:
        wb.open("tel:112")
    elif 'call' in query:
        wb.open("tel:"+query.replace('call'))
    elif 'search' in query:
        wb.open(f"https:////www.google.com//search?q={query}")
    else:
        try:
            model=genai.GenerativeModel('gemini-pro')
            API_KEY="AIzaSyBKXEp7mLNglX-R02pZjLR_4j1lc7HV9HM"
            genai.configure(api_key=API_KEY)
            response=model.generate_content("conider you are spark and my personal mental health companion please answer the following query\n"+query)
            return response.text.replace("*", '')
        except:
            response=wikipedia.summary(query)
            return 'Acoording to wikipedia\n'+response
def appfunc():
    global root,frame,frame1,frame2,text,player,label,entry,send,bgc,fgc,user_text
    root           = Tk()
    animate_start()
    frame          = Frame(root,bg=bgc)
    frame1         = Frame(frame)
    frame2         = Frame(root,bg=fgc)
    frame4         = Frame(root,bg=fgc)
    label          = Label(frame,bg=fgc)
    mic            = ImageTk.PhotoImage((Image.open('Pictures\\mic.png')).resize((20,20),Image.FILTERED))
    player         = tkvideo.tkvideo("Animations//#4.mp4", label, loop = 1, size = (400,250))
    entry          = Entry(frame2,bg=fgc,fg=bgc,font=('Ariel',15),bd=0,highlightthickness=0)
    text           = Text(frame1,font=('impact',17),wrap='word')
    user_text      = Text(frame4,font=('impact',17),wrap='word')
    send           = ImageTk.PhotoImage((Image.open('Pictures\\send.png')).resize((20,20),Image.FILTERED))
    sos            = ImageTk.PhotoImage((Image.open('Pictures\\sos.png')).resize((20,20),Image.FILTERED))
    send_button    = Button(frame2,bg=fgc,bd=0,highlightthickness=0,image=send,command=run)
    mic_button     = Button(frame2,bg=fgc,bd=0,highlightthickness=0,image=mic,command=microp)
    sos_button     = Button(frame2,bg=fgc,bd=0,highlightthickness=0,image=sos,command=soscall)
    #ROOT WINDOW
    root.geometry("300x600")
    root.title('SPARK')
    root.attributes('-topmost', True)
    root.iconphoto(False,PhotoImage(file='Pictures//icon.png'))
    entry.bind("<Return>",run)
    #FRAMES
    frame.place(relx=0.001,rely=0.001,relwidth=0.998,relheight=0.998)
    frame1.place(relheight=0.61,relwidth=0.98,relx=0.01,rely=0.31)
    frame2.place(relheight=0.07,relwidth=0.98,relx=0.01,rely=0.924)
    #TEXT BOX
    text.insert('1.0','Hello there,\nHow can I assist you today')
    text.tag_config('justify',justify='center')
    text.tag_add('justify','1.0','end')
    text.place(relheight=0.999,relwidth=0.9998,relx=0.0001,rely=0.0001)
    text.config(state='disabled',background=fgc,foreground=bgc)
    user_text.insert('1.0','')
    user_text.tag_config('justify',justify='center')
    user_text.tag_add('justify','1.0','end')
    user_text.place(relheight=0.999,relwidth=0.9998,relx=0.0001,rely=0.0001)
    user_text.config(state='disabled',background=fgc,foreground=bgc)
    #LABEL
    label.place(relheight=0.3,relwidth=0.98,relx=0.01,rely=0.005)
    player.play()
    #ENTRY
    entry.place(relheight=0.999,relwidth=0.65,relx=0.0001,rely=0.0001)
    #BUTTON
    send_button.place(relx=0.858,relheight=0.999,relwidth=0.1,rely=0.0001)

    sos_button.place(relx=0.758,relheight=0.999,relwidth=0.1,rely=0.0001)
    speaker        = ImageTk.PhotoImage((Image.open('Pictures\\speak.png')).resize((20,20),Image.FILTERED))
    speaker_button = Button(frame1,bg=fgc,bd=0,highlightthickness=0,image=speaker)
    speaker_button.place(relheight=0.08,relwidth=0.1,relx=0.87,rely=0.9)
    mic_button.place(relx=0.658,relheight=0.999,relwidth=0.1,rely=0.0001)
    root.mainloop()

#SPEAK ENGINE

rate   =150
voice  =1
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[voice].id)
engine.setProperty('rate',rate)

#variables
query      = None
entry       = None
bgc         ='black'
fgc         ='white'
response=None
if __name__=="__main__":
    appfunc()
