import speech_recognition as sr
from initial import play_audio
import subprocess

r = sr.Recognizer()

def say(text):
    subprocess.call('PowerShell -Command "Add-Type –AssemblyName System.Speech;'
                    ' (New-Object System.Speech.Synthesis.SpeechSynthesizer).'
                    'Speak(\'{}\');"'.format(text), shell=True)

def initSpeech():
    print('listening...')
    play_audio('./audio/1.wav')

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
    say(str(command))

if __name__ == '__main__':
    initSpeech()