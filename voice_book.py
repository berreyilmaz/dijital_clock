import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog 

def metni_cikart(pdf_yolu):
    metin=""
    pdf_okuyucu = PyPDF2.PdfReader(open(pdf_yolu,'rb'))
    for sayfa_num in range(len(pdf_okuyucu.pages)):
        metin += pdf_okuyucu.pages[sayfa_num].extract_text()
    return metin

def metni_ses_cevir(metin,cikti_dosyası):
    sesli_cevirici = gTTS (text=metin, lang='tr')
    sesli_cevirici.save(cikti_dosyası)

def dosya_sec():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("PDf Dosyaları","*pdf")])
    if dosya_yolu:
        pdf_metin=metni_cikart(dosya_yolu)
        metni_ses_cevir(pdf_metin,"kaydet.mp3")
        os.system("start kaydet.mp3")


app = tk.Tk()
app.title("Sesli Kitap Uygulaması")
app.geometry("250x150")
secim_butonu = tk.Button(app,text="PDF seç",command=dosya_sec,padx=20,pady=20)
secim_butonu.pack(pady=20)






app.mainloop()
