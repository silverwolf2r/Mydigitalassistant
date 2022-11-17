#digital assistant


import os
from os import system, name
import speech_recognition as sr
import win32com.client as wincl
import subprocess
import winapps
import wolframalpha
import winsound


def clear():
	system('cls')

def listen():
    ad = None
    frequency = 2500  # Set Frequency To 2500 Hertz

    duration = 100  # Set Duration To 1000 ms == 1 second

    while ad == None:
        try:
            # obtain audio from the microphone
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening")
                winsound.Beep(frequency, duration)
                audio = r.listen(source)
            
            #recognize audio and assign it to a variable   
            x = (r.recognize_google(audio))
            text = str(r.recognize_google(audio))
            print("You said " + text)
            return text
        except:
            ad = None

def speak(text):
    #speak the text
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)

def commandlist():
    print("""
    Command List:
    Shutdown - Shutdown the computer
    Sleep - Puts the computer to sleep
    Tell me - Will tell information about certain subjects
    Open file - Will open browsers and if you say a non browser will open folder location
    Word Game - Starts the Shiritori word game
    Book - Opens the book script for you to download a book
    Website - Opens whatever link you say next
    Exit -  Exits the script
    """)

while(1):
    commandlist()
    Curse = listen()
    clear()

    if str(Curse) == "shutdown":
        speak("Gooodbye, and Goodnight")
        os.system("shutdown /s")
        quit()
    if str(Curse) == "sleep":
        speak("Retire to the void Sweet Prince")
        os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")
        quit()
    if str(Curse) == "tell me":
        speak("ok")
        Curse = listen()
        appid = "3J84PX-AEPPPVHK73"
        client = wolframalpha.Client(appid)
        res = client.query(Curse)
        answer = next(res.results).text
        print(answer)
        speak(answer)
    if str(Curse) == "open file":
        speak("What file would you like to search for?")
        Curse = listen()
        try:
            for item in winapps.search_installed(Curse):
                insloc = item.install_location
                program = str(Curse).lower()
                pn = "\\" + str(program) + ".exe"
                query = ('"' + str(insloc) + pn + '"')
                print (query)
                os.system(query)
        except:
            local_path = r"C:\Users\tok6b"
            subprocess.Popen(f'explorer /root,"search-ms:query={Curse}&crumb=folder:{local_path}&"')
            quit()
    if str(Curse) == "word game":
        speak("Shiritori")
        os.startfile("C:/Users/tok6b/Desktop/python_scripts/Shiritori.py")
        quit()
    if str(Curse) == "book":
        speak("Opening Book Script")
        os.startfile("C:/Users/tok6b/Desktop/python_scripts/book.py")
        quit()
    if str(Curse) == "website":
        Curse = listen()
        Curse = Curse.replace(" ", "")
        query = "start http://" + str(Curse)
        os.system(query)
    if str(Curse) == "exit":
        quit()

