import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
engine = pyttsx3.init('sapi5')  # 'sapi5' is 'microsaoft speech api'
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)
# there are two voices in my pc. 0 id is a male voice and 1 id is a female voice.


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon! ")
    else:
        speak("Good Evening!")

    speak("I am DuarDo. How can I serve you Boss?")


"""it takes microphone input and converts it into string"""


def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening...")
        # seconds of non-speaking audio before a phrase is considered complete
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # google speech recognizer engine
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"Boss: {query}\n")
    except Exception:
        # print(e)
        speak("Say That again Sir.")
        return "None"
    return query


"""to send email"""
# def sendEmail(to, message):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('arafatyeasir3@gmail.com', 'password')
#     server.sendmail('yeasirarafat.ratul@gmail.com', to, message)
#     server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()  # takecommand object converted to lower case

        # logic for excuting
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open udemy' in query:
            webbrowser.open("udemy.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow")

        elif 'play music' in query:
            music_folder = 'F:\\SONGS\\Favourite'
            songs = os.listdir(music_folder)
            os.startfile(os.path.join(music_folder, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss, the time is {strTime}")

        elif 'open code' in query:
            path = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'open sublime' in query:
            path = "C:\\Users\\Sublime Text 3\\sublime_text.exe"
            os.startfile(path)

        # elif 'send email' in query:
        #     try:
        #         speak("what should i say?")
        #         message = takeCommand()
        #         to = "yeasitrafat.ratul@gmail.com"
        #         sendEmail(to, message)
        #         speak("Email has been sent")
        #     except Exception:
        #         speak("Sorry,I could not send the email")
        elif 'Go To Sleep Mode' in query:
            speak("Okey Boss! I am quiting...")
            exit()
