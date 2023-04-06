import speech_recognition as sr

r = sr.Recognizer()

def dinleme(soru = False):
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        if soru: print(soru)
        veri = r.listen(source)
        ses = ""
        try :
            ses = r.recognize_vosk(veri,language='tr')
        except sr.UnknownValueError:
            print("Anlayamadım")
        except sr.RequestError:
            print("Sistem şuan çalışmıyor")
        return ses

