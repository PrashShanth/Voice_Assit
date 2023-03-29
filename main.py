import speech_recognition as sr 
from time import ctime
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS
r = sr.Recognizer()

def recourd_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            prashanth_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            prashanth_speak("Sorry, I did not get that")
        except sr.RequestError:
            prashanth_speak("Sorry, My speech service is down")
        return voice_data

def prashanth_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        prashanth_speak('My name is Prashanth')
    if 'what time is it' in voice_data:
        prashanth_speak(ctime())
    if 'search' in voice_data:
        search = recourd_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        prashanth_speak('Here is what i found for ' + search)
    
    if 'find location' in voice_data:
        location = recourd_audio('what is your location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        prashanth_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
prashanth_speak('How can i help you')
while 1:
    voice_data = recourd_audio()
    respond(voice_data)
