import pyautogui
import pygetwindow as gw
import time
import tkinter as tk
import os
import threading
from utils.Encontrar_Pasta import *
from utils.Idioma import definir_idioma
from utils.Centralizar_Janela import centralizar_janela
from utils.Atualizacoes import Verificar_Atualizacoes
from utils.Fechar_Janela import fechar_janela

jogo_está_aberto = False

def tela_selecao_de_modo():
    global tela, Role_1, Role_2, modo_de_jogo, roles, jogo_está_aberto
    tela = "seleção de modo de jogo"
    modo_de_jogo=None
    Role_1=None
    Role_2=None
    frame_botoes_roles.pack_forget()
    frame_botoes_roles.place_forget()
    label_auto_aceitar.pack_forget()
    label_auto_aceitar.place_forget()
    frame_botoes_idiomas.pack_forget()
    frame_botoes_idiomas.place_forget()

    if idioma=="Portugues":
        modos_de_jogo=["Escolha alternada", "Ranqueada solo duo", "ARAM", "Blitz do Nexus", "Arena", "URF", "Todos por um", "Apenas auto aceitar"]
    elif idioma=="English":
        modos_de_jogo=["Draft pick", "Ranked solo duo", "ARAM", "Nexus Blitz", "Arena", "URF", "One for all", "Just auto accept"]

    for i in range(len(botoes_modos_de_jogo)):
        botoes_modos_de_jogo[i].config(text=modos_de_jogo[i], command=lambda t=modos_de_jogo[i]: Atualizar_Modo_de_Jogo(t))

    try:
        botao_icone_idioma.pack()
        botao_icone_idioma.place(relx=0.8915, rely=0.016)
    except: None
    frame_borda_topo.pack()
    frame_borda_topo.place(relx=0.4988888888888888, rely=0.052, anchor="center")
    label_borda_topo.pack()
    frame_borda_inferior.pack()
    frame_borda_inferior.place(relx=0.4988888888888888, rely=0.953, anchor="center")
    frame_botao_desfazer.pack()
    frame_botao_desfazer.place(relx=0.0275, rely=0.98, anchor="sw")
    frame_botao_confirmar.pack()
    frame_botao_confirmar.place(relx=0.9745, rely=0.98, anchor="se")
    frame_botoes_modos_de_jogo.pack()
    frame_botoes_modos_de_jogo.place(relx=0.0275, rely=0.095)
    if idioma=="Portugues":
        label_borda_topo.config(text="Escolha o modo de jogo")
        texto_inferior.set("Modo de jogo\nescolhido:")
        botao_desfazer.config(text="Desfazer")
        botao_confirmar.config(text="Confirmar")
    elif idioma=="English":
        label_borda_topo.config(text="Select game mode")
        texto_inferior.set("Selected game\nmode:")
        botao_desfazer.config(text="Undo")
        botao_confirmar.config(text="Confirm")
    centralizar_janela(root, 378, 476)
    def Jogo_Aberto():
        global modo_de_jogo, jogo_está_aberto
        while True:
            if jogo_está_aberto == False:
                return
            #time.sleep(30)
            if not [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"] and jogo_está_aberto == True:
                if idioma == "Portugues":
                    modo_de_jogo = "Apenas auto aceitar"
                elif idioma == "English":
                    modo_de_jogo = "Just auto accept"
                jogo_está_aberto = False
                tela_auto_aceitar() 
                return

    if jogo_está_aberto == True:
        thread_jogo_aberto = threading.Thread(target=Jogo_Aberto)
        thread_jogo_aberto.daemon = True
        thread_jogo_aberto.start()

def tela_selecao_de_role():
    global tela, botoes_roles, roles
    tela = "seleção de role"
    frame_botoes_modos_de_jogo.pack_forget()
    frame_botoes_modos_de_jogo.place_forget()
    botao_icone_idioma.pack_forget()
    botao_icone_idioma.place_forget()

    frame_botoes_roles.pack()
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
        frame_botoes_roles.place(relx=0.0275, rely=0.2075)
        frame_botao_desfazer.place(rely=0.9564)
        frame_botao_confirmar.place(rely=0.9564)
        frame_borda_topo.place(relx=0.4988888888888888, rely=0.115, anchor="center")
        frame_borda_inferior.place(relx=0.4988888888888888, rely=0.902, anchor="center")
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

        botoes_roles = [tk.Button(frame_botoes_roles, text=texto2, command=lambda t=texto2: Atualizar_Roles(t)) for texto2 in roles]
        for botao in botoes_roles:
            botao.config(width=50, height=2, bg="#1f1f1f", fg="#f0f0f0", bd=1)
            botao.pack(pady=5)

        centralizar_janela(root, 378, 235)
    else:
        frame_botoes_roles.place(relx=0.0275, rely=0.1235)
        frame_botao_desfazer.place(rely=0.974)
        frame_botao_confirmar.place(rely=0.974)
        frame_borda_inferior.place(relx=0.4988888888888888, rely=0.943, anchor="center")
        frame_borda_topo.place(relx=0.4988888888888888, rely=0.068, anchor="center")
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
        botoes_roles = [tk.Button(frame_botoes_roles, text=texto2, command=lambda t=texto2: Atualizar_Roles(t)) for texto2 in roles]

        for botao in botoes_roles:
            botao.config(width=50, height=2, bg="#1f1f1f", fg="#f0f0f0", bd=1)
            botao.pack(pady=5)

        centralizar_janela(root, 378, 380)            

def tela_auto_aceitar():
    global tela, jogo_está_aberto

    if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
        jogo_está_aberto = True

    tela="auto aceitar"
    frame_borda_topo.pack_forget()
    frame_borda_topo.place_forget()
    frame_botoes_modos_de_jogo.pack_forget()
    frame_botoes_modos_de_jogo.place_forget()
    frame_botoes_roles.pack_forget()
    frame_botoes_roles.place_forget()
    frame_botao_confirmar.pack_forget()
    frame_botao_confirmar.place_forget()
    frame_borda_inferior.pack_forget()
    frame_borda_inferior.place_forget()
    botao_icone_idioma.pack_forget()
    botao_icone_idioma.place_forget()

    label_auto_aceitar.pack()
    label_auto_aceitar.place(relx=0.4988888888888888, rely=0.315, anchor="center")
    
    if idioma=="Portugues":
        botao_desfazer.config(text="Menu principal")
    elif idioma=="English":
        botao_desfazer.config(text="Main menu")
    frame_botao_desfazer.place(relx=0.4988888888888888, rely=0.735, anchor="center")

    centralizar_janela(root, 375, 100)

    thread_imagem = threading.Thread(target=WhereToClick)
    thread_imagem.daemon = True
    thread_imagem.start()

    thread_mensagem = threading.Thread(target=atualizar_mensagem)
    thread_mensagem.daemon = True
    thread_mensagem.start()

def tela_alterar_idioma():
    global tela
    tela="alterar idioma"
    frame_borda_topo.pack_forget()
    frame_borda_topo.place_forget()
    frame_botoes_modos_de_jogo.pack_forget()
    frame_botoes_modos_de_jogo.place_forget()
    frame_botoes_roles.pack_forget()
    frame_botoes_roles.place_forget()
    frame_botao_confirmar.pack_forget()
    frame_botao_confirmar.place_forget()
    botao_icone_idioma.pack_forget()
    botao_icone_idioma.place_forget()

    frame_botoes_idiomas.pack()
    frame_botoes_idiomas.place(relx=0.0275, rely=0.03)

    frame_borda_inferior.pack()
    frame_borda_inferior.place(relx=0.4988888888888888, rely=0.678, anchor="center")
    if idioma=="Portugues":
        texto_inferior.set("Idioma selecionado: Português")
        botao_desfazer.config(text="Confirmar")
    elif idioma=="English":
        texto_inferior.set(f"Selected language: {idioma}")
        botao_desfazer.config(text="Confirm")

    frame_botao_desfazer.place(relx=0.4988888888888888, rely=0.873, anchor="center")

    altura_janela_idioma = 78 + len(lista_idiomas) * 49
    centralizar_janela(root, 378, altura_janela_idioma)

def atualizar_mensagem():
    if idioma=="Portugues":
        mensagens = "Encontrando partida"
        mensagens = [f"{mensagens}", f"{mensagens}"+".", f"{mensagens}"+"..", f"{mensagens}"+"..."]
    elif idioma=="English":
        mensagens = "Finding match"
        mensagens = [f"{mensagens}", f"{mensagens}"+".", f"{mensagens}"+"..", f"{mensagens}"+"..."]
    index = 0
    while True:
        if not tela=="auto aceitar":
            return
        try:
            label_auto_aceitar.config(text=mensagens[index])
            index = (index + 1) % len(mensagens)
            time.sleep(0.5)
        except:
            None

def confirmar():
    if idioma=="Portugues":
        if tela == "seleção de modo de jogo":
            if modo_de_jogo == "Apenas auto aceitar":
                root.after(500, lambda: tela_auto_aceitar() if modo_de_jogo == "Apenas auto aceitar" else None)
                if modo_de_jogo == "Apenas auto aceitar":
                    return

            if modo_de_jogo == None:
                texto_inferior.set("Selecione um modo de jogo!")
                root.after(2000, lambda: texto_inferior.set("Modo de jogo\nescolhido:") if modo_de_jogo == None else None)
            root.after(0, lambda: tela_auto_aceitar()
                        if modo_de_jogo == "ARAM"
                        or modo_de_jogo == "Arena"
                        or modo_de_jogo == "URF"
                        or modo_de_jogo == "Todos por um"
                        else tela_selecao_de_role() if modo_de_jogo is not None else None)
        elif tela == "seleção de role":
            if (modo_de_jogo != "Blitz do Nexus" and (Role_1 != "Preencher" and Role_2 == None)):
                texto_inferior.set("As duas roles devem\nser preenchidas!")
                if modo_de_jogo!="Blitz do Nexus":
                    root.after(2000, lambda: texto_inferior.set("Primeira role:\nSegunda role:") if tela=="seleção de role" and Role_1 == None else None)
                    root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role:") if tela=="seleção de role" and Role_2==None and Role_1 != None and Role_1 != "Preencher" else None)
                    root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role: {Role_2}") if tela=="seleção de role" and Role_1 != None and Role_2!=None else None)
                else: root.after(2000, lambda: texto_inferior.set("Posição escolhida:") if tela=="seleção de role" and Role_1 == None else None)
            elif modo_de_jogo== "Blitz do Nexus" and Role_1==None:
                texto_inferior.set("A role deve\nser preenchida!")
                root.after(2000, lambda: texto_inferior.set("Posição escolhida:") if tela=="seleção de role" and Role_1 == None else None)
            else:
                root.after(500, lambda: tela_auto_aceitar())

    elif idioma=="English":
        if tela == "seleção de modo de jogo":
            if modo_de_jogo == "Just auto accept":
                root.after(500, lambda: tela_auto_aceitar() if modo_de_jogo == "Just auto accept" else None)
                if modo_de_jogo == "Just auto accept":
                    return

            if modo_de_jogo == None:
                texto_inferior.set("Select a game mode!")
                root.after(2000, lambda: texto_inferior.set("Selected game\nmode:") if modo_de_jogo == None else None)
            root.after(0, lambda: tela_auto_aceitar()
                        if modo_de_jogo == "ARAM"
                        or modo_de_jogo == "Arena"
                        or modo_de_jogo == "URF"
                        or modo_de_jogo == "One for all"
                        else tela_selecao_de_role() if modo_de_jogo is not None else None)
        elif tela == "seleção de role":
            if (modo_de_jogo != "Nexus Blitz" and (Role_1 != "Fill" and Role_2 == None)):
                texto_inferior.set("Both roles must\nbe selected!")
                if modo_de_jogo!="Nexus Blitz":
                    root.after(2000, lambda: texto_inferior.set("First role:\nSecond role:") if tela=="seleção de role" and Role_1 == None else None)
                    root.after(2000, lambda: texto_inferior.set(f"First role: {Role_1}\nSecond role:") if tela=="seleção de role" and Role_2==None and Role_1 != None and Role_1 != "Fill" else None)
                    root.after(2000, lambda: texto_inferior.set(f"First role: {Role_1}\nSecond role: {Role_2}") if tela=="seleção de role" and Role_1 != None and Role_2!=None else None)
                else: root.after(2000, lambda: texto_inferior.set("Selected role:") if tela=="seleção de role" and Role_1 == None else None)
            elif modo_de_jogo== "Nexus Blitz" and Role_1==None:
                texto_inferior.set("The role must\nbe selected!")
                root.after(2000, lambda: texto_inferior.set("Selected role:") if tela=="seleção de role" and Role_1 == None else None)
            else:
                root.after(500, lambda: tela_auto_aceitar())

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
                modo_de_jogo = None
                jogo_está_aberto = False
                tela_selecao_de_modo()
        elif tela=="auto aceitar":
            modo_de_jogo=None
            Role_1=None
            Role_2=None
            jogo_está_aberto = False
            tela_selecao_de_modo()
        elif tela=="alterar idioma":
            modo_de_jogo=None
            Role_1=None
            Role_2=None
            tela_selecao_de_modo()
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
                modo_de_jogo = None
                jogo_está_aberto = False
                tela_selecao_de_modo()
        elif tela=="auto aceitar":
            modo_de_jogo=None
            Role_1=None
            Role_2=None
            jogo_está_aberto = False
            tela_selecao_de_modo()
        elif tela=="alterar idioma":
            modo_de_jogo=None
            Role_1=None
            Role_2=None
            tela_selecao_de_modo()

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
                root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role:") if tela=="seleção de role" and Role_2==None else None if Role_1 != None and Role_2==None else None)
                root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role: {Role_2}") if tela=="seleção de role" else None if Role_1 != None and Role_2!=None else None)
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
                root.after(2000, lambda: texto_inferior.set(f"First role: {Role_1}\nSecond role:") if tela=="seleção de role" and Role_2==None else None if Role_1 != None and Role_2==None else None)
                root.after(2000, lambda: texto_inferior.set(f"First role: {Role_1}\nSecond role: {Role_2}") if tela=="seleção de role" else None if Role_1 != None and Role_2!=None else None)
    
def Atualizar_Idioma(valor):
    global idioma
    idioma = valor.replace("ê", "e")
    caminho_idioma = os.path.join(os.path.expanduser("~"),"League_Lobby_Clicker_idioma-Saralapa.txt")
    with open(caminho_idioma, "w") as file:
        file.write(idioma)
    if idioma == "Portugues":
        botao_desfazer.config(text="Confirmar")
        texto_inferior.set(f"Idioma selecionado: {valor}")
    elif idioma == "English":
        botao_desfazer.config(text="Confirm")
        texto_inferior.set(f"Selected language: {valor}")

def KeepSearchingImageAndClickWhenFound(image):
    global jogo_está_aberto
    if not tela=="auto aceitar":
        return
    
    while True:
        if not tela=="auto aceitar":
            return
        if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
            jogo_está_aberto = True
            tela_selecao_de_modo()
            break
        try:
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image)
            image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

            if image_position_image:
                print(image)
                if image=="Aceitar.png":
                    janela_ativa=gw.getActiveWindow()               
                    mouse_position=pyautogui.position()
                    image_center = pyautogui.center(image_position_image)
                    pyautogui.click(image_center.x, image_center.y)
                    pyautogui.moveTo(mouse_position)
                    janela_ativa.activate()
                else:
                    image_center = pyautogui.center(image_position_image)
                    pyautogui.click(image_center.x, image_center.y) 
                break

            time.sleep(0.5)

        except: None

