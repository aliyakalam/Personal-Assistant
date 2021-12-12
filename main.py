import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit  
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
# inorder to get female voice
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say('Hi,Alexa here....')
    engine.say(text)
    engine.runAndWait()


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
        talk('Current time ' + time)
        print(time)
    # reply by catching the word we are saying
    elif 'who are you?' in command:
        talk('I am a personal assistant')
    elif 'study' in command:
        talk('It is playing time')
    elif 'come here' in command:
        talk('I have to study')
    elif 'Are you a student or teacher' in command:
        talk('I am an undergraduate student')
    elif 'Are you ok?' in command:
        talk('Yes dear')
    elif 'Can I have a coffee with you' in command:
        talk('Why not,I am ready')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry I didnot get you.Please say again.')

# run repeatedly if alexa didn't get you
while True:
    run()