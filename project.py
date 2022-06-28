from tkinter import *

import speech_recognition as sr
import pyttsx3

e=pyttsx3.init()

mainwindow= Tk()
mainwindow.title(' Text-To-Speech and Speech-To-Text Converter')
mainwindow.geometry('500x500')
mainwindow.configure(bg='light yellow')



def listen_and_recognise():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as s:
            r.adjust_for_ambient_noise(s, duration=0.2)
            a=r.listen(s)
            try:
                text = r.recognize_google(a,language="en-IN")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service")
        return text
def speak(message):
    voices = e.getProperty('voices')
    e.setProperty('voice', voices[1].id)
    e.say(message)
    e.setProperty("rate", 150)
    e.runAndWait()

def listen_recognise_and_speak():
    text1=listen_and_recognise()
    speak(text1)
    return text1



def from_text_to_Speech():
    texttospeechwindow = Toplevel(mainwindow)
    texttospeechwindow.title('Text-to-Speech Converter ')
    texttospeechwindow.geometry("500x500")
    texttospeechwindow.configure(bg='snow2')

    Label(texttospeechwindow, text='Text-to-Speech Converter ', font=("Comic Sans MS", 18), bg='beige').place(x=90 , y=10)

    text = Text(texttospeechwindow, height=10, width=50, font=12)
    text.place(x=22, y=60)

    speakbutton = Button(texttospeechwindow, text='Listen', bg='coral', command=lambda: speak(str(text.get(1.0, END))))
    speakbutton.place(x=200, y=250)

    clearbutton = Button(texttospeechwindow, text='Clear', bg='coral', command=lambda: str(text.delete("1.0","end")))
    clearbutton.place(x=250, y=250)

def from_speech_to_text():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-to-Text Converter ')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='pink')

    Label(speechtotextwindow, text='Speech-to-Text Converter ', font=("Comic Sans MS", 18), bg='Lavender').place(x=90 , y=10)

    text = Text(speechtotextwindow, font=12, height=10, width=50)
    text.place(x=22, y=100)

    recordbutton = Button(speechtotextwindow, text='Record', bg='coral', command=lambda: text.insert(END, listen_and_recognise()))
    recordbutton.place(x=200, y=60)

    clearbutton = Button(speechtotextwindow, text='Clear', bg='coral', command=lambda: text.delete("1.0","end"))
    clearbutton.place(x=260, y=60)



def both():
    speechtotextandTextTOSpeechwindow = Toplevel(mainwindow)
    speechtotextandTextTOSpeechwindow.title('Speech-to-Text and Text-to-Speech Converter ')
    speechtotextandTextTOSpeechwindow.geometry("500x500")
    speechtotextandTextTOSpeechwindow.configure(bg='khaki')

    Label(speechtotextandTextTOSpeechwindow, text='Speech-to-Text and Text-to-Speech Converter ', font=("Comic Sans MS", 16), bg='#9A7B4F').place(x=15 , y=10)

    text = Text(speechtotextandTextTOSpeechwindow, font=12, height=10, width=50 )
    text.place(x=22, y=100)

    recordbutton = Button(speechtotextandTextTOSpeechwindow, text='Record', bg='coral', command=lambda: text.insert(END, listen_recognise_and_speak()))
    recordbutton.place(x=200, y=60)
    clearbutton = Button(speechtotextandTextTOSpeechwindow, text='Clear', bg='coral', command=lambda: text.delete("1.0","end"))
    clearbutton.place(x=260, y=60)

Label(mainwindow, text=' Text-To-Speech and Speech-To-Text Converter',
     font=('Comic Sans MS', 20), bg='light salmon', wrap=True, wraplength=450).place(x=75, y=20)

texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion', font=('Times New Roman', 16), bg='light slate blue', command=from_text_to_Speech)
texttospeechbutton.place(x=120, y=250)

speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='light slate blue', command=from_speech_to_text)
speechtotextbutton.place(x=120, y=150)

speechtotextandTextTOSpeechbutton = Button(mainwindow, text='Speech-to-Text and Text-to-Speech Converter ', font=('Times New Roman', 16), bg='light slate blue', command=both)
speechtotextandTextTOSpeechbutton.place(x=50, y=350)

mainwindow.update()
mainwindow.mainloop()
