import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit  
import datetime
import wikipedia
import pyjokes
import requests
import json
from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


listener = sr.Recognizer()
engine = pyttsx3.init()
# inorder to get female voice
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say('Hi,Alexa here....')
    engine.say(text)
    engine.runAndWait()

talk('Welcome to the personal Assistant, very glad to meet you ,How can I help you?')
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening to you...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            
    except:
        pass
    return command


def run():
    command = take_command()
    print(command)
    if 'play music' in command:
        #replace play with empty string
        music = command.replace('play music', '')
        talk('playing ' + music)
        # inorder to play song in youtube
        pywhatkit.playonyt(music)
        print(music)
    
    elif 'search' in command or 'play' in command:
        command = command.replace("search", "")
        command = command.replace("play", "")         
        webbrowser.open(command)    
    elif 'Hey Alexa' in command:
        person = command.replace('Hey Alexa', '')
        information = wikipedia.summary(person, 1)
        print(information)
        talk(information)
    elif 'time' in command:
        # in string format
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'weather' in command:
        def weather(city):
            city = city.replace(" ", "+")
            res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            location = soup.select('#wob_loc')[0].getText().strip()
            time = soup.select('#wob_dts')[0].getText().strip()
            info = soup.select('#wob_dc')[0].getText().strip()
            weather = soup.select('#wob_tm')[0].getText().strip()
            talk(time)
            talk(info)
            talk(weather+"°C")
        city = input("Enter the City Name->  ")
        city = city+" weather"
        weather(city)
        
    # reply by catching the word we are saying
    elif 'who are you?' in command:
        talk('I am a personal assistant')
    elif 'study' in command:
        talk('It is playing time')
    elif 'come here' in command:
        talk('I have to study')
    elif 'Tea or Coffee' in command:
        talk('No Thanks')
    elif 'Are you a student or teacher' in command:
        talk('I am an undergraduate student')
    elif 'Are you ok?' in command:
        talk('Yes dear')
    elif 'Can I have a coffee with you' in command:
        talk('Why not,I am ready')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry I didnot get you,Please say again.')

# run repeatedly if alexa didn't get you
while True:
    run()
