import speech_recognition as sr
import pyttsx3
import wikipedia
import pyjokes
import pywhatkit
import datetime


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)


def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()
def take_command():    
    try:
        with sr.Microphone() as source:

            print("Hi!! How can I help?")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey google' in command:
                command=command.replace("hey google",'')
    except:
        pass
    return command
   
   
def run_google():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace("play",'')
        talk(song+" playing in youtube")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I : %M %p")
        talk("Current time is: "+ time)
    elif 'who is' in command:
        person = command.replace("who is",'')
        info = wikipedia.summary(person,1)
        talk(info)
    elif "joke" in command:
        j=pyjokes.get_joke()
        talk(j)
   
    else:
        print("unable to reach you")
        talk("unable to reach you")
     
run_google()

