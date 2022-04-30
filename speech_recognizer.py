import pyaudio
import wave
import speech_recognition as sr

from initial import play_audio

r = sr.Recognizer()

def initSpeech():
    play_audio('./audio/1.wav')
    print('listening...')

    with sr.Microphone() as source:
        #print('say something')
        audio = r.listen(source)

    play_audio('./audio/2.wav')

    command = ''

    try:
        command = r.recognize_google(audio)
    except:
        print('couldn\'t understand.')

    print(command)

initSpeech()