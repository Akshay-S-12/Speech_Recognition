#text to speech conversion
import pyttsx3
#calss==>init()
txt_sp=pyttsx3.init()
voices=txt_sp.getProperty('voices')
txt_sp.setProperty('voice',voices[1].id) #female voice
txt_sp.setProperty('volume',0.9) #volume 0 to 1
text=input("Enter the text : ")
txt_sp.say(text)
txt_sp.runAndWait() 