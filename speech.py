import pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import os
import webbrowser
import wikipedia


irona = pyttsx3.init('sapi5')
voices = irona.getProperty('voices')
# print(voices) |to print the property of different voices|
# print(voices[0].id) 
irona.setProperty('voice', voices[1].id)


def speak(audio):
    irona.say(audio)
    irona.runAndWait()
    
def greetingMessage():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("hello i am irona your technical assistant,tell me how can i help you")
    
def order():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening")
        speak("i am listening")
        r.pause_threshold = 1 #it will wait for user.
        audio = r.listen(source)
    try:
        print("recognizing...")
        speak("recognizing")
        query = r.recognize_google(audio, language = "en-in")
        print(f"sir you said {query}")
    except Exception as e:
        print("sorry i could not hear, please say thay again")
        speak("sorry i could not hear, please say thay again")
        return "None"
        
    return query


greetingMessage()
path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
while True:
    
    query = order().lower()
    if 'chrome' in query:
        speak("opening chrome for you")
        os.system("chrome")
    if 'notepad' in query:
        speak("opening notepad for you")
        os.system("notepad")
    if 'excel' in query:
        speak("opening excel for you")
        os.system("excel")
    if 'sublime' in query:
        speak("opening sublime for you")
        os.system("sublime")
    
        
    elif 'wikipedia' in query:
        speak("searching wikipedia")
        query = query.replace("wikipedia"," ")
        results = wikipedia.summary(query, sentences = 2)
        speak("according to wikipedia")
        print(results)
        speak(results)
        
    elif 'facebook' in query:
        speak("opening facebook for you")
        webbrowser.get(path).open("facebook.com")
    elif 'hackerrank' in query:
        speak("opening hackerrank for you")
        webbrowser.get(path).open("hackerrank.com")
    elif 'youtube' in query:
        speak("opening youtube for you")
        webbrowser.get(path).open("youtube.com")
    elif 'whatsapp' in query:
        speak("opening whatsapp for you")
        webbrowser.get(path).open("whatsapp.com")
    elif 'instagram' in query:
        speak("opening instagram for you")
        webbrowser.get(path).open("instagram.com")
    elif 'github' in query:
        speak("opening github for you")
        webbrowser.get(path).open("github.com")
        
        
    elif 'exit' in query:
        speak("thanyou, have a good day")
        break