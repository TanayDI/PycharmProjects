import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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
    speak("i am Friday, online and ready")
    speak("How can i help you?")


def initiate():
    speak("initiating sequence...")
    speak("Starting all system applications,")
    speak("installing and checking all drivers,")
    speak("calibrating and examining all the core processors,")
    speak("Checking internet connection,")
    speak("wait a movement sir,")
    speak("all drivers are up and running, System initiated successfully!,")
    speak("now i am online")


