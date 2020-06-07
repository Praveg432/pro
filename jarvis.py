#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import webbrowser as wb
import speech_recognition as sr
from tkinter import *
from time import ctime
import time
import os
from gtts import gTTS
import playsound
from playsound import playsound


def speak(audioString):
    global x
    b = audioString
    if len(b)>0:
        tts=gTTS(text=b,lang='en-us')
        tts.save("voice%s.mp3"%(x))
        playsound("voice%s.mp3"%(x))
        x +=1


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("heard...")
    data = ""



    try:
        data = r.recognize_google(audio)
        print("You said : " + data )
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

def passcode():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("heard...")
    data = ""

    passList=["pineapple","orange","point break","black","Kedarnath","kedarnath"]

    try:
        data = r.recognize_google(audio)
        print(data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
    if data in passList:
        return 1
    else:
        return 0



def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    elif "open Facebook" in data:
        talking(5)
        wb.open("https://www.facebook.com")

    elif "open Notepad" in data:
        talking(5)
        os.system(notepad)

    elif "open Google" in data:
        talking(5)
        wb.open("https://www.google.com")

    elif "what time is it" in data:
        speak(ctime())

    elif "search" in data:
        query = data[7:]
        talking(6)
        wb.open_new_tab("https://google.com/search?q=%s" % query)

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        talking(6)
        wb.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")
    elif (data==""):
        talking(7)
    else :
        talking(6)
        wb.open_new_tab("https://google.com/search?q=%s" % data)


def talking(vo):
    if(vo==1):
        speak("Please speak the passcode:")
    elif(vo==2):
        speak("Turning off the program")
    elif(vo==3):
        speak("Hi! What can I do for you?")
    elif(vo==4):
        speak("Wrong Passcode! You cannot use the system.")
    elif(vo==5):
        speak("Sure! Here you go")
    elif(vo==6):
        speak("Fetching results")
    else:
        speak("Could not understand audio. Try again later.")



x=0
print("start..")
talking(1)
if(passcode()==1):
    talking(3)
    data = recordAudio()
    jarvis(data)
    talking(2)
    print("Run complete")
else:
    talking(4)
    talking(2)
    print("Run terminated")
