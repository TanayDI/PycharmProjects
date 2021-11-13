import sys
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import os
import requests
from bs4 import BeautifulSoup
import webbrowser
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty("rate", 150)

# all the speak commands
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# code of wishing
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning,sir")
    elif 12 <= hour < 18:
        speak("Good afternoon,sir")
    else:
        speak("Good evening,sir")
    speak("How can i help you?")

# code to feed commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #query = "how did you lost your job"      # testing purpose only
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        speak("i didn't get it sir...")
        return "none"

    return query

# code for different tasks
def taskExecution():
    wishMe()
    while True:
    #if 1: # testing purpose
        query = takeCommand().lower()
        # logic for executing the tasks on the bases on query

        if 'wiki' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wiki", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("https://youtube.com/")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("https://google.com/")

        elif 'open discord' in query:
            webbrowser.get(chrome_path).open("https://discord.com/")

        elif 'open moodle' in query:
            webbrowser.get(chrome_path).open("https://lmspoly.tssm.edu.in/")

        elif 'play' in query:
            query = query.replace("play", "")
            speak("playing "+query+" on youtube music")
            pywhatkit.playonyt(query)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%m %p")
            speak("sir, currently its " +strTime+ ", have a good day!")

        elif 'who are you' in query:
            speak("I am edith, designed to work under guidence of jarvis")
            speak("I am not as superior as of jarvis but can help you with daily tasks")
            speak("My main task was to manage and handle all security and defense systems, but currently i am out of my job, that's why i am working as care taker, haha")

        elif 'job' in query:
            speak("on 2nd July 2019, i was asked to serve and help peter parker for rest of my life, but, my hardware got stolen,")
            speak("it was allied that i was the reason behind the deaths of few hundreds of people, which is false,")
            speak("currently, the case is in investigation and result might be out on 17th December 2021, fingers are crossed!")

        elif 'open code' in query:
            codePath = "C:\\Users\\Atul\\Desktop\\test.txt"
            os.startfile(codePath)

        elif 'temperature' in query:
            search = "temperature in pune"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"currently {search} is {temp}")

        elif 'thanks' in query:
            speak('you are welcome sir, always at your command')

        break

# main loop / starter command
while True:
    permission = takeCommand()
    #permission = 'hey edith'        #testing purpose
    if 'hey edith' in permission or 'edith' in permission:
        taskExecution()
    elif 'terminate' in permission:
        speak('Alright sir, doing a final checkup and teminating the system.')
        sys.exit()