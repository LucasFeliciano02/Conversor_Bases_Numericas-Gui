import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# cores
cor0 = "#444466"  # Preta
cor1 = "#feffff"  # branca / white
cor2 = "#6f9fbd"  # azul
cor3 = "#38576b"  # valor
cor4 = "#403d3d"  # letra
cor5 = '#e89613'    # laranja


janela = Tk()
janela.title('Conversor')
janela.geometry('400x310')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)
janela.iconbitmap('bases_numericas.ico')  # icon do app


style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190)


# Criando 2 Frames para a janela

frame_cima = Frame(janela, width=400, height=60, bg=cor1, pady=0, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=400, height=300,
                    bg='#d9d9d9', pady=12, padx=20)
frame_baixo.grid(row=2, column=0, sticky=NW)


# bin()  oct()  hex()  int()

# * FUNÇÕES

def converter():

    def numero_to_decimal(numero, base):

        decimal = int(numero, base)

        binario = bin(decimal)
        octal = oct(decimal)
        hexadecimal = hex(decimal)

        label_binario['text'] = str(binario[2:])
        label_octal['text'] = str(octal[2:])
        label_decimal['text'] = str(decimal)
        label_hexadecimal['text'] = str(hexadecimal[2:].upper())

    
    numero = entry_valor.get()
    
    if numero == '':
        messagebox.showwarning('Atenção!', 'Insira algum numero')
        return
    
    base = combo.get()

    # Definindo o valor da base


    if base == 'BINARIO':
        base = 2
    elif base == 'OCTAL':
        base = 8
    elif base == 'DECIMAL':
        base = 10
    elif base == 'HEXADECIMAL':
        base = 16
    else:
        messagebox.showwarning('Atenção!', 'Selecione uma base numérica!')
        return
    
    numero_to_decimal(numero, base)


# * ---------- Função Copiar resultados -----------


    def copiar_resultado():
        info = label_binario['text']
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo('Sucesso', 'O resultado foi copiado com sucesso')

    botao_gerar_senha = Button(frame_baixo, command=copiar_resultado, text='Copiar', width=5, height=1, padx=0,
                               relief='raised', overrelief='ridge', anchor='center', font=('Ivy 7 bold'), bg=cor1, fg=cor0)
    botao_gerar_senha.place(x=320, y=64)

    def copiar_resultado2():
        info = label_octal['text']
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo('Sucesso', 'O resultado foi copiado com sucesso')

    botao_gerar_senha = Button(frame_baixo, command=copiar_resultado2, text='Copiar', width=5, height=1, padx=0,
                               relief='raised', overrelief='ridge', anchor='center', font=('Ivy 7 bold'), bg=cor1, fg=cor0)
    botao_gerar_senha.place(x=320, y=104)

    def copiar_resultado3():
        info = label_decimal['text']
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo('Sucesso', 'O resultado foi copiado com sucesso')

    botao_gerar_senha = Button(frame_baixo, command=copiar_resultado3, text='Copiar', width=5, height=1, padx=0,
                               relief='raised', overrelief='ridge', anchor='center', font=('Ivy 7 bold'), bg=cor1, fg=cor0)
    botao_gerar_senha.place(x=320, y=144)

    def copiar_resultado4():
        info = label_hexadecimal['text']
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo('Sucesso', 'O resultado foi copiado com sucesso')

    botao_gerar_senha = Button(frame_baixo, command=copiar_resultado4, text='Copiar', width=5, height=1, padx=0,
                               relief='raised', overrelief='ridge', anchor='center', font=('Ivy 7 bold'), bg=cor1, fg=cor0)
    botao_gerar_senha.place(x=320, y=188)


# Configurando frame_cima com titulo

app_nome = Label(frame_cima, text='Conversor de base numérica',
                 relief=FLAT, anchor='center', font='System 20', bg=cor5, fg=cor0)
app_nome.place(x=10, y=14)


# Configurando frame_baixo


# Combobox
bases = ['BINARIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']

combo = ttk.Combobox(frame_baixo, width=12, justify=CENTER, font='Ivy 12 bold')
combo['values'] = (bases)
combo.place(x=35, y=10)

# Entry do lado da combobox
entry_valor = Entry(frame_baixo, width=9, justify='center',
                    font=("", 13), highlightthickness=1, relief='solid')
entry_valor.place(x=160, y=10)

# Botao converter

botao_converter = Button(frame_baixo, command=converter, text='CONVERTER', relief=RAISED,
                         overrelief=RIDGE, font='Ivy 8 bold', bg='#9cff7a', fg=cor4)
botao_converter.place(x=247, y=10)


# Configurando labels em baixo

label_binario = Label(frame_baixo, text='BINARIO', width=12,
                      relief=FLAT, anchor='nw', font='Courier 13 bold', bg=cor0, fg=cor1)
label_binario.place(x=35, y=60)

label_binario = Label(frame_baixo, text='', width=13,
                      relief=FLAT, anchor='center', font='Courier 13 bold', fg=cor4)
label_binario.place(x=170, y=60)


label_octal = Label(frame_baixo, text='OCTAL', width=12,
                    relief=FLAT, anchor='nw', font='Courier 13 bold', bg=cor0, fg=cor1)
label_octal.place(x=35, y=100)

label_octal = Label(frame_baixo, text='', width=13, relief=FLAT,
                    anchor='center', font='Courier 13 bold', fg=cor4)
label_octal.place(x=170, y=100)


label_decimal = Label(frame_baixo, text='DECIMAL', width=12,
                      relief=FLAT, anchor='nw', font='Courier 13 bold', bg=cor0, fg=cor1)
label_decimal.place(x=35, y=140)

label_decimal = Label(frame_baixo, text='', width=13,
                      relief=FLAT, anchor='center', font='Courier 13 bold', fg=cor4)
label_decimal.place(x=170, y=140)


label_hexadecimal = Label(frame_baixo, text='HEXADECIMAL', width=12,
                          relief=FLAT, anchor='nw', font='Courier 13 bold', bg=cor0, fg=cor1)
label_hexadecimal.place(x=35, y=180)

label_hexadecimal = Label(frame_baixo, text='', width=13,
                          relief=FLAT, anchor='center', font='Courier 13 bold', fg=cor4)
label_hexadecimal.place(x=170, y=180)


# * Centralizando o arquivo

# Dimensoes da janela
largura = 400
altura = 310

# Resolução do nosso sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenwidth()
# print(largura_screen, altura_screen)  # para saber as dimensoes do monitor


# Posição da janela
posx = largura_screen/2 - largura/1.8
posy = altura_screen/5 - altura/5

# Definir a geometria
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


janela.mainloop()
