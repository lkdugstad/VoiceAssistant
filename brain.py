import speech_recognition as sr
from gtts import gTTS # google text to speech
import playsound # to play saved mp3 file
import os # to save/open files
import stocks
import category
import wikipedia as w
'''
dauerzuhoeren: https://pypi.org/project/SpeechRecognition/2.1.3/
programming tips: https://stackify.com/20-simple-python-performance-tuning-tips/
use python 3.8
'''
# ein brain mit den letzten 3-4 aufrufen sollte gespeichert werden. Verbindung zu vorherigen Anfragen
#globale Variablen
num = 1
def startRecord():
    '''
    Starts at the beginning of the programm
    gives feedback over the console
    Todo: give an accustic feedback when starting to record and when stopping to record
    :return: string consisting of the spoken words
    '''
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Begin der Aufnahme")
        audio = r.listen(source, phrase_time_limit=5) #5 sek lang zuhoeren
        transcript = r.recognize_google(audio, language="de-DE")
    print("Ende der Aufnahme")
    return transcript

def toSpeech(output):
    '''
    num to rename every audio file with different name to remove ambiguity
    :param output: the string which should be pronounced
    :return: prounounces
    '''
    global num
    num += 1
    print("gesprochen wird : ", output)
    toSpeak = gTTS(text= output, lang='de', slow=False)
    file = str(num) + ".mp3" # saving the audio file given by gtts
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)

def main():
    print("python main function")
    print(category.findCategory("aktiengewinne"))

def wikiAbfrage(keyWord):
    '''
    returns a summary of the given key word
    https://towardsdatascience.com/wikipedia-api-for-python-241cfae09f1c
    :param keyWord:
    :return: String of the summary
    '''
    w.set_lang("de")
    list = w.search(keyWord)
    return w.summary(list[0])

if __name__ == '__main__':
    main()
