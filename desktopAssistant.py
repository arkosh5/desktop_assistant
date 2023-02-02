"""When speaking about an assistant, think about Alexa, Siri and Google's virtual assistant. Lately there have been a rise in development of smart assistants, take a look at your favorite website chances are very high it has a bot that answers common question asked regularly.

Some common tasks that can be handled in your local machine with the help of an assistant include:

    Open and close any application on your system.
    Search anything on Google, Youtube, Wikipedia and so on
    Get weather updates for any location asked.
    Tell current time & date
    Give calendar reminders on upcoming events.
    Send email through voice commands.
    Play or Stop music in our system.
    Solve any algebraic and mathematical problems.
    Restart, Sleep or Shut Down the system.

In order to build a desktop assistant, you might need some modules to help out. Some of the key ones include:
Pyttsx3, Speech Recognition, Twilio, Subprocesses, Wikipedia, and a web browser.

A desktop assistant can perform a single task or a variety of tasks, depending on the complexity of your coding. The
more advanced your assistant is, the more impressive it will be to potential employers. """
import getpass
import re

import cv2
# Importing the required modules
import pyttsx3
import datetime
import webbrowser
import os
import smtplib
import pyjokes
import requests
import subprocess
import sys
import time
import pyautogui
import ctypes
import speech_recognition as sr
import randfacts as facts
from bs4 import BeautifulSoup

engine = pyttsx3.init()  # Initializing the engine for the voice
rate = engine.getProperty('rate')  # Set the length of each statement
engine.setProperty('rate', rate)


# Check if an Internet connection is there or not
def checkInternet():
    print("Checking Internet")
    try:
        requests.get('https://www.google.com')
        return True
    except requests.ConnectionError:
        return False


# Function to quit Assisstant
def quit():
    print("Goodbye Boss. Have A Nice day")
    engine.say("Goodbye Boss")
    engine.runAndWait()
    sys.exit(1)


# Function to speak
def speak(audio):
    print(audio)
    # make it speak in female voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


# Function to wish me on start
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour <= 17:
        speak("Good AfterNoon!")

    else:
        speak("Good Evening!")

    speak("I am Mrs. Sarah The Desktop Assistant. how may I help you?")


# Function activate Ms. Tessa The Desktop Assistant
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except sr.UnknownValueError:
            time.sleep(5)
            speak("I can't Find Anything")
            print("I can't Find Anything")
            return "None"
        except sr.RequestError:
            speak("Say that again please")
            return "None"
    return query


# Main function


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    username = os.environ.get("GMAIL_USERNAME")
    password = os.environ.get("GMAIL_PASSWORD")
    server.login('username', password)
    server.sendmail('arkosh6@gmail.com', to, content)
    server.close()


def possibleCommands():
    wishMe()
    commands = {
        "open youtube": "youtube.com",
        "open google": "google.com",
        "open stackoverflow": "stackoverflow.com",
        "open gmail": "gmail.com",
        "open facebook": "facebook.com",
        "open instagram": "instagram.com",
        "open twitter": "twitter.com",
        "open reddit": "reddit.com",
        "open github": "github.com",
        "open linkedin": "linkedin.com",
        "open whatsapp": "web.whatsapp.com",
        "open messenger": "messenger.com",
        "open leetcode": "leetcode.com",
        "open hackerrank": "hackerrank.com"
    }
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open' in query:
            for key in commands:
                if key in query:
                    webbrowser.open(commands[key])
                    speak("Opening " + key)
                    break

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\arkos\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

if __name__ == "__main__":
    possibleCommands()