def SearchImageForXSecondsAndClickWhenFound(image, seconds):
    if not tela=="auto aceitar":
        return
    start_time = time.time()
    
    while (time.time() - start_time) < seconds:  
        if not tela=="auto aceitar":
            return
        try:
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image)
            image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

            if image_position_image:
                print(image)
                image_center = pyautogui.center(image_position_image)
                pyautogui.click(image_center.x, image_center.y)
                return 23

            time.sleep(0.5)

        except: None

def Role1(image):
    global jogo_está_aberto
    if not tela=="auto aceitar":
        return
    
    while True:
        if not tela=="auto aceitar":
            return
        try:
            if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                jogo_está_aberto = True
                tela_selecao_de_modo()
                break
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_Encontrar_partida = os.path.join("languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", "Encontrar partida.png")
            image_position_Encontrar_partida = pyautogui.locateOnScreen(image_path_Encontrar_partida, confidence=0.8)

            if image_position_Encontrar_partida:
                print(image_position_Encontrar_partida)
                image_center = pyautogui.center(image_position_Encontrar_partida)
                if lol_window.width==1600:
                    x_adjusted = image_center.x + 155  
                elif lol_window.width==1280:
                    x_adjusted = image_center.x + 124  
                elif lol_window.width==1024:
                    x_adjusted = image_center.x + 99   
                else:
                    root.destroy()
                    exit()
                pyautogui.click(x_adjusted, image_center.y)
                break

            time.sleep(0.5)

        except: None

    while True:
        if not tela=="auto aceitar":
            return
        try:
            if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                jogo_está_aberto = True
                tela_selecao_de_modo()
                break
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image+".png")
            image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

            if image_position_image:
                print(image)
                image_center = pyautogui.center(image_position_image)
                pyautogui.click(image_center.x, image_center.y)
                break

            time.sleep(0.5)

        except: None

    time.sleep(0.5)
    if image_path_image == os.path.join("languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", "Preencher" + ".png") or image_path_image == os.path.join("languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", "Fill" + ".png") :
        return 23

