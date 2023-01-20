# 마이크를 통해 말하는 내용을 인식하여 나타내는 코드

# 사용 패키지
import speech_recognition as sr
#import sys #-- 텍스트 저장시 사용
import pyttsx3


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    speech = r.listen(source)
    #sys.stdout = open('audio_output.txt', 'w') #-- 텍스트 저장시 사용
    engine = pyttsx3.init()

    
try:
    audio = r.recognize_google(speech, language="ko-KR")
    print("Your speech thinks like\n " + audio)      
    # testing
    engine.say(audio)
    engine.runAndWait()
except sr.UnknownValueError:
    print("Your speech can not understand")
except sr.RequestError as e:
    print("Request Error!; {0}".format(e))

#sys.stdout.close() #-- 텍스트 저장시 사용