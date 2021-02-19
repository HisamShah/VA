import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5') # microsoft voice api
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning !!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !!")
    else:
        speak("Good Evening !!")

    speak("I am your assistant sir !! how may I help you ?")

def takeCommand():
    ''' takes microphone input and return string '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ... ... ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising... ... ...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Please say that again .. .. ")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    if 1:
    
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia. .. ..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'play' in query:
           song = query.replace('play', '')
           speak('playing ' + song)
           pywhatkit.playonyt(song) 
        elif'search in browser' in query:
            speak("what should i search")
            #chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            search = takeCommand().lower()
            webbrowser.open_new_tab(search+".com")
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'discord' in query:
            webbrowser.open("discord.com")            
        elif 'open codeforces' in query:
            webbrowser.open("codeforces.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open chrome' in query:
            webbrowser.open("Chrome")
        elif 'github' in query:
            webbrowser.open("github.com")
        elif 'amazon' in query:
            webbrowser.open("amazon.in")
        elif 'flipkart' in query:
            webbrowser.open("flipkart.com")    
        elif 'mail' in query:
            webbrowser.open("mail.google.com")     
        elif 'open team' in query:
           t = "C:\\Users\\nadim\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart\\teams.exe"
           os.startfile(t)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Hello!! The time is {strTime}")
        elif 'vs code' in query:
            N = "C:\\Users\\nadim\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(N)
        elif 'droidcam' in query:
            d = "C:\Program Files (x86)\DroidCam\DroidCamApp.exe"
            os.startfile(d) 
        elif 'filmora' in query:
            f = "C:\Program Files\Wondershare\Filmora9\Wondershare Filmora9.exe"
            os.startfile(f)    
        elif 'pycharm' in query:
            p = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.1\\bin\\pycharm64.exe"
            os.startfile(p)                
        elif 'competitive programming template' in query:
            codePath = "C:\\Users\\HP\\Desktop\\submit.cpp"
            os.startfile(codePath)
        elif 'whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
        elif 'joke' in query:
            speak(pyjokes.get_joke())  
        elif 'are you single' in query:
             speak('I am in a relationship with wifi')    
        elif 'Prime minister of India' in query:
            speak('Narendra Modi')


#while True:
  #  takeCommand()