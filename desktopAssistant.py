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
    server.login('arkosh6@gmail.com', 'ntcpedrliupxokoz')
    server.sendmail('arkosh6@gmail.com', to, content)
    server.close()


def possibleCommands():
    wishMe()
    while True:
        # Using while loop to run the assistant until user types exit or quit to leave the system
        query = takeCommand().lower()  # Taking Input from users and converting to string to lower case for security

        # System to set up some basics
        if 'cortana' in query:
            speak('My name is Sarah')  # verify name of the assistant
        elif 'open youtube' in query:
            webbrowser.open('https://youtube.com')
        elif 'quit assistant' in query:
            sys.exit(1)  # close the program
        elif 'how are you' in query:
            speak('I am Fine')

        # Other Functions Include
        elif 'open google' in query:
            webbrowser.open('https://google.com')
        elif 'open facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        # Play more music to make the assistant attractive.
        elif 'open spotify' in query:
            webbrowser.open('https://www.spotify.com/us/')
            
        elif 'open netflix' in query:
            webbrowser.open('https://www.netflix.com/us/')

        elif 'open twitter' in query:
            webbrowser.open('https://twitter.com/')

        elif 'open amazon' in query:
            webbrowser.open('https://www.amazon.com/')

        elif 'open github' in query:
            webbrowser.open('https://github.com/')

        elif 'open linkedin' in query:
            webbrowser.open('https://www.linkedin.com/')

        elif 'what is hackathon' in query:
            speak('Hackathon is a coding marathon')

        # open the application on windows platform
        elif 'open calculator' in query:
            subprocess.Popen(['calc.exe'])

        elif 'open windows media player' in query:
            subprocess.Popen(['wmplayer.exe'])

        # time and date related
        elif 'what time is it now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f'It is now {strTime}')

        elif 'what date it is today' in query:
            date = datetime.datetime.now()
            strDate = date.strftime("%A, %d %b %Y")
            print(strDate)
            speak(f'It is now {strDate}')

        # computer related functions
        elif 'open notepad' in query:
            notepad = 'C:\Windows\System32\notepad.exe'
            subprocess.Popen(notepad)

        elif 'open pycharm' in query:
            pycharm = '"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm 2022.1.3.lnk"'
            subprocess.Popen(pycharm)

        elif 'open vsc' in query:
            vsc = os.path.join(os.path.join(os.environ['USERPROFILE']),
                               'AppData\Local\Programs\Microsoft VS Code\Code.exe')
            subprocess.Popen(vsc)

        # send email
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "p0@live.com.au"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Boss. I am not able to send this email")

        # calculator
        elif 'sum' in query:
            nums = re.findall('\d+', query)
            result = sum(map(int, nums))
            speak(f'The sum is {result}')

        elif 'give me the difference' in query:
            nums = re.findall('\d+', query)
            result = int(nums[0]) - int(nums[1])
            speak(f'The difference is {result}')

        elif 'give me the product' in query:
            nums = re.findall('\d+', query)
            mul = int(nums[0]) * int(nums[1])
            speak(f'The product is {mul}')

        elif 'do a division' in query:
            nums = re.findall('\d+', query)
            dvsn = int(nums[0]) / int(nums[1])
            speak(f'The division is {dvsn}')

        elif 'give me the square root of the number' in query:
            nums = re.findall('\d+', query)
            # print(nums)
            sqrt = int(nums[0]) ** 0.5
            speak(f'The Square root of the number is {sqrt}')

        elif 'open file manager' in query:
            subprocess.Popen(['explorer.exe'])

        elif 'open google maps' in query:
            webbrowser.open('https://www.google.com/maps')
            speak('Here is Google Maps')
            engine.say('Here is Google Maps')

        elif 'open google drive' in query:
            webbrowser.open('https://drive.google.com/drive/my-drive')
            speak('Here is Google Drive')
            engine.say('Here is Google Drive')

        elif 'open google classroom' in query:
            webbrowser.open('https://classroom.google.com/u/0/h')
            speak('Here is Google Classroom')
            engine.say('Here is Google Classroom')

        elif 'open google meet' in query:
            webbrowser.open('https://meet.google.com/')
            speak('Here is Google Meet')
            engine.say('Here is Google Meet')

        elif 'open google docs' in query:
            webbrowser.open('https://docs.google.com/document/u/0/')
            speak('Here is Google Docs')
            engine.say('Here is Google Docs')

        elif 'open google sheets' in query:
            webbrowser.open('https://docs.google.com/spreadsheets/u/0/')
            speak('Here is Google Sheets')
            engine.say('Here is Google Sheets')

        elif 'open microsoft teams' in query:
            webbrowser.open('https://teams.microsoft.com/_#/')
            speak('Here is Microsoft Teams')
            engine.say('Here is Microsoft Teams')

        elif 'open microsoft office' in query or 'open office' in query:
            webbrowser.open('https://www.office.com/')
            speak('Here is Microsoft Office')
            engine.say('Here is Microsoft Office')

        elif 'open microsoft word' in query:
            webbrowser.open('https://www.office.com/launch/word')
            speak('Here is Microsoft Word')
            engine.say('Here is Microsoft Word')

        elif 'open microsoft excel' in query:
            webbrowser.open('https://www.office.com/launch/excel')
            speak('Here is Microsoft Excel')
            engine.say('Here is Microsoft Excel')

        elif 'open microsoft powerpoint' in query:
            webbrowser.open('https://www.office.com/launch/powerpoint')
            speak('Here is Microsoft PowerPoint')
            engine.say('Here is Microsoft PowerPoint')

        elif 'open microsoft outlook' in query:
            webbrowser.open('https://www.office.com/launch/outlook')
            speak('Here is Microsoft Outlook')
            engine.say('Here is Microsoft Outlook')

        elif 'open microsoft onedrive' in query:
            webbrowser.open('https://onedrive.live.com/')
            speak('Here is Microsoft OneDrive')
            engine.say('Here is Microsoft OneDrive')

        elif 'open microsoft onenote' in query:
            webbrowser.open('https://www.office.com/launch/onenote')
            speak('Here is Microsoft OneNote')
            engine.say('Here is Microsoft OneNote')


        elif 'open learn' in query:
            webbrowser.open('https://learn.canterbury.ac.nz/my/')
            speak('Here is Learn')
            engine.say('Here is Learn')

        elif 'create a new folder' in query:
            speak('What is the name of the folder?')
            engine.say('What is the name of the folder?')
            folder_name = takeCommand()
            speak('Where do you want to create the folder?')
            engine.say('Where do you want to create the folder?')
            folder_path = takeCommand()
            path = os.path.join(f"C:\\Users\\{getpass.getuser()}\\{folder_path}", folder_name)
            os.mkdir(path)
            speak('Folder created successfully')
            engine.say('Folder created successfully')

        elif 'write a note' in query:
            speak('What should i write, sir')
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak('Sir, Should i include date and time')
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- \n")
                file.write(note)
            else:
                file.write(note)

        elif 'quit' in query:
            speak('Thank you for using me, sir')
            exit()

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif 'tell me a fact' in query:
            speak(facts.get_fact())

        # if not in the list of commands, then search on google
        elif 'search for' in query or 'search' in query:
            query = query.replace("search for", "")
            query = query.replace("search", "")
            webbrowser.open("https://www.google.com/search?q=" + query)

        # search on youtube and open the first video
        elif 'play' in query:
            query = query.replace("play", "")
            webbrowser.open("https://www.youtube.com/results?search_query=" + query)
            time.sleep(5)
            # scroll down to the first video
            pyautogui.scroll(-1000)
            time.sleep(1)
            # click on the first video
            pyautogui.click(500, 500)

        # find the location of the user
        elif 'where am i' in query:
            ipAdd = requests.get('https://api.ipify.org').text
            print(ipAdd)
            url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            city = geo_data['city']
            country = geo_data['country']
            speak(f"I am not sure, but I think we are in {city} city of {country} country")

        # tell the weather of the user's location
        elif 'weather in' in query:
            # openweathermap key is 668f9e58b2a0294e1137d50af54fa23d
            api_key = "668f9e58b2a0294e1137d50af54fa23d"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            city = query.replace("weather in", "")
            complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" weather in " + city + " is " + str(
                    current_temperature) + " degree celsius" + "\n humidity in percentage is " + str(
                    current_humidity) + "\n description  " + str(weather_description))
            else:
                speak(" City Not Found ")


        elif 'weather' in query:
            # current weather of the user's location
            # openweathermap key is 668f9e58b2a0294e1137d50af54fa23d
            api_key = "668f9e58b2a0294e1137d50af54fa23d"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            ipAdd = requests.get('https://api.ipify.org').text
            print(ipAdd)
            url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            city = geo_data['city']
            complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" weather in " + city + " is " + str(
                    current_temperature) + " degree celsius" + "\n humidity in percentage is " + str(
                    current_humidity) + "\n description  " + str(weather_description))

            else:
                speak(" City Not Found ")

        # power off the computer
        elif 'shutdown' in query:
            speak('Shutting down the computer')
            os.system('shutdown /s /t 1')

        # restart the computer
        elif 'restart' in query:
            speak('Restarting the computer')
            os.system('shutdown /r /t 1')

        # sleep the computer
        elif 'sleep' in query:
            speak('Sleeping the computer')
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        # lock the computer
        elif 'lock' in query:
            speak('Locking the computer')
            ctypes.windll.user32.LockWorkStation()

        # hibernate the computer
        elif 'hibernate' in query:
            speak('Hibernating the computer')
            os.system('shutdown /h')

        # logout the computer
        elif 'logout' in query:
            speak('Logging out the computer')
            os.system('shutdown -l')

        # open the camera
        elif 'open camera' in query:
            speak('Opening the camera')
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(0)
                if k == 27:
                    break
            cap.release()

        # open the calculator
        elif 'open calculator' in query:
            speak('Opening the calculator')
            os.system('calc')

        # open the notepad
        elif 'open notepad' in query:
            speak('Opening the notepad')
            os.system('notepad')

        # open the paint
        elif 'open paint' in query:
            speak('Opening the paint')
            os.system('mspaint')

        # open the wordpad
        elif 'open wordpad' in query:
            speak('Opening the wordpad')
            os.system('write')

        # open the control panel
        elif 'open control panel' in query:
            speak('Opening the control panel')
            os.system('control')

        # open the task manager
        elif 'open task manager' in query:
            speak('Opening the task manager')
            os.system('taskmgr')

        elif "tell me a story" in query:
            # Scrape stories from a website or API that provides random stories:
            scrap = requests.get('https://www.mothstories.org/stories/random')
            soup = BeautifulSoup(scrap.content, 'html.parser')
            story = soup.find('div', class_='content')
            speak(story.get_text())

        # open the command prompt in new window
        elif 'open command prompt' in query:
            speak('Opening the command prompt')
            os.system('cmd')
            os.system('taskkill/cmd')


if __name__ == "__main__":
    possibleCommands()
