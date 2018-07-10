import fnmatch
import tkinter


pencere = tkinter.Tk()
pencere.title("Arama Programı")
pencere.resizable(width=False , height=False)
pencere.geometry("400x500")

def degistir():
    yazi.config(text = "Belirlendi.")
    buton.config(text = "Değiştir.")
def degistir1():
    yazi1.config(text = "Belirlendi.")
    buton1.config(text = "Değiştir.")
def isimleAra():
    """Uzantıyı sadece .*uzantı diye kabul ediyor,çözemedim..."""


    import os
    import time
    uzanti = giris1.get()
    """Sorunua böyle bir çözüm buldum...."""
    uzanti = "*"+uzanti
    """"""""
    dizin = giris.get()
    dosyaadi = giris2.get()



    for root, dirs, files in os.walk(dizin):
        for filename in fnmatch.filter(files, uzanti):

            if filename == (dosyaadi) in files:
                status = os.stat(os.path.join(root, filename))
                """değiştrime tarihi"""
                stat.config(text = "Değiştirilme Tarihi : " + time.ctime(os.path.getmtime(os.path.join(root, filename))))

                """açılma tarihi"""
                stat1.config(text = "Oluşturulma Tarihi : " + time.ctime(os.path.getctime(os.path.join(root, filename))))


                sonuc1.config(text="Arama Sonucu : " + os.path.join(root, filename))

            else:
                pass

def uzantiAra():
    """Uzantıyı .uzantı olarak alıyor."""
    import os
    directory = giris.get()
    uzanti = giris1.get()
    """win olduğundan dir ile belirttik """
    for root, dirs, files in os.walk(directory):

        for filename in files:
            if filename.lower().endswith(uzanti):
                sonuclar = os.path.join(root, filename)

                print(sonuclar)
                """Eğer pycharmda açarsanız konsol ekranında hepsini göreceksiniz."""

                sonuc.config(text = "Arama Sonuçları :\n " + sonuclar)
                """Arayüzde göstericek"""




yazi = tkinter.Label(pencere)
yazi.config(text="Arama için path bir belirleyin. \n ÖRN : C:/Users/doğanay/Desktop")
yazi.pack()

giris = tkinter.Entry(pencere, bd = 3)
giris.config()
giris.pack()

buton = tkinter.Button(pencere)
buton.config(text = "Belirle" , bd = 3 , command = degistir)
buton.pack()

yazi1 = tkinter.Label(pencere)
yazi1.config(text = "Bir dosya uzantısı belirleyin. \n ÖRN : *.py")
yazi1.pack()



giris1 = tkinter.Entry(pencere, bd = 3)
giris1.config()
giris1.pack()

buton1 = tkinter.Button(pencere)
buton1.config(text = "Uzantı belirle" ,bd = 3, command = degistir1)
buton1.pack()






yazi2 = tkinter.Label(pencere)
yazi2.config(text="İsim ile aratmak için uzantısı ile isim girin.\n ÖRN: python.girdiğiniz uzantı")
yazi2.pack()

giris2 = tkinter.Entry(pencere, bd = 3)
giris2.pack()

buton2 = tkinter.Button(pencere , text = "İsimle Ara", bd = 3 , command = isimleAra)
buton2.pack()


sonuc1 = tkinter.Label(pencere)
sonuc1.config(text="İsimle Arama Sonucu :\n ")
sonuc1.pack()

stat = tkinter.Label(pencere)
stat.config()
stat.pack()

stat1 = tkinter.Label(pencere)
stat1.config()
stat1.pack()





buton2 = tkinter.Button(pencere)
buton2.config(text = "Bütün uzantıları ara" ,bd = 3, command = uzantiAra)
buton2.pack()

sonuc = tkinter.Label(pencere)
sonuc.config(text="Arama Sonucu \n: ")
sonuc.pack()




pencere.mainloop()