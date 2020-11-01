import pyttsx3
import datetime
import speech_recognition as sr

#Setting Up Sapi Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voices = engine.setProperty('voice', voices[1].id)
engine.setProperty("language","hi")

#This Speak function speaks a string.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Wishme command wishes the user according to data and time.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak('Good Evening Sir')
    
    speak('I am sophie')

#This function converts speech to text        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print('User said', query)
    except Exception as e:
        print("Say that again Please")
        return 'None'
    return query

#Main Code
if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()


        