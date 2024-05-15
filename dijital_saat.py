from tkinter import Label, Tk
import time

def digital_saat():
    #saat alanı
    time_live = time.strftime("%H:%M:%S")
    etiket.config(text=time_live)
    #tarih alanı
    date_info = time.strftime("%d %B %Y")
    label_date.config(text=date_info)
    etiket.after(200,digital_saat)

app_windows = Tk()
app_windows.title = "Dijital Saat"
app_windows.geometry("400x400")
app_windows.resizable(1,1)
app_windows.configure(bg="black")

text_font = ("Boulder",36,'bold')
background = "black"
foreground = "white"
border_width = 20

#saat etiketi
etiket = Label(app_windows, font=text_font, bg = background, fg = foreground)
etiket.grid(row=0, column=1, padx=border_width, pady=10)

#tarih etiketi
label_date = Label(app_windows, font=text_font, bg = background, fg = foreground )
label_date.grid(row=1, column=1, padx=border_width, pady=10)

digital_saat()
app_windows.mainloop()