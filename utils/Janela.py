import threading
import pygetwindow as gw
import tkinter as tk
from tkinter import colorchooser
import os
import time
from ctypes import windll
from PIL import ImageTk, Image
from utils.Centralizar_Janela import centralizar_janela
from utils.Fechar_Janela import fechar_janela
from utils.Idioma import definir_idioma
from utils.Cliques import WhereToClick
from utils.Cor import Alterar_Cor, Definir_Cor, Botoes_Cores
from utils.Texto_Tela_Auto_Aceitar import atualizar_mensagem
from utils.Botao_Confirmar import confirmar
from utils.Barra_de_Titulo import *

def tela_selecao_de_modo(jogo_está_aberto):
    global tela, Role_1, Role_2, modo_de_jogo, roles
    centralizar_janela(root, 378, 506)
    root.title("League Lobby Clicker - Saralapa")
    label_titulo.config(text=root.title())
    frame_barra_de_titulo.config(width=root.winfo_width())
    botao_fechar.place(x=root.winfo_width()-45)
    botao_minimizar.place(x=root.winfo_width()-45*2)
    botao_doacao.place(x=root.winfo_width()-45*3)

    frame_topo_janela.config(width=root.winfo_width())
    frame_esquerda_janela.config(height=root.winfo_height())
    frame_direita_janela.config(height=root.winfo_height())
    frame_direita_janela.place(x=root.winfo_width()-1)
    frame_base_janela.config(width=root.winfo_width())
    frame_base_janela.place(y=root.winfo_height()-1)

    tela = "seleção de modo de jogo"
    Role_1=None
    Role_2=None
    for frame in frame_botoes_roles:
        frame.pack_forget()
        frame.place_forget()
    for botao in botoes_roles:
        botao.pack_forget()
        botao.place_forget()
    label_auto_aceitar.pack_forget()
    label_auto_aceitar.place_forget()
    for frame in frame_botoes_idiomas:
        frame.pack_forget()
        frame.place_forget()
    for botao in botoes_idiomas:
        botao.pack_forget()
        botao.place_forget()
    for botao in botoes_cores:
        botao.pack_forget()
        botao.place_forget()
    frame_botao_cor_personalizada.pack_forget()
    frame_botao_cor_personalizada.place_forget()

    if idioma=="Portugues":
        modos_de_jogo=["Escolha alternada", "Ranqueada solo duo", "ARAM", "Blitz do Nexus", "Arena", "URF", "Todos por um", "Apenas auto aceitar"]
    elif idioma=="English":
        modos_de_jogo=["Draft pick", "Ranked solo duo", "ARAM", "Nexus Blitz", "Arena", "URF", "One for all", "Just auto accept"]

    botao_icone_idioma.pack()
    botao_icone_idioma.place(relx=0.8915, rely=0.075375)
    botao_icone_cor.pack()
    botao_icone_cor.place(relx=0.0195, rely=0.072375)
    frame_borda_topo.pack()
    frame_borda_topo.place(relx=0.4988888888888888, rely=0.1095, anchor="center")
    label_borda_topo.pack()
    frame_borda_inferior.pack()
    frame_borda_inferior.place(relx=0.4988888888888888, rely=0.956, anchor="center")
    frame_botao_desfazer.config(bd=1)
    frame_botao_desfazer.pack()
    frame_botao_desfazer.place(relx=0.025, rely=0.9815, anchor="sw")
    frame_botao_confirmar.pack()
    frame_botao_confirmar.place(relx=0.975, rely=0.9815, anchor="se")

    i=0
    for botao in botoes_modos_de_jogo:
        frame_botoes_modos_de_jogo[i].pack()
        frame_botoes_modos_de_jogo[i].place(relx=0.0245, rely=0.1565 + i * 0.09675)
        botao.config(text=modos_de_jogo[i], command=lambda t=modos_de_jogo[i]: Atualizar_Modo_de_Jogo(t))
        botao.pack()
        botao.place(relx=0.0275, rely=0.158 + i * 0.0968)
        i+=1
    
    if idioma=="Portugues":
        label_borda_topo.config(text="Escolha o modo de jogo")
        if modo_de_jogo == None:
            texto_inferior.set("Modo de jogo\nescolhido:")
        else:
            texto_inferior.set(f"Modo de jogo\nescolhido: {modo_de_jogo}")
        botao_desfazer.config(text="Desfazer")
        botao_confirmar.config(text="Confirmar")
    elif idioma=="English":
        label_borda_topo.config(text="Select game mode")
        if modo_de_jogo == None:
            texto_inferior.set("Selected game\nmode:")
        else:
            texto_inferior.set(f"Selected game\nmode: {modo_de_jogo}")
        botao_desfazer.config(text="Undo")
        botao_confirmar.config(text="Confirm")
    botao_desfazer.config(height=0)

    def Jogo_Aberto(jogo_está_aberto):
        global modo_de_jogo
        while True:
            if jogo_está_aberto == False:
                return
            time.sleep(30)
            if not [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"] and jogo_está_aberto == True:
                if idioma == "Portugues":
                    modo_de_jogo = "Apenas auto aceitar"
                elif idioma == "English":
                    modo_de_jogo = "Just auto accept"
                jogo_está_aberto = False
                tela_auto_aceitar() 
                return

    if jogo_está_aberto == True:
        thread_jogo_aberto = threading.Thread(target=Jogo_Aberto(jogo_está_aberto))
        thread_jogo_aberto.daemon = True
        thread_jogo_aberto.start()

def tela_selecao_de_role():
    global tela, botoes_roles, roles
    tela = "seleção de role"
    for botao in botoes_modos_de_jogo:
        botao.pack_forget()
        botao.place_forget()
    for frame in frame_botoes_modos_de_jogo:
        frame.pack_forget()
        frame.place_forget()
    botao_icone_idioma.pack_forget()
    botao_icone_idioma.place_forget()
    botao_icone_cor.pack_forget()
    botao_icone_cor.place_forget()

    if idioma=="Portugues":
        label_borda_topo.config(text="Escolha em que posição você vai jogar")
        if Role_1 == None:
            botao_desfazer.config(text="Menu anterior")
        else:
            botao_desfazer.config(text="Desfazer")
    elif idioma=="English":
        label_borda_topo.config(text="Choose which position you will play")
        if Role_1 == None:
            botao_desfazer.config(text="Previous menu")
        else:
            botao_desfazer.config(text="Undo")

    if modo_de_jogo == "Blitz do Nexus" or modo_de_jogo== "Nexus Blitz":
        centralizar_janela(root, 378, 265)
        frame_barra_de_titulo.config(width=root.winfo_width())
        frame_topo_janela.config(width=root.winfo_width())
        frame_esquerda_janela.config(height=root.winfo_height())
        frame_direita_janela.config(height=root.winfo_height())
        frame_direita_janela.place(x=root.winfo_width()-1)
        frame_base_janela.config(width=root.winfo_width())
        frame_base_janela.place(y=root.winfo_height()-1)

        frame_botao_desfazer.place(rely=0.966)
        frame_botao_confirmar.place(rely=0.966)
        frame_borda_topo.place(relx=0.4988888888888888, y=28, anchor="center")
        frame_borda_inferior.place(relx=0.4988888888888888, rely=0.914, anchor="center")
        if idioma=="Portugues":
            texto_inferior.set("Posição escolhida:")
        elif idioma=="English":
            texto_inferior.set("Selected role:")

        for botao in botoes_roles:
            botao.destroy()

        if idioma == "Portugues":
            roles = ["Jungle", "Rota", "Preencher"]
        elif idioma == "English":
            roles = ["Jungle", "Lane", "Fill"]

        botoes_roles = [tk.Button(root, text=texto2, command=lambda t=texto2: Atualizar_Roles(t)) for texto2 in roles]
        i=0
        for botao in botoes_roles:
            frame_botoes_roles[i].pack()
            frame_botoes_roles[i].place(relx=0.0245, y=83 + i * 49)
            botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)
            botao.pack()
            botao.place(relx=0.0275, y=84 + i * 49)
            i+=1

    else:   
        centralizar_janela(root, 378, 410)
        frame_barra_de_titulo.config(width=root.winfo_width())
        frame_topo_janela.config(width=root.winfo_width())
        frame_esquerda_janela.config(height=root.winfo_height())
        frame_direita_janela.config(height=root.winfo_height())
        frame_direita_janela.place(x=root.winfo_width()-1)
        frame_base_janela.config(width=root.winfo_width())
        frame_base_janela.place(y=root.winfo_height()-1)

        frame_botao_desfazer.place(rely=0.9775)
        frame_botao_confirmar.place(rely=0.9775)
        frame_borda_inferior.place(relx=0.4988888888888888, rely=0.946, anchor="center")
        frame_borda_topo.place(relx=0.4988888888888888, y=11, anchor="center")
        if idioma=="Portugues":
            texto_inferior.set(f"Primeira role:\nSegunda role:")
        elif idioma=="English":
            texto_inferior.set(f"First role:\nSecond role:")

        for botao in botoes_roles:
            botao.destroy()
        
        if idioma=="Portugues":
            roles = ["Top", "Jungle", "Mid", "ADC", "Suporte", "Preencher"]
        elif idioma=="English":
            roles = ["Top", "Jungle", "Mid", "ADC", "Support", "Fill"]
        botoes_roles = [tk.Button(root, text=texto2, command=lambda t=texto2: Atualizar_Roles(t)) for texto2 in roles]

        i=0
        for botao in botoes_roles:
            frame_botoes_roles[i].pack()
            frame_botoes_roles[i].place(relx=0.0245, y=81 + i * 49)
            botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)
            botao.pack()
            botao.place(relx=0.0275, y=82 + i * 49)
            i+=1

