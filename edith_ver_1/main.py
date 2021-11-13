import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()


# engine.say('hey there, i am edith. my name stands for, even dead, i am the hero !')
# engine.say('i was designed to manage and handle all the security and defence systems under the guidence of jarvis')
# engine.say('just to tell, jarvis is on maintainence break, so i was assigned to help you on the way')
# engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening ...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # command = 'edith who is facebook'
            if 'edith' in command:
                command = command.replace('edith', '')

    except:
        pass
    return command


def run_edith():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'who are you' in command:
        intro = 'hey there, i am edith. my name stands for, even dead, i am the hero !' \
                'i was designed to manage handle all the security and defence system under the guidence of jarvis.' \
                'just to tell, jarvis is on maintainence break, so i was assigned to help you on the way'
        talk(intro)
    else:
        talk('Sorry! i did not heard that. can you repeat please ?')
        print('Sorry! i did not heard that. can you repeat please ?')


while True:
    run_edith()
