import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import time
import vlc


r = sr.Recognizer()
translator = GoogleTranslator()

with sr.Microphone() as source:
   r.energy_threshold = 3000
   r.adjust_for_ambient_noise(source, duration=0.5)
   audio = r.listen(source)

   try:
       speech_text = r.recognize_google(audio, language='es')
       print(f"Spanish: {speech_text}")
   except sr.UnknownValueError:
       print("Could not understand.")
   except sr.RequestError:
       print("Could not request result from google.")
       

   translated_text = GoogleTranslator(source='es', target='en').translate(speech_text)
   print(f"English: {translated_text}")
       
       
   voice = gTTS(translated_text, lang='en')
   voice.save("voice.mp3")

   player = vlc.MediaPlayer("/Users/joshliu/Desktop/side_projects/voice_translater/Speech-to-Speech-translator/voice.mp3")
   player.play()
   time.sleep(10)
   