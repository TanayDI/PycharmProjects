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

chrome_path = 'C:\Program Files\Google\Chrome\Application/chrome.exe %s'

# ------------ Engine Creator --------------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices) #voice properties
engine.setProperty('voice', voices[2].id)
engine.setProperty("rate", 145)


# ---------- System Functions ----------------------

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

    strTime = datetime.datetime.now().strftime("%I:%m %p")
    speak("currently its " + strTime)
    speak("i am edith, online and ready")
    speak("How can i help you?")


# code for initiate sequence
def initiate():
    speak("initiating sequence...")
    speak("Starting all system applications,")
    speak("installing and checking all drivers,")
    speak("calibrating and examining all the core processors,")
    speak("Checking internet connection,")
    speak("wait a movement sir,")
    speak("all drivers are up and running, System initiated successfully!,")
    speak("now i am online")


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
        #query = "whats the time"  # testing purpose only
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        speak("i didn't get it sir...")
        return "none"

    return query

# ---------------task-Functions--------------------------

def wiki():
    query = takeCommand().lower()
    speak('Searching Wikipedia...')
    query = query.replace("wiki", "")
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    speak(results)


def whois():
    query = takeCommand().lower()
    speak('Searching Wikipedia...')
    query = query.replace("who is", "")
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    speak(results)


def playonyt():
    query = takeCommand().lower()
    query = query.replace("play", "")
    speak("playing " + query + " on youtube music")
    pywhatkit.playonyt(query)


def time():
    query = takeCommand().lower()
    strTime = datetime.datetime.now().strftime("%I:%m %p")
    speak("sir, currently its " + strTime + ", have a good day!")


def easter01():
    speak("I am edith, designed to work under guidence of jarvis")
    speak("I am not as superior as of jarvis but can help you with daily tasks")
    speak(
        "My main task was to manage and handle all security and defense systems, but currently i am out of my job, that's why i am working as care taker, haha")


def easter02():
    speak(
        "on 2nd July 2019, i was asked to serve and help peter parker for rest of my life, but, my hardware got stolen,")
    speak("it was allied that i was the reason behind the deaths of few hundreds of people, which is false,")
    speak("currently, the case is in investigation and result might be out on 17th December 2021, fingers are crossed!")


def location():
    speak("let me check sir,")
    speak("  ,  ,  ,  ,  ,  ,  ,")
    speak("currently there's some issue in finding your exact location,")
    speak("but for reference, we are currently in Narhe area of Pune,Maharashtra")


def temperature():
    search = "temperature in pune"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"currently {search} is {temp} celcius")


def write():
    query = takeCommand().lower()
    rememberMsg = query.replace("remember that", "")
    rememberMsg = rememberMsg.replace("edith", "")
    speak("you told me to remember that " + rememberMsg)
    speak("message remembered successfully")
    remember = open('remainders.txt', 'w')
    remember.write(rememberMsg)
    remember.close()


def read():
    with open('remainders.txt') as text:
        remember = text.read()
    speak("you told me that " + remember)


def searcher():
    query = takeCommand().lower()
    query = query.replace("search", "")
    query = query.replace("open", "")
    query = query.replace("%20", "")
    speak(f"opening {query}")
    web2 = 'https://www.' + query + '.com/'
    webbrowser.get(chrome_path).open(web2)


def youtubeSearch():
    query = takeCommand().lower()
    query = query.replace("youtube search", "")
    query = query.replace("friday", "")
    webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query=" + query)
    speak("this is what i found on the web")


def googleSearch():
    query = takeCommand().lower()
    query = query.replace("google search", "")
    query = query.replace("edith", "")
    pywhatkit.search(query)
    speak("this is what i found on the web")


# -------------------code for different tasks---------------------------


def taskExecution():
    while True:
    #if 1:  # testing purpose
        query = takeCommand().lower()
        # logic for executing the tasks on the bases on query

        if 'wiki' in query:
            wiki()

        elif 'who is' in query:
            whois()

        elif 'start youtube' in query:
            webbrowser.get(chrome_path).open("https://youtube.com/")

        elif 'start google' in query:
            webbrowser.get(chrome_path).open("https://google.com/")

        elif 'start discord' in query:
            webbrowser.get(chrome_path).open("https://discord.com/")

        elif 'start moodle' in query:
            webbrowser.get(chrome_path).open("https://lmspoly.tssm.edu.in/")

        elif 'open' in query:
            searcher()

        elif 'youtube search' in query:
            youtubeSearch()

        elif 'google search' in query:
            googleSearch()

        elif 'play' in query:
            playonyt()

        elif 'time' in query:
            time()

        elif 'who are you' in query:
            easter01()

        elif 'job' in query:
            easter02()

        elif 'location' in query:
            location()

        elif 'open notepad' in query:
            codepath = "C:\\Users\\Atul\\Desktop\\test.txt"
            os.startfile(codepath)

        elif 'remember that' in query:
            write()

        elif 'what do you remember' in query:
            read()

        elif 'temperature' in query:
            temperature()

        elif 'thanks' in query:
            speak('you are welcome sir, always at your command')
        break


# main loop / starter command
while True:
#if 1:
    permission = takeCommand().lower()
    #permission = 'friday'  # testing purpose
    if 'hey friday' in permission or 'friday' in permission:
        #initiate()
        #wishMe()
        taskExecution()
    elif 'terminate' in permission:
        speak('Alright, doing a final checkup and teminating the system.')
        speak("goodbye sir, call me by my name and i will be at your command")
        sys.exit()
