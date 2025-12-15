#voice to speech conversion
#pip install SpeechRecognition
#pip install pyAudio
import speech_recognition as sr
def speech_text():
    r=sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Speak Anything : ")
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio) #google api
                print("You said : ",text)
                if text=='stop':
                    break
            except:
                print("Sorry could not recognize your voice")
speech_text()                
    