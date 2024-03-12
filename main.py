import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def take_command():
    command=""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_word_meaning(word):
    url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response=requests.get(url)
    if(response.status_code==200):
        meaning=response.json()[0]['meanings'][0]['definitions'][0]['definition']
        return meaning
    else:
        return "Sorry, I couldn't find the meaning of the word."


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'my name is' in command:
        intro=command.replace('my name is',"")
        talk("Hi"+intro+"what can i do for you.")
    elif "meaning of" in command:
        idx=command.index('meaning of')
        word=command[idx+len('meaning of'):].strip()
        meaning=get_word_meaning(word) #to remove white spaces
        print(f"The meaning of {word} is {meaning}")
        talk(f"The meaning of {word} is {meaning}")
    else:
        talk('Please say the command again.')

while True:
    run_alexa()


