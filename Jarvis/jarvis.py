import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random


chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) 
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=22 and hour<3:
        speak("Good Night!")
    elif hour>=3 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis, your Virtual Assistant. What should I browse")


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        print("Done!")
        speak("Done")

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 
        webbrowser.get(chrome_path).open(query)

    except Exception as e:
        print(e) 

        print("Sorry I did't get that, Please try again")
        speak("Sorry I didn't get that, Please try again")
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.startttls()
#     server.login('prajwalkambale85@gmail.com', 'PDKey8524@A')
#     server.sendmail('prajwalkambale85@gmail.com', to, content)
#     server.close()

if __name__ == "__main__":
    speak("Today is a Great day")
wishMe()
# while True:
if 1: 
  query = takeCommand().lower()

  if 'wikipedia' in query:
      speak('Searching Wikipedia...')
      query = query.replace("wikipedia", " ")
      results = wikipedia.summary(query, sentences=3)
      speak("According to Wikipedia")
      speak(results) 
      print(results)

  elif 'youtube' in query:
      webbrowser.open("youtube.com")
      speak('Opening YT...')
      print("Opening Youtube")

  elif 'google' in query:
      webbrowser.open("google.com")
      speak('Opening Google...')
      print("Opening Google")

  elif 'play music' in query:
      music_dir = 'F:\\Python Programs\\Jarvis\\Sample music'
      songs = os.listdir(music_dir)
      os.startfile(os.path.join(music_dir, songs[0]))

  elif 'time' in query :
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
        print({strTime})

  elif 'open vs code' in query :
      codePath = "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
      os.startfile(codePath)

  elif 'Chrome' in query :
      codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
      os.startfile(codePath)

  elif 'cmd' in query :
      codePath = "%windir%\\system32\\cmd.exe"
      os.startfile(codePath)

  elif 'Settings' in query :
      codePath1 = "%windir%\\System32\\Control.exe"
      os.startfile(codePath1)


#   elif 'mail mom' in query:
#       try:
#           speak("What should I write?")
#           content = takeCommand()
#           to = "padmashrikambale@gmail.com"
#           sendEmail(to, content)
#           speak("Email has been sent!")
      
        

  elif 'thank you' in query:
      speak("That\'s my pleasure")

  elif 'close' in query:
      speak("Good Bye")
      exit()

  elif ' Prajwal Playlist ' in query:
      webbrowser.open("https://www.youtube.com/watch?v=zXLgYBSdv74&list=PL6UWbgJ-85DI2ZUHPgMZmq-g41LHcaJwW")
      speak("Playing Prajwal Playlist")

  elif 'close' in query:
      speak("Good Bye")
      exit()






    
    