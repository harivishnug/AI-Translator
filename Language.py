import googletrans
import pyttsx3
from gtts import gTTS
from pygame import mixer
from playsound import playsound

engine = pyttsx3.init()     #init is used to run the program automatically
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)    # setting our assistant voice

def talk(text):     #making a function as talk (say and repeat)
    engine.say(text)
    engine.runAndWait()

translator = googletrans.Translator()
talk('Enter Your Sentence to Translate')
a=input('Enter Your Sentence to Translate : ')
talk('Note : For Language code refer "Language.txt" ')
print('Note : For Language code refer "Language.txt" ')
talk('Enter Language That you want to change')
b=input('Enter Language That you want to change (code only permitted): ')
translated = translator.translate(a, dest=b)
talk(a)
talk('changed into your selected language')
print(translated.text)

def playaudio(audio):
    audio = gTTS(translated.text, lang=b)
    audio.save('easy.mp3')
    #playaudio('C:\Users\G.Harivishnu\Desktop\language\easy.mp3')

    playsound(audio)

#def convert_to_audio(text):

# print(googletrans.LANGUAGES)