def tela_alterar_idioma():
    global tela
    altura_janela_idioma = 108 + len(lista_idiomas) * 49
    centralizar_janela(root, 378, altura_janela_idioma)
    frame_barra_de_titulo.config(width=root.winfo_width())
    frame_topo_janela.config(width=root.winfo_width())
    frame_esquerda_janela.config(height=root.winfo_height())
    frame_direita_janela.config(height=root.winfo_height())
    frame_direita_janela.place(x=root.winfo_width()-1)
    frame_base_janela.config(width=root.winfo_width())
    frame_base_janela.place(y=root.winfo_height()-1)

    tela = "alterar idioma"
    frame_borda_topo.pack_forget()
    frame_borda_topo.place_forget()
    for botao in botoes_modos_de_jogo:
        botao.pack_forget()
        botao.place_forget()
    for frame in frame_botoes_modos_de_jogo:
        frame.pack_forget()
        frame.place_forget()
    for frame in frame_botoes_roles:
        frame.pack_forget()
        frame.place_forget()
    frame_botao_confirmar.pack_forget()
    frame_botao_confirmar.place_forget()
    botao_icone_idioma.pack_forget()
    botao_icone_idioma.place_forget()
    botao_icone_cor.pack_forget()
    botao_icone_cor.place_forget()

    i = 0
    for botao in botoes_idiomas:
        frame_botoes_idiomas[i].pack()
        frame_botoes_idiomas[i].place(relx=0.0245, y=39 + i * 49)
        botao.pack()
        botao.place(x=(root.winfo_width()-botao.winfo_reqwidth())//2, y=40 + i * 49)
        i+=1

    frame_borda_inferior.pack()
    frame_borda_inferior.place(relx=0.4988888888888888, y=149, anchor="center")
    if idioma=="Portugues":
        texto_inferior.set("Idioma selecionado: Português")
        botao_desfazer.config(text="Confirmar")
    elif idioma=="English":
        texto_inferior.set(f"Selected language: {idioma}")
        botao_desfazer.config(text="Confirm")

    frame_botao_desfazer.place(relx=0.4988888888888888, y=-19, anchor="center")

def tela_selecao_de_cor():
    global tela
    centralizar_janela(root, 303, 388)
    root.title("League Lobby Clicker - S...")
    label_titulo.config(text=root.title())
    frame_barra_de_titulo.config(width=root.winfo_width())
    botao_fechar.place(x=root.winfo_width()-45)
    botao_minimizar.place(x=root.winfo_width()-45*2)
    botao_doacao.place(x=root.winfo_width()-45*3)
    frame_topo_janela.config(width=root.winfo_width())
    frame_esquerda_janela.config(height=root.winfo_height())
    frame_direita_janela.config(height=root.winfo_height())
    frame_direita_janela.place(x=root.winfo_width()-1)
    frame_base_janela.config(width=root.winfo_width())
    frame_base_janela.place(y=root.winfo_height()-1)

    tela = "seleção de cor"
    frame_borda_topo.pack_forget()
    frame_borda_topo.place_forget()
    for botao in botoes_modos_de_jogo:
        botao.pack_forget()
        botao.place_forget()
    for frame in frame_botoes_modos_de_jogo:
        frame.pack_forget()
        frame.place_forget()
    for frame in frame_botoes_roles:
        frame.pack_forget()
        frame.place_forget()
    frame_botao_confirmar.pack_forget()
    frame_botao_confirmar.place_forget()
    botao_icone_idioma.pack_forget()
    botao_icone_idioma.place_forget()
    botao_icone_cor.pack_forget()
    botao_icone_cor.place_forget()
    frame_borda_inferior.pack_forget()
    frame_borda_inferior.place_forget()

    if idioma == "Portugues":
        botao_desfazer.config(text="Confirmar")
        botao_cor_personalizada.config(text="Cor personalizada")
    elif idioma == "English":
        botao_desfazer.config(text="Confirm")
        botao_cor_personalizada.config(text="Custom color")
    botao_desfazer.config(height=2)
    frame_botao_desfazer.config(bd=2)
    frame_botao_desfazer.place(relx=0.4988888888888888, y=-30, anchor="center")
    botao_cor_personalizada.config(height=2)
    frame_botao_cor_personalizada.pack()
    frame_botao_cor_personalizada.place(relx=0.4988888888888888, y=67, anchor="center")
    j = 0
    k = 0
    for i in range(len(botoes_cores)):
        if k==2:
            k=0
        if i%2==0 and i!=0:
            j+=1
        botoes_cores[i].config(width=17, height=2, bd=2)
        botoes_cores[i].pack()
        botoes_cores[i].place(relx=0.04875 + k * 0.47725 , y=105 + j * 56)
        k+=1

def tela_auto_aceitar():
    global tela, jogo_está_aberto
    centralizar_janela(root, 375, 130)
    frame_barra_de_titulo.config(width=root.winfo_width())
    botao_fechar.place(x=root.winfo_width()-45)
    botao_minimizar.place(x=root.winfo_width()-45*2)
    botao_doacao.place(x=root.winfo_width()-45*3)
    frame_topo_janela.config(width=root.winfo_width())
    frame_esquerda_janela.config(height=root.winfo_height())
    frame_direita_janela.config(height=root.winfo_height())
    frame_direita_janela.place(x=root.winfo_width()-1)
    frame_base_janela.config(width=root.winfo_width())
    frame_base_janela.place(y=root.winfo_height()-1)

    if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
        jogo_está_aberto = True

    tela = "auto aceitar"
    frame_borda_topo.pack_forget()
    frame_borda_topo.place_forget()
    for botao in botoes_modos_de_jogo:
        botao.pack_forget()
        botao.place_forget()
    for frame in frame_botoes_modos_de_jogo:
        frame.pack_forget()
        frame.place_forget()
    for frame in frame_botoes_roles:
        frame.pack_forget()
        frame.place_forget()
    for botao in botoes_roles:
        botao.pack_forget()
        botao.place_forget()
    frame_botao_confirmar.pack_forget()
    frame_botao_confirmar.place_forget()
    frame_borda_inferior.pack_forget()
    frame_borda_inferior.place_forget()
    botao_icone_idioma.pack_forget()
    botao_icone_idioma.place_forget()
    botao_icone_cor.pack_forget()
    botao_icone_cor.place_forget()

    label_auto_aceitar.pack()
    label_auto_aceitar.place(relx=0.4988888888888888, y=62, anchor="center")
    
    if idioma=="Portugues":
        botao_desfazer.config(text="Menu principal")
    elif idioma=="English":
        botao_desfazer.config(text="Main menu")
    frame_botao_desfazer.place(relx=0.4988888888888888, y=-24, anchor="center")

    thread_imagem = threading.Thread(target=WhereToClick)
    thread_imagem.daemon = True
    thread_imagem.start()

    thread_mensagem = threading.Thread(target=atualizar_mensagem)
    thread_mensagem.daemon = True
    thread_mensagem.start()

def desfazer():
    global modo_de_jogo, tela, Role_1, Role_2, roles, jogo_está_aberto
    if idioma=="Portugues":
        if tela == "seleção de modo de jogo":
            modo_de_jogo = None
            texto_inferior.set("Modo de jogo\nescolhido:")
        elif tela == "seleção de role":
            if Role_2 != None:
                Role_2 = None
                if modo_de_jogo!="Blitz do Nexus":
                    texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role:")
                else: texto_inferior.set("Posição escolhida:")
            elif Role_1 != None:
                Role_1 = None
                botao_desfazer.config(text="Menu anterior")
                if modo_de_jogo!="Blitz do Nexus":
                    texto_inferior.set(f"Primeira role:\nSegunda role:")
                else: texto_inferior.set("Posição escolhida:")
            else:
                jogo_está_aberto = False
                tela_selecao_de_modo(jogo_está_aberto)
        elif tela=="auto aceitar":
            modo_de_jogo=None
            Role_1=None
            Role_2=None
            jogo_está_aberto = False
            tela_selecao_de_modo(jogo_está_aberto)
        elif tela=="alterar idioma":
            tela_selecao_de_modo(jogo_está_aberto)
        elif tela == "seleção de cor":
            tela_selecao_de_modo(jogo_está_aberto)
    elif idioma=="English":
        if tela == "seleção de modo de jogo":
            modo_de_jogo = None
            texto_inferior.set("Selected game\nmode:")
        elif tela == "seleção de role":
            if Role_2 != None:
                Role_2 = None
                if modo_de_jogo!="Nexus Blitz":
                    texto_inferior.set(f"First role: {Role_1}\nSecond role:")
                else: texto_inferior.set("Selected role:")
            elif Role_1 != None:
                Role_1 = None
                botao_desfazer.config(text="Previous menu")
                if modo_de_jogo!="Nexus Blitz":
                    texto_inferior.set(f"First role:\nSecond role:")
                else: texto_inferior.set("Selected role:")
            else:
                jogo_está_aberto = False
                tela_selecao_de_modo(jogo_está_aberto)
        elif tela=="auto aceitar":
            modo_de_jogo=None
            Role_1=None
            Role_2=None
            jogo_está_aberto = False
            tela_selecao_de_modo(jogo_está_aberto)
        elif tela=="alterar idioma":
            tela_selecao_de_modo(jogo_está_aberto)
        elif tela == "seleção de cor":
            tela_selecao_de_modo(jogo_está_aberto)

def Atualizar_Modo_de_Jogo(valor):
    global modo_de_jogo, roles
    modo_de_jogo = valor
    if idioma=="Portugues":
        texto_inferior.set(f"Modo de jogo\nescolhido: {modo_de_jogo}")
    elif idioma=="English":
        texto_inferior.set(f"Selected game\nmode: {modo_de_jogo}")

def Atualizar_Roles(valor):
    global Role_1, Role_2, roles
    if idioma=="Portugues":
        if Role_1 == None or modo_de_jogo == "Blitz do Nexus":
            Role_1 = valor
            botao_desfazer.config(text="Desfazer")
            if modo_de_jogo != "Blitz do Nexus":
                if Role_1!="Preencher":
                    texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role:")
                else:
                    texto_inferior.set(f"Posição escolhida: {Role_1}")
            else:
                texto_inferior.set(f"Posição escolhida: {Role_1}")
                if Role_1!="Preencher":
                    Role_2="Preencher"
        elif Role_2 == None and Role_1 != "Preencher" and modo_de_jogo != "Blitz do Nexus":
            Role_2 = valor
            texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role: {Role_2}")
            if Role_1 == Role_2:
                Role_2 = None
                texto_inferior.set(f"A primeira e a segunda\nposição não podem ser iguais!")
                root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role:") if tela=="seleção de role" and Role_2==None and Role_1 != None else None)
                root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role: {Role_2}") if tela=="seleção de role" and Role_1 != None and Role_2!=None else None)
    elif idioma=="English":
        if Role_1 == None or modo_de_jogo == "Nexus Blitz":
            Role_1 = valor
            botao_desfazer.config(text="Undo")
            if modo_de_jogo != "Nexus Blitz":
                if Role_1!="Fill":
                    texto_inferior.set(f"First role: {Role_1}\nSecond role:")
                else:
                    texto_inferior.set(f"Selected role: {Role_1}")
            else:
                texto_inferior.set(f"Selected role: {Role_1}")
                if Role_1!="Fill":
                    Role_2="Fill"
        elif Role_2 == None and Role_1 != "Fill" and modo_de_jogo != "Nexus Blitz":
            Role_2 = valor
            texto_inferior.set(f"First role: {Role_1}\nSecond role: {Role_2}")
            if Role_1 == Role_2:
                Role_2 = None
                texto_inferior.set(f"The first and second\nroles cannot be the same!")
                root.after(2000, lambda: texto_inferior.set(f"First role: {Role_1}\nSecond role:") if tela=="seleção de role" and Role_2==None and Role_1 != None else None)
                root.after(2000, lambda: texto_inferior.set(f"First role: {Role_1}\nSecond role: {Role_2}") if tela=="seleção de role" and Role_1 != None and Role_2!=None else None)
    
def Atualizar_Idioma(valor):
    global idioma
    idioma = valor.replace("ê", "e")
    caminho_idioma = os.path.join(os.path.expanduser("~"),"League Lobby Clicker - Saralapa", "League_Lobby_Clicker_idioma-Saralapa.txt")
    with open(caminho_idioma, "w") as file:
        file.write(idioma)
    if idioma == "Portugues":
        botao_desfazer.config(text="Confirmar")
        texto_inferior.set(f"Idioma selecionado: {valor}")
    elif idioma == "English":
        botao_desfazer.config(text="Confirm")
        texto_inferior.set(f"Selected language: {valor}")

def Atualizar_Cor(valor):
    global cor, botao_icone_cor, botao_icone_idioma, imagem_cor, imagem_idioma
    if valor != None:
        cor = valor
        caminho_cor = os.path.join(os.path.expanduser("~"),"League Lobby Clicker - Saralapa", "League_Lobby_Clicker_cor-Saralapa.txt")
        with open(caminho_cor, "w") as file:
            file.write(cor)
        
        frame_botao_desfazer.config(bg=cor)
        botao_desfazer.config(fg=cor)
        label_borda_topo.config(fg=cor)
        label_borda_inferior.config(fg=cor)
        botao_desfazer.config(fg=cor)
        frame_botao_desfazer.config(bg=cor)
        botao_confirmar.config(fg=cor)
        frame_botao_confirmar.config(bg=cor)
        for frame in frame_botoes_idiomas:
            frame.config(bg=cor)
        for botao in botoes_idiomas:
            botao.config(fg=cor)
        for frame in frame_botoes_modos_de_jogo:
            frame.config(bg=cor)
        for botao in botoes_modos_de_jogo:
            botao.config(fg=cor)
        for frame in frame_botoes_roles:
            frame.config(bg=cor)
        for botao in botoes_roles:
            botao.config(fg=cor)
        label_auto_aceitar.config(fg=cor)
        frame_botao_cor_personalizada.config(bg=cor)
        botao_cor_personalizada.config(fg=cor)
        label_titulo.config(fg=cor)

        imagem_cor = ImageTk.PhotoImage(Alterar_Cor("Images/Color-change.png", "#000000", cor))
        botao_icone_cor.config(image=imagem_cor)

        imagem_idioma = ImageTk.PhotoImage(Alterar_Cor("Images/Language.png", "#ffffff", cor))
        botao_icone_idioma.config(image=imagem_idioma)

def Criar_Janela():
    global frame_botoes_roles, label_auto_aceitar, frame_botoes_idiomas, botoes_modos_de_jogo, botao_icone_idioma, frame_borda_topo, label_borda_topo, frame_borda_inferior, frame_botao_desfazer, frame_botao_confirmar, frame_botoes_modos_de_jogo, texto_inferior, botao_desfazer, botao_confirmar, root, lista_idiomas, idioma, jogo_está_aberto, botoes_roles, botoes_idiomas, botao_icone_cor, cor, botoes_cores, label_borda_inferior, botao_icone_cor, imagem_cor, imagem_idioma, botao_cor_personalizada, modo_de_jogo, frame_botao_cor_personalizada, frame_barra_de_titulo, frame_topo_janela, frame_esquerda_janela, label_titulo, frame_direita_janela, frame_base_janela, label_icone
    idioma = definir_idioma()
    cor = Definir_Cor()
    modo_de_jogo = None
    jogo_está_aberto = False
    root = tk.Tk()

    root.title("League Lobby Clicker - Saralapa")
    root.iconbitmap('Images/icon.ico')
    root.config(bg="#191919")
    root.overrideredirect(True)
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", lambda: fechar_janela(root))
    HWND = windll.user32.GetParent(root.winfo_id())
    
    windll.user32.SetWindowLongW(HWND, -20, windll.user32.GetWindowLongW(HWND, -20) & ~0x00000080 | 0x00040000)
    root.wm_withdraw()
    root.after(10, lambda: root.wm_deiconify())

    frame_borda_topo = tk.LabelFrame(root, bg="#191919", width=210, height=30, bd=0)
    frame_borda_topo.pack(side="top", anchor="center", pady=5)

    label_borda_topo = tk.Label(frame_borda_topo, font=("Arial", 14), text="Escolha o modo de jogo", bg="#191919", fg=cor, height=0)
    label_borda_topo.pack()

    modos_de_jogo = ["Escolha alternada", "Ranqueada solo duo", "ARAM", "Blitz do Nexus", "Arena", "URF", "Todos por um", "Apenas auto aceitar"]

    frame_botoes_modos_de_jogo = [tk.Frame(root, bg=cor) for _ in modos_de_jogo]

    botoes_modos_de_jogo = [tk.Button(root, text=texto1, command=lambda t=texto1: Atualizar_Modo_de_Jogo(t)) for texto1 in modos_de_jogo]

    for botao in botoes_modos_de_jogo:
        botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)
        botao.pack(pady=5)

    for frame in frame_botoes_modos_de_jogo:
        frame.config(width=360, height=41, bd=0)

    roles = ["Top", "Jungle", "Mid", "ADC", "Suporte", "Preencher"]

    frame_botoes_roles = [tk.Frame(root, bg=cor) for _ in roles]

    botoes_roles = [tk.Button(root, text=texto2, command=lambda t=texto2: Atualizar_Roles(t)) for texto2 in roles]

    for botao in botoes_roles:
        botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)
        botao.pack(pady=5)

    for frame in frame_botoes_roles:
        frame.config(width=360, height=41, bd=0)

    lista_idiomas = ["Português", "English"]

    frame_botoes_idiomas = [tk.Frame(root, bg=cor) for _ in lista_idiomas]

    botoes_idiomas = [tk.Button(root,text=texto3, command=lambda t=texto3: Atualizar_Idioma(t)) for texto3 in lista_idiomas]

    for botao in botoes_idiomas:
        botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)
        botao.pack(pady=5)

    for frame in frame_botoes_idiomas:
        frame.config(width=360, height=41, bd=0)

    frame_borda_inferior = tk.LabelFrame(root, bg="#191919", width=210, height=30, bd=0)

    texto_inferior = tk.StringVar(frame_borda_inferior)
    texto_inferior.set("Modo de jogo\nescolhido:")

    label_borda_inferior = tk.Label(frame_borda_inferior, textvariable=texto_inferior, bg="#191919", fg=cor)
    label_borda_inferior.pack()

    frame_botao_desfazer = tk.Frame(root, bg=cor, width=85, height=24, bd=1)
    frame_botao_desfazer.pack()

    botao_desfazer = tk.Button(frame_botao_desfazer, text="Desfazer", command=lambda: desfazer(), bg="#1f1f1f", fg=cor, bd=1)
    botao_desfazer.pack()

    frame_botao_confirmar = tk.Frame(root, bg=cor, width=65, height=24, bd=1)
    frame_botao_confirmar.pack()

    botao_confirmar = tk.Button(frame_botao_confirmar, text="Confirmar", command=lambda: confirmar(), bg="#1f1f1f", fg=cor, bd=1)
    botao_confirmar.pack()
    
    imagem_idioma = ImageTk.PhotoImage(Alterar_Cor("Images/Language.png", "#ffffff", cor))
    try:
        botao_icone_idioma = tk.Button(root, image=imagem_idioma, command=tela_alterar_idioma, bd=0, bg="#191919", width=31, height=31)
        botao_icone_idioma.pack()
    except: None

    imagem_cor = ImageTk.PhotoImage(Alterar_Cor("Images/Color-change.png", "#000000", cor))

    botao_icone_cor, botoes_cores, frame_botao_cor_personalizada, botao_cor_personalizada = Botoes_Cores(imagem_cor)

    label_auto_aceitar = tk.Label(root, font=("Arial", 18), bg="#191919", fg=cor)
    label_auto_aceitar.pack()

    def AbrirJanela():
        [window for window in gw.getWindowsWithTitle(root.title()) if window.title == root.title()][0].minimize()
        [window for window in gw.getWindowsWithTitle(root.title()) if window.title == root.title()][0].restore()
        [window for window in gw.getWindowsWithTitle(root.title()) if window.title == root.title()][0].activate()
    root.after(10, AbrirJanela)

    icone = Image.open("Images/icon.ico")
    icone = icone.resize((16, 16))
    icone = ImageTk.PhotoImage(icone)

    frame_barra_de_titulo, label_icone, label_titulo = Criar_Barra_de_Titulo(icone)

    global botao_fechar
    botao_fechar = BotaoFechar()    

    global botao_minimizar
    botao_minimizar = BotaoMinimizar()

    global botao_doacao, imagem_doacao
    imagem_doacao = ImageTk.PhotoImage(Alterar_Cor("Images/Doacao.png", "#ef9ba0", "#f1f1f1"))
    botao_doacao = BotaoDoacao()
    
    MoverJanela()
    frame_topo_janela, frame_esquerda_janela, frame_direita_janela, frame_base_janela = BordaJanela()

    tela_selecao_de_modo(jogo_está_aberto)
    root.mainloop()