from dataclasses import replace
import speech_recognition as sr
from gtts import gTTS
from datetime import datetime
import webbrowser
from playsound import playsound
import time



r = sr.Recognizer()

while True:
      with sr.Microphone() as soundMe:
            audio = r.record(soundMe, duration = 4)
            try:
                  text = r.recognize_google(audio,language="th")
                  if text:
                        if "เปิด" in text:
                              text = text.replace("เปิด","")
                              text = text.strip()
                              
                              webbrowser.open("www."+text+".com")

                              TextToSpeech = gTTS(text , lang= "th")
                              TextToSpeech.save(text+'.mp3')

                              if TextToSpeech:
                                    playsound(text+'.mp3')

                              
            except:
                  text = "404"

            if "ปิด" in text:
                  print("ปิดโปรแกรมแล้ว")
                  playsound("exit.mp3")
                  break
            print("Detect => "+text)

