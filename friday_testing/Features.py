import sys
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os
import requests
from bs4 import BeautifulSoup
import webbrowser
from time import sleep

chrome_path = 'C:\Program Files\Google\Chrome\Application/chrome.exe %s'

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wiki(term):
    query = term.replace("friday", "")
    query = query.replace("wiki", "")
    speak('Searching Wikipedia...')
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    speak(results)


def whois(term):
    query = term.replace("friday", "")
    query = query.replace("who is", "")
    speak('Searching Wikipedia...')
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    speak(results)


def playonyt(term):
    query = term.replace("friday", "")
    query = query.replace("play", "")
    speak("playing " + query + " on youtube music")
    pywhatkit.playonyt(query)


def time(term):
    strTime = datetime.datetime.now().strftime("%I:%m %p")
    speak(f"Sir, currently its {strTime}, have a good day!")


def easter01():
    speak("I am Friday, designed to work under guidence of Jarvis, but unfortunately, as Jarvis is no more with us I was assigned to handle the daily takes")
    speak("My name stands for, Female Replacement Intelligent Digital Assistant Youth")
    speak("My speciality is, i can better understand human emotions and work on it")


def location():
    speak("let me check sir,")
    speak("currently there's some issue in finding your exact location,")
    speak("but for reference, we are currently in Narhe area of Pune,Maharashtra")


def temperature(term):
    search = "temperature in pune"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"currently {search} is {temp} celcius")


def write(term):
    rememberMsg = term.replace("remember that", "")
    rememberMsg = rememberMsg.replace("friday", "")
    speak("you told me to remember that " + rememberMsg)
    speak("message remembered successfully")
    remember = open('remainders.txt', 'w')
    remember.write(rememberMsg)
    remember.close()


def read():
    with open('remainders.txt') as text:
        remember = text.read()
    speak("you told me that " + remember)


def searcher(term):
    query = term.replace("search", "")
    query = query.replace("open", "")
    query = query.replace("%20", "")
    query = query.replace("friday", "")
    speak(f"opening {query}")
    web2 = 'https://www.' + query + '.com/'
    webbrowser.get(chrome_path).open(web2)


def youtubeSearch(term):
    query = term.replace("youtube search", "")
    query = query.replace("friday", "")
    query = query.replace("search on youtube", "")
    webbrowser.get(chrome_path).open("https://www.youtube.com/results?search_query=" + query)


def googleSearch(term):
    query = term.replace("google search", "")
    query = query.replace("friday", "")
    pywhatkit.search(query)


def youtube():
    webbrowser.get(chrome_path).open("https://youtube.com/")


def google():
    webbrowser.get(chrome_path).open("https://google.com/")


def discord():
    webbrowser.get(chrome_path).open("https://discord.com/")


def moodle():
    webbrowser.get(chrome_path).open("https://lmspoly.tssm.edu.in/")


def breaker():
    speak('you are welcome sir, always at your command')


