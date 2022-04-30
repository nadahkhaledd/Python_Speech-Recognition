import subprocess


def say(text):
    print(text)
    # subprocess.call('PowerShell -Command "Add-Type –AssemblyName System.Speech;'
    #                 ' (New-Object System.Speech.Synthesis.SpeechSynthesizer).'
    #                 'Speak(\'{}\');"'.format(text), shell=True)

    subprocess.call('mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""{}"")(window.close)")'.format(text))