import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os
import random
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am noob, please tell me how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = input() #r.listen(source)
    try:
        print("Recognizing...")
        query= audio    #r.recognize_google(audio,language='en-in')
        #print(f"you said:{query}\n")
    except Exception as e:
        #print(e)
        print("say again please...")
        return "None"
    speak (query)
    return query
def sendEmail(From,Pass,t,c):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(From,Pass)
    server.sendmail(From,t,c)
    server.close()
if __name__=="__main__":
    wishMe()
    while True:
        query =takeCommand().lower()
        if 'wikipedia' in query:
            print("seaching wikipedia...")
            speak("please wait searching wikipedia...")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query , sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("loading...")
            speak("please wait for opening")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("opening...")
            speak("opening")
            webbrowser.open("google.com")

        elif 'play music' in query:
            speak("please wait...")
            print("opening...")
            dir='C:\\Users\\rahul\\Music\\songs\\English_songs'
            songs=os.listdir(dir)
            n = len(songs)
            os.startfile(os.path.join(dir , songs[random.randint(0,n-1)]))

        elif 'send mail' in query:
            speak('enter your mail')
            print('enter your mail id')
            From=input()
            speak('enter password')
            print("enter password")
            Pass=input()
            speak('enter mail id of user')
            print('to:')
            t=input()
            print('what should i say')
            c=takeCommand()
            sendEmail(From,Pass,t,c)
            print('successfully sent...')
            speak('email has been sent')
