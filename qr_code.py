import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode

#temel kodlar
def qr_code_olusutr():
    url = url_girdi.get()

    if url:
        qr_url = pyqrcode.create(url)
        dosya_yolu = filedialog.asksaveasfile(defaultextension=".jpg",filetypes=[("SVG Dosyaları","*.jpg")])
        if dosya_yolu:
             qr_url.svg(dosya_yolu, scale=8)
             durum_etiketi.config(text="QR kodu oluşturuldu ve kaydedildi.")

#tasarım
uygulama_pencere = tk.Tk()
uygulama_pencere.title("QR kod oluşturucu")
etiket = tk.Label(uygulama_pencere,text="URL'yi girin:")
url_girdi = tk.Entry(uygulama_pencere,width=40)
buton = tk.Button(uygulama_pencere,text="QR kodu oluştur",command=qr_code_olusutr)
durum_etiketi = tk.Label(uygulama_pencere,text="")

etiket.grid(row=0,column=0,padx=10,pady=10)
url_girdi.grid(row=0,column=1,padx=10,pady=10)
buton.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
durum_etiketi.grid(row=2,column=1,columnspan=2,padx=10,pady=10)







uygulama_pencere.mainloop()