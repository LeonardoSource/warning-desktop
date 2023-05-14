# FAZER A CONFIGURACAO DO TEXTO ALTERNATIVO

from configparser import *
from tkinter import *
from tkinter import ttk

# Configuração
config = ConfigParser()
config.read('warning.config')
start = config.get('START','start')
warn = config.get('WARNINGS', '3')

#Tela Inicial
def greetings():
    root = Tk()
    root.title("Warning Desktop")
    root.geometry("300x400+200+100")
    
    notebook = ttk.Notebook(root)
    notebook.pack(fill='x')
    
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    
    notebook.add(tab1, text='Boas Vindas')
    notebook.add(tab2, text='Configurações')
    
    # mensagem de boas vindas
    bemvindo = ttk.Label(tab1, text='Bem Vindo você está no WARNING DESKTOP')
    bemvindo.pack(pady=40)
    
    # Botao de iniciar o a mensagem de aviso
    start_now = Button(tab1, text="Iniciar Agora >>", bg="green", command=root.destroy)
    start_now.pack(fill='x')
    
    # Testa configuração atual
    test = Button(tab1, text="Testar configuracao atual", bg="yellow", command=show_alert )
    test.pack(fill='x')
    
    # OPções de configuracoes
    label1 = Label(tab2, text='Texto')
    msg = Entry(tab2)
    check3 = Checkbutton(tab2, text='OPção 3')
    check4 = Checkbutton(tab2, text='OPção 4')
    check5 = Checkbutton(tab2, text='OPção 5')
    check6 = Checkbutton(tab2, text='OPção 6')
    label1.pack(side='top')
    msg.pack(side='top')
    check3.pack(side='top')
    check4.pack(side='top')
    check5.pack(side='top')
    check6.pack(side='top')
    
    # texto alternativo
    alt_text = msg.get()
    
    # SE EXIBE A CAIXA DE CONFIGURACAO NA INICIALIZAÇÃO
    
    # Joga o resultado boleano na variavel show_again
    show_again = Checkbutton(root, text='Mostar na inicialização', variable=start)
    show_again.pack(pady=30)
    
    config.set('START', 'start', start)
    
    # Salva as configuracoes no arquivo
    with open('warning.config', 'w') as configfile:
        config.write(configfile)
    
    root.mainloop()
    
    
# Pisca o Botao (A Label e o botao)
def blink_label(label):
    fg_color = label.cget("foreground")
    bg_color = label.cget("background")
    label.config(foreground=bg_color, background=fg_color)
    label.after(500, blink_label, label)

# Tela de alerta
def show_alert():
    root = Tk()
    root.overrideredirect(True) # Retira as decorações da janela
    root.geometry("700x150+100+100")
    root.configure(bg="red")
    
    
    # Botao principal
    bt1 = Button(root, text=warn, \
                 font=("Arial", 80), bg="red", fg="white", \
                 command=root.destroy \
        )
    bt1.config(height=bt1.winfo_reqheight()) # recommended
    bt1.pack(fill='x')

    blink_label(bt1)

    root.mainloop()

def main():
    if start == '1' :
        greetings()
        show_alert()
    else:
        show_alert()
    
if __name__ == '__main__':
    __main__ = main()
