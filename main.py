import time, webbrowser
from Dinleme import dinleme




def karşılık(): #verilecek yanıtlar bu fonksiyon üzerinde tanımlanır
    if "deneme" in ses:
        print("Sistem başarılı bi şekilde çalışıyor")
    elif "arama yap" in ses:
        arama = input("Ne aramak istiyorsunuz?") #arama = dinleme("Ne aramak istiyorsunuz?")
        url = f"https://www.google.com/search?q={arama}"
        webbrowser.get().open(url)
    elif "saat kaç" in ses:
        print(time.strftime("Saat şuan: %H:%M:%S"))
    


while 1:
    input("Dinleme başlatmak için Enterlayın...")    #test aşamasında ses tanıma özelliğini devredışı bırakmak için satır başına hashtag ekleyin
    ses = dinleme().lower()    #test aşamasında ses tanıma özelliğini devredışı bırakmak için satır başına hashtag ekleyin

    #ses= input(">>")   #ses tanıma özelliğini etkinleştirmek için satır başına hashtag ekleyin
    print(ses)
    karşılık()   #yanıt vermek için kullanılan fonksiyon çağrılır
