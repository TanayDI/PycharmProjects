import pyttsx3
import speech_recognition as sr
import wikipedia
import sys
import webbrowser
from Features import wiki, whois, playonyt, time, easter01, location, temperature, write, read, searcher, youtubeSearch, googleSearch, youtube, google, discord, moodle, breaker
from friday import initiate, wishMe


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language='en-in')
            print(f"you Said : {query}")

        except Exception as error:
            print("i didn't get that ...")
            return "none"

        return query.lower()


def TaskExe():
    wishMe()

    while True:
        query = takeCommand()

        if 'wiki' in query:
            wiki(query)
        elif 'who is' in query:
            whois(query)
        elif 'play' in query:
            playonyt(query)
        elif 'time' in query:
            time(query)
        elif 'who are you' in query:
            easter01()
        elif 'location' in query:
            location()
        elif 'temperature' in query:
            temperature(query)
        elif 'remember that' in query:
            write(query)
        elif 'what do you remember' in query:
            read()
        elif 'thanks' or 'thank you' in query:
            speak('you are welcome sir, always at your command')
            break





while True:
    permission = takeCommand()
    if 'friday' in permission:
        TaskExe()
    elif 'terminate' in permission:
         sys.exit()