def Role2(image):
    global jogo_está_aberto
    if not tela=="auto aceitar":
        return
    
    while True:
        if not tela=="auto aceitar":
            return
        try:
            if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                jogo_está_aberto = True
                tela_selecao_de_modo()
                break
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_Encontrar_partida = os.path.join("languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", "Encontrar partida.png")
            image_position_Encontrar_partida = pyautogui.locateOnScreen(image_path_Encontrar_partida, confidence=0.8)

            if image_position_Encontrar_partida:
                print(image_position_Encontrar_partida)
                image_center = pyautogui.center(image_position_Encontrar_partida)
                if lol_window.width==1600:
                    x_adjusted = image_center.x + 200  
                elif lol_window.width==1280:
                    x_adjusted = image_center.x + 160  
                elif lol_window.width==1024:
                    x_adjusted = image_center.x + 128  
                else:
                    root.destroy()
                    exit()
                pyautogui.click(x_adjusted, image_center.y)
                break

            time.sleep(0.5)

        except: None

    while True:
        if not tela=="auto aceitar":
            return
        try:
            if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                jogo_está_aberto = True
                tela_selecao_de_modo()
                break
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("Languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image+".png")
            image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

            if image_position_image:
                print(image)
                image_center = pyautogui.center(image_position_image)
                pyautogui.click(image_center.x, image_center.y)
                break

            time.sleep(0.5)
            
        except: None

    time.sleep(0.5)

def WhereToClick():
    if not tela=="auto aceitar":
        return
    chamar_funcao_encontrar_pasta_LOL()
    if  modo_de_jogo!="Apenas auto aceitar" and modo_de_jogo!="Just auto accept":
        pyautogui.hotkey('alt', 'tab')
        janela_ativa = gw.getActiveWindow()
        pyautogui.hotkey('alt', 'tab')
        if not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
            
            while not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
                time.sleep(1)
        if not [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
            [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"][0].minimize()
            [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"][0].restore()
            KeepSearchingImageAndClickWhenFound("inicio.png")
            if SearchImageForXSecondsAndClickWhenFound("OK.png", 1) == 23:
                KeepSearchingImageAndClickWhenFound("inicio.png")
            if SearchImageForXSecondsAndClickWhenFound("grupo.png",1) == 23:
                KeepSearchingImageAndClickWhenFound("sair do grupo.png")
                SearchImageForXSecondsAndClickWhenFound("sair do grupo.png",1)
                SearchImageForXSecondsAndClickWhenFound("Sim.png", 1)
                time.sleep(0.5)
                SearchImageForXSecondsAndClickWhenFound("sair do grupo.png",1)
                KeepSearchingImageAndClickWhenFound("inicio.png")
            KeepSearchingImageAndClickWhenFound("Jogar.png")
            KeepSearchingImageAndClickWhenFound("PVP.png")
            if modo_de_jogo=="Escolha alternada" or modo_de_jogo=="Ranqueada solo duo":
                KeepSearchingImageAndClickWhenFound("Summoner's Rift.png")
            if not modo_de_jogo==None:
                KeepSearchingImageAndClickWhenFound(modo_de_jogo+".png")
            else:
                tela_selecao_de_modo()
                return
            time.sleep(0.5)
            KeepSearchingImageAndClickWhenFound("Confirmar.png")
            if modo_de_jogo!="ARAM" and modo_de_jogo!="Arena" and modo_de_jogo!="URF" and modo_de_jogo!="One for all" and modo_de_jogo !="Todos por um":
                if not Role_1==None:
                    if not Role1(Role_1)==23:
                        Role2(Role_2)
                else:
                    tela_selecao_de_modo()
                    return
            KeepSearchingImageAndClickWhenFound("Encontrar partida.png")
            time.sleep(2)
            janela_ativa.activate()
    while True:
        if not tela=="auto aceitar":
            return
        if not [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
            KeepSearchingImageAndClickWhenFound("Aceitar.png")
            time.sleep(5)
        else:
            tela_selecao_de_modo()
            return


root =tk.Tk()

root.title("League Lobby Clicker - Saralapa")
root.iconbitmap('icon.ico')
root.config(bg="#151515")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", lambda: fechar_janela(root))

frame_borda_topo = tk.LabelFrame(root, bg="#151515", width=210, height=30, bd=0)
frame_borda_topo.pack(side="top", anchor="center", pady=5)

label_borda_topo = tk.Label(frame_borda_topo, font=("Arial", 14), text="Escolha o modo de jogo", bg="#151515", fg="#f0f0f0", height=0)
label_borda_topo.pack()

modos_de_jogo = ["Escolha alternada", "Ranqueada solo duo", "ARAM", "Blitz do Nexus", "Arena", "URF", "Todos por um", "Apenas auto aceitar"]

frame_botoes_modos_de_jogo = tk.Frame(root, bg="#151515")

botoes_modos_de_jogo = [tk.Button(frame_botoes_modos_de_jogo, text=texto1, command=lambda t=texto1: Atualizar_Modo_de_Jogo(t)) for texto1 in modos_de_jogo]

for botao in botoes_modos_de_jogo:
    botao.config(width=50, height=2, bg="#1f1f1f", fg="#f0f0f0", bd=1)
    botao.pack(pady=5)

frame_botoes_modos_de_jogo.pack()

roles = ["Top", "Jungle", "Mid", "ADC", "Suporte", "Preencher"]

frame_botoes_roles = tk.Frame(root, bg="#151515")

botoes_roles = [tk.Button(frame_botoes_roles, text=texto2, command=lambda t=texto2: Atualizar_Roles(t)) for texto2 in roles]

for botao in botoes_roles:
    botao.config(width=50, height=2, bg="#1f1f1f", fg="#f0f0f0", bd=1)
    botao.pack(pady=5)

frame_botoes_roles.pack()

lista_idiomas = ["Português", "English"]

frame_botoes_idiomas = tk.Frame(root, bg="#151515")

botoes_idiomas = [tk.Button(frame_botoes_idiomas,text=texto3, command=lambda t=texto3: Atualizar_Idioma(t)) for texto3 in lista_idiomas]

for botao in botoes_idiomas:
    botao.config(width=50, height=2, bg="#1f1f1f", fg="#f0f0f0", bd=1)
    botao.pack(pady=5)

frame_botoes_idiomas.pack()

frame_borda_inferior = tk.LabelFrame(root, bg="#151515", width=210, height=30, bd=0)

texto_inferior = tk.StringVar(frame_borda_inferior)
texto_inferior.set("Modo de jogo\nescolhido:")

label_borda_inferior = tk.Label(frame_borda_inferior, textvariable=texto_inferior, bg="#151515", fg="#f0f0f0")
label_borda_inferior.pack()

frame_botao_desfazer = tk.Frame(root, bg="#151515", width=85, height=24, bd=0)
frame_botao_desfazer.pack()

botao_desfazer = tk.Button(frame_botao_desfazer, text="Desfazer", command=lambda: desfazer(), bg="#1f1f1f", fg="#f0f0f0", bd=1)
botao_desfazer.pack()

frame_botao_confirmar = tk.Frame(root, bg="#151515", width=65, height=24, bd=0)
frame_botao_confirmar.pack()

botao_confirmar = tk.Button(frame_botao_confirmar, text="Confirmar", command=lambda: confirmar(), bg="#1f1f1f", fg="#f0f0f0", bd=1)
botao_confirmar.pack()

imagem_idioma = tk.PhotoImage(file="Language.png")
try:
    botao_icone_idioma = tk.Button(root, image=imagem_idioma, command=tela_alterar_idioma, bd=0, bg="#151515", width=31, height=31)
    botao_icone_idioma.pack()
except: None

label_auto_aceitar = tk.Label(root, font=("Arial", 18), bg="#151515", fg="#f0f0f0")
label_auto_aceitar.pack()

idioma = definir_idioma()
chamar_funcao_encontrar_pasta_LOL()
tela_selecao_de_modo()
Verificar_Atualizacoes()
root.mainloop()