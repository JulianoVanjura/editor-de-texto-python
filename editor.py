from tkinter import *
from tkinter import filedialog, messagebox      # importa a opção para aparecer as caixas de save e load


# variaveis globais
nome = None
local = None


# função para abrir um novo arquivo
def novo():
    global nome
    resultado = messagebox.askquestion("Arquivo", "Deseja criar um arquivo em branco?")
    nome = ""
    # se o resultado for yes será criado um novo documento
    if resultado == "yes":
        if nome == "":
            nome = filedialog.asksaveasfilename(filetypes=(("Arquivo TXT - ", "*.txt"), ("Python - ", "*.py"),),
                                                        initialdir=local)
            arquivo = open(nome, "w")  # para escrever no arquivo
            texto.delete(0.0, END)  # para funcionar
            escreva = texto.get(0.0, END)
            arquivo.write(escreva)
            arquivo.close()


# salvar
def salvar():
    global nome
    arquivo = open(nome, "w")  # para escrever no arquivo
    escreva = texto.get(0.0, END)
    arquivo.write(escreva)
    arquivo.close()


# função para salvar como o arquivo
def salvar_arquivo():
    # para mostrar a opção de salvar
    # filetypes = para adicionar um tipo
    nome_arquivo = filedialog.asksaveasfilename(filetypes = (("Arquivo TXT - ", "*.txt"), ("Python - ", "*.py"),), initialdir =local)
    arquivo = open(nome_arquivo, "w")   # para escrever no arquivo
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


# diretorio
def diretorio():
    global local
    local = filedialog.askdirectory(initialdir="/")


# sair
def sair():
    janela.quit()


# Configurações
def configu():

    # funções dos botões
    # funções dos botões das cores das fontes
    def c_lightverde():
        texto["fg"] = "light green"

    def c_verde_fraco():
        texto["fg"] = "#00e581"

    def c_verde_claro():
        texto["fg"] = "#24ff00"

    def c_azul_verde():
         texto["fg"] = "#00c2df"

    def c_azul_claro():
        texto["fg"] = "#2500e0"

    def c_roxo_claro():
        texto["fg"] = "#8e00d8"

    def c_amarelo_claro():
        texto["fg"] = "#eaff00"

    def c_laranja_claro():
        texto["fg"] = "#ff5a00"

    def c_vermelho_claro():
        texto["fg"] = "#ff5f5f"

    def c_preto():
        texto["fg"] = "black"

    def c_branco():
        texto["fg"] = "white"

    def c_prata():
        texto["fg"] = "silver"

    def c_sinza():
        texto["fg"] = "#333333"

     # funções dos botões das cores do fundo do editor
    def c_lightverde_fundo():
        texto["bg"] = "light green"

    def c_verde_fraco_fundo():
        texto["bg"] = "#00e581"

    def c_verde_claro_fundo():
        texto["bg"] = "#24ff00"

    def c_azul_verde_fundo():
        texto["bg"] = "#00c2df"

    def c_azul_claro_fundo():
        texto["bg"] = "#2500e0"

    def c_roxo_claro_fundo():
        texto["bg"] = "#8e00d8"

    def c_amarelo_claro_fundo():
        texto["bg"] = "#eaff00"

    def c_laranja_claro_fundo():
        texto["bg"] = "#ff5a00"

    def c_vermelho_claro_fundo():
        texto["bg"] = "#ff5f5f"

    def c_preto_fundo():
        texto["bg"] = "black"

    def c_branco_fundo():
        texto["bg"] = "white"

    def c_prata_fundo():
        texto["bg"] = "silver"

    def c_sinza_fundo():
        texto["bg"] = "#333333"


    # janela
    window_config = Toplevel()
    window_config.geometry("500x500+300+100")

    # Frames cores das fontes
    frame_cores = Frame(window_config)
    frame_cores.pack()

    # frame da cor de fundo
    frame_cor_fundo = Frame(window_config)
    frame_cor_fundo.pack()

    # frame fontes
    frame_fontes = Frame(window_config)
    frame_fontes.pack()


    # Label dentro da janela
    lb_cor_font = Label(frame_cores, text="Configurações da fonte", pady=10, font=("arial", 12))
    lb_cor_font.pack()
    lb_separador = Label(frame_cores, text="{:_<80}".format("_"), pady=10).pack()
    lb_separator2 = Label(frame_cor_fundo, text="{:_<80}".format("_"), pady=10).pack()
    lb_separator3 = Label(frame_fontes, text="{:_<80}".format("_")).pack()

    # Botões de cores da fonte
    lb_texto_font = Label(frame_cores, text="Cor da fonte: ").pack(side=LEFT)
    bt_lightverde = Button(frame_cores, width=0, bg="light green", activebackground="light green", command=c_lightverde)
    bt_lightverde.pack(side=LEFT)
    bt_verde_fraco = Button(frame_cores, width=0, bg="#00e581", activebackground="#00e581", command=c_verde_fraco)
    bt_verde_fraco.pack(side=LEFT)
    bt_verde_claro = Button(frame_cores, width=0, bg="#24ff00", activebackground="#24ff00", command=c_verde_claro)
    bt_verde_claro.pack(side=LEFT)
    bt_azul_verde = Button(frame_cores, width=0, bg="#00c2df", activebackground="#00c2df", command=c_azul_verde)
    bt_azul_verde.pack(side=LEFT)
    bt_azul_claro = Button(frame_cores, width=0, bg="#2500e0", activebackground="#2500e0", command=c_azul_claro)
    bt_azul_claro.pack(side=LEFT)
    bt_roxo_claro = Button(frame_cores, width=0, bg="#8e00d8", activebackground="#8e00d8", command=c_roxo_claro)
    bt_roxo_claro.pack(side=LEFT)
    bt_amarelo_claro = Button(frame_cores, width=0, bg="#eaff00", activebackground="#eaff00", command=c_amarelo_claro)
    bt_amarelo_claro.pack(side=LEFT)
    bt_laranja_claro = Button(frame_cores, width=0, bg="#ff5a00", activebackground="#ff5a00", command=c_laranja_claro)
    bt_laranja_claro.pack(side=LEFT)
    bt_vermelho_claro = Button(frame_cores, width=0, bg="#ff5f5f", activebackground="#ff5f5f", command=c_vermelho_claro)
    bt_vermelho_claro.pack(side=LEFT)
    bt_preto = Button(frame_cores, width=0, bg="black", activebackground="black", command=c_preto)
    bt_preto.pack(side=LEFT)
    bt_branco = Button(frame_cores, width=0, bg="white", activebackground="white", command=c_branco)
    bt_branco.pack(side=LEFT)
    bt_prata = Button(frame_cores, width=0, bg="silver", activebackground="silver", command=c_prata)
    bt_prata.pack(side=LEFT)
    bt_sinza = Button(frame_cores, width=0, bg="#333333", activebackground="#333333", command=c_sinza)
    bt_sinza.pack(side=LEFT)

    # Botões de cores de fundo
    lb_fundo_font = Label(frame_cor_fundo, text="Cor de fundo: ").pack(side=LEFT)
    bt_lightverde2 = Button(frame_cor_fundo, width=0, bg="light green", activebackground="light green", command=c_lightverde_fundo)
    bt_lightverde2.pack(side=LEFT)
    bt_verde_fraco2 = Button(frame_cor_fundo, width=0, bg="#00e581", activebackground="#00e581", command=c_verde_fraco_fundo)
    bt_verde_fraco2.pack(side=LEFT)
    bt_verde_claro2 = Button(frame_cor_fundo, width=0, bg="#24ff00", activebackground="#24ff00", command=c_verde_claro_fundo)
    bt_verde_claro2.pack(side=LEFT)
    bt_azul_verde2 = Button(frame_cor_fundo, width=0, bg="#00c2df", activebackground="#00c2df", command=c_azul_verde_fundo)
    bt_azul_verde2.pack(side=LEFT)
    bt_azul_claro2 = Button(frame_cor_fundo, width=0, bg="#2500e0", activebackground="#2500e0", command=c_azul_claro_fundo)
    bt_azul_claro2.pack(side=LEFT)
    bt_roxo_claro2 = Button(frame_cor_fundo, width=0, bg="#8e00d8", activebackground="#8e00d8", command=c_roxo_claro_fundo)
    bt_roxo_claro2.pack(side=LEFT)
    bt_amarelo_claro2 = Button(frame_cor_fundo, width=0, bg="#eaff00", activebackground="#eaff00", command=c_amarelo_claro_fundo)
    bt_amarelo_claro2.pack(side=LEFT)
    bt_laranja_claro2 = Button(frame_cor_fundo, width=0, bg="#ff5a00", activebackground="#ff5a00", command=c_laranja_claro_fundo)
    bt_laranja_claro2.pack(side=LEFT)
    bt_vermelho_claro2 = Button(frame_cor_fundo, width=0, bg="#ff5f5f", activebackground="#ff5f5f", command=c_vermelho_claro_fundo)
    bt_vermelho_claro2.pack(side=LEFT)
    bt_preto2 = Button(frame_cor_fundo, width=0, bg="black", activebackground="black", command=c_preto_fundo)
    bt_preto2.pack(side=LEFT)
    bt_branco2 = Button(frame_cor_fundo, width=0, bg="white", activebackground="white", command=c_branco_fundo)
    bt_branco2.pack(side=LEFT)
    bt_prata2 = Button(frame_cor_fundo, width=0, bg="silver", activebackground="silver", command=c_prata_fundo)
    bt_prata2.pack(side=LEFT)
    bt_sinza2 = Button(frame_cor_fundo, width=0, bg="#333333", activebackground="#333333", command=c_sinza_fundo)
    bt_sinza2.pack(side=LEFT)

    window_config.mainloop()

