
# A FAZER
# ADAPTAR O TAMNHO DA JANELA AO TAMNHO DO BOTAO QUE JA ESTA ADAPTADO

from configparser import *
from tkinter import *

# Configuração
config = ConfigParser()
config.read('warning.config')
start = config.get('START','start')

#Tela Inicial
def greetings():
    root = Tk()
    root.title("Boas Vindas")
    root.geometry("300x400+200+100")
    
    label = Label(text='HELLO', fg='white', bg='blue')
    label.pack(pady=30)
    
    root.mainloop()
    
# Mostra Configuração
def show_config():
    root = Tk()
    root.title("Configuração")
    root.geometry("300x400+100+100")
    
    config.set('START', 'start', '1')
    
    with open('warning.config', 'w') as configfile:
        config.write(configfile)
    
    root.mainloop()
    
# Pisca o Botao
def blink_label(label):
    fg_color = label.cget("foreground")
    bg_color = label.cget("background")
    label.config(foreground=bg_color, background=fg_color)
    label.after(500, blink_label, label)

# Tela de alerta
def show_alert():
    root = Tk()
    root.overrideredirect(True)
    root.geometry("700x150+100+100")
    root.configure(bg="red")
    
    
    bt1 = Button(root, text="INTERVALO", \
                 font=("Arial", 80), bg="red", fg="white", \
                 command=root.destroy \
        )
    bt1.config(height=bt1.winfo_reqheight()) # recommended
    bt1.pack(fill="x")

    blink_label(bt1)

    root.mainloop()


if start == '1' :
    greetings()
else:
    show_alert()
