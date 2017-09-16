from tkinter import *
from tkinter import filedialog      # importa a opção para aparecer as caixas de save e load


# função para salvar o arquivo
def salvar_arquivo():
    # para mostrar a opção de salvar
    # filetypes = para adicionar um tipo
    fileName = filedialog.asksaveasfilename(filetypes = (("Arquivo TXT - ", "*.txt"), ("Python - ", "*.py"),))
    arquivo = open(fileName, "w")   # para escrever no arquivo
    escreva = texto.get(0.0, END)
    arquivo.write(escreva)
    arquivo.close()


# função para abrir um arquivo
def abrir_arquivo():
    abrir = filedialog.askopenfilename()    # para escolher o arquivo
    file = open(abrir, "r")     # para ler o arquivo
    conteudo = file.read()
    texto.delete(0.0, END)
    texto.insert(0.0, conteudo)


janela = Tk()
janela.geometry("800x500+400+100")
janela.title("Editor de Texto")

texto = Text(janela, font=("arial", 11), bg="#333333", fg="silver")
texto.pack(expand=YES, fill=BOTH)

menu_topo = Menu(janela, bg="#424242", activebackground="#00ee76", fg="#00ee76")
janela.config(menu=menu_topo)

file = Menu(menu_topo, bg="#00ee76", activebackground="#00ee76")
menu_topo.add_cascade(label="  FILE  ", menu=file)
file.add_command(label="Salvar            ", command=salvar_arquivo)
file.add_command(label="Abrir             ", command=abrir_arquivo)

janela.mainloop()