# janela principal
janela = Tk()
janela.geometry("800x500+400+100")
janela.title("Editor de Texto")

frame_texto = Frame(janela)
frame_texto.pack(expand=YES, fill=BOTH)

texto = Text(frame_texto, font=("MonospaceTypewriter Regular", 11), bg="#333333", fg="black")
texto.pack(expand=YES, fill=BOTH)


# Cria a barra de menu
menu_topo = Menu(frame_texto, bg="light green", activebackground="#00ee76", fg="black")
janela.config(menu=menu_topo)

# menu de arquivos
file = Menu(menu_topo, bg="#00ee76", activebackground="light green")
menu_topo.add_cascade(label="  File  ", menu=file)
file.add_command(label="Novo              ", command=novo)
file.add_command(label="Salvar            ", command=salvar)
file.add_command(label="Salvar Como       ", command=salvar_arquivo)
file.add_command(label="Abrir             ", command=abrir_arquivo)
file.add_separator()
file.add_command(label="Diretorio          ", command=diretorio)
file.add_command(label="Sair              ", command=sair)

# Menu de configurações
configuracao = Menu(menu_topo, bg="#00ee76", activebackground="light green")
menu_topo.add_cascade(label="Configurações", menu=configuracao)
configuracao.add_command(label="Configurar editor   ", command=configu)


# Pede para salvar o arquivo quando abre o programa
#nome = filedialog.asksaveasfilename(filetypes = (("Arquivo TXT - ", "*.txt"), ("Python - ", "*.py"),), initialdir ="/home/dredix/Documentos")
#arquivo = open(nome, "w")   # para escrever no arquivo
#escreva = texto.get(0.0, END)
#arquivo.write(escreva)
#arquivo.close()




janela.mainloop()

