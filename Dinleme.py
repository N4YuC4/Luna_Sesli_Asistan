import speech_recognition as sr

r = sr.Recognizer()

def dinleme(soru = False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        if soru: print(soru)
        veri = r.listen(source)
        Ses = ""
        try :
            Ses = r.recognize_vosk(veri,language='tr')
        except sr.UnknownValueError:
            print("Anlayamadım")
        except sr.RequestError:
            print("Sistem şuan çalışmıyor")
        Ses=Ses[14:-3]
        return Ses

