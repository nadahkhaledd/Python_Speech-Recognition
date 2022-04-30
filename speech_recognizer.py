import speech_recognition as sr
from initial import play_audio
from commands import Commander

r = sr.Recognizer()
cmd = Commander()

running = True
def initSpeech():
    #print('listening...')
    play_audio('./audio/1.wav')

    with sr.Microphone() as source:
        #print('say something')
        print('listening...')
        audio = r.listen(source)

    play_audio('./audio/2.wav')

    command = ''
    try:
        command = r.recognize_google(audio)
    except:
        print('couldn\'t understand.')

    print(command)
    if command in ['quit', 'exit']:
        global running
        running = False

    cmd.discover(command)

if __name__ == '__main__':
    while running == True:
        initSpeech()