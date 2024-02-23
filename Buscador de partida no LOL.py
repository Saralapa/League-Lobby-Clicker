from tkinter import messagebox
import webbrowser
import requests
import pyautogui
import subprocess
import pygetwindow as gw
import time
import tkinter as tk
import os
import threading

# Variáveis globais
tela = "game mode selection"
Role_1 = None
Role_2 = None
modo_de_jogo = None
versao_atual = "1.5"

def encontrar_e_salvar_pasta_instalacao_lol(unidade, flagPF):
    unidade=unidade+"\\"  # Adiciona uma barra invertida ao final da unidade se necessário
    global pasta_instalacao  # Declara a variável como global
    pasta_instalacao=None

    if flagPF==1:  # Verifica a flag para determinar a abordagem a ser utilizada
        # Verifica os possíveis diretórios padrão de instalação do League of Legends
        pastas_padrao = rf"{unidade}\Riot Games\League of Legends"

        for pasta in pastas_padrao:  # Itera sobre os possíveis diretórios padrão
            if os.path.exists(pastas_padrao):  # Verifica se o diretório existe
                pasta_instalacao=pastas_padrao  # Define a pasta de instalação
                pasta_instalacao = os.path.dirname(pasta_instalacao)  # Obtém o diretório pai
                pasta_instalacao = os.path.join(pasta_instalacao, "Riot Client", "RiotClientServices.exe")  # Junta o caminho até o executável do cliente da Riot
                pasta_instalacao = pasta_instalacao.replace("\\\\", "\\")  # Substitui "\\" por "\"

                LOL_path = os.path.join(os.path.expanduser("~"),"league_of_legends_path.txt")  # Caminho para o arquivo de texto que armazenará o caminho do League of Legends
                LOL_path = LOL_path.replace("\\\\", "\\")  # Substitui "\\" por "\"
                with open(LOL_path, 'w') as arquivo:  # Abre o arquivo em modo de escrita
                    arquivo.write(pasta_instalacao)  # Escreve o caminho da pasta de instalação

                if pasta_instalacao:  # Verifica se a pasta de instalação foi encontrada
                    return 23  # Retorna 23 se a pasta for encontrada
                else:
                    return  # Retorna vazio se não encontrou

        # Se não encontrar em nenhum dos diretórios padrão, busca recursivamente por toda a unidade
        for pasta, subpastas, arquivos in os.walk(unidade):  # Itera por todos os diretórios e arquivos na unidade
            if "Program Files" in pasta or "ProgramData" in pasta or "AppData" in pasta or "Windows" in pasta:  # Ignora alguns diretórios específicos
                del subpastas[:]  # Exclui as subpastas para evitar a busca nelas
                continue
            if "League of Legends" in subpastas and "Riot Games" in pasta:  # Verifica a existência do diretório "League of Legends" dentro de "Riot Games"
                pasta_instalacao = os.path.join(pasta, "Riot Client", "RiotClientServices.exe")  # Caminho até o executável do cliente da Riot
                pasta_instalacao = pasta_instalacao.replace(f"{unidade}",f"{unidade}\\")  # Corrige o caminho

                LOL_path = os.path.join(os.path.expanduser("~"),"league_of_legends_path.txt")  # Caminho para o arquivo de texto que armazenará o caminho do League of Legends
                LOL_path = LOL_path.replace("\\\\", "\\")  # Substitui "\\" por "\"
                with open(LOL_path, 'w') as arquivo:  # Abre o arquivo em modo de escrita
                    arquivo.write(pasta_instalacao)  # Escreve o caminho da pasta de instalação

                return 23  # Retorna 23 se a pasta for encontrada
            
            if pasta_instalacao:  # Verifica se a pasta de instalação foi encontrada
                return  # Retorna vazio se não encontrou

        if not pasta_instalacao:  # Se a pasta de instalação não for encontrada
            print("A pasta de instalação do League of Legends não foi encontrada.")  # Imprime uma mensagem de aviso
    
    elif flagPF==2:  # Verifica a flag para determinar a abordagem a ser utilizada
        for pasta, subpastas, arquivos in os.walk(unidade):  # Itera por todos os diretórios e arquivos na unidade
            print(pasta, subpastas, arquivos)  # Imprime os diretórios, subdiretórios e arquivos (utilizado para debug)

            if "Riot Client" in subpastas and "League of Legends" in subpastas:  # Verifica a existência dos diretórios "Riot Client" e "League of Legends"
                riot_client_index = subpastas.index("Riot Client")  # Obtém o índice do diretório "Riot Client"
                lol_index = subpastas.index("League of Legends")  # Obtém o índice do diretório "League of Legends"

                if lol_index == riot_client_index + 1:  # Verifica se "League of Legends" está dentro de "Riot Client"
                    pasta_instalacao = os.path.join(pasta, "Riot Client", "RiotClientServices.exe")  # Caminho até o executável do cliente da Riot
                    pasta_instalacao = pasta_instalacao.replace(f"{unidade}", f"{unidade}\\")  # Corrige o caminho

                    LOL_path = os.path.join(os.path.expanduser("~"),"league_of_legends_path.txt")  # Caminho para o arquivo de texto que armazenará o caminho do League of Legends
                    LOL_path = LOL_path.replace("\\\\", "\\")  # Substitui "\\" por "\"
                    with open(LOL_path, 'w') as arquivo:  # Abre o arquivo em modo de escrita
                        arquivo.write(pasta_instalacao)  # Escreve o caminho da pasta de instalação

                    return 23  # Retorna 23 se a pasta for encontrada
            
            if pasta_instalacao:  # Verifica se a pasta de instalação foi encontrada
                return  # Retorna vazio se não encontrou

        if not pasta_instalacao:  # Se a pasta de instalação não for encontrada
            print("A pasta de instalação do League of Legends não foi encontrada.")  # Imprime uma mensagem de aviso

def chamar_funcao_encontrar_pasta_LOL():
    unidades = [f"{disco}:" for disco in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{disco}:")]
    if not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
        LOL_path = os.path.join(os.path.expanduser("~"),"league_of_legends_path.txt")
        LOL_path = LOL_path.replace("\\\\", "\\")

        if os.path.exists(LOL_path):
            None
            
        else:
            for unidade in unidades:
                if encontrar_e_salvar_pasta_instalacao_lol(unidade, 1) == 23:
                    break
            if pasta_instalacao==None:
                for unidade in unidades:
                    if encontrar_e_salvar_pasta_instalacao_lol(unidade, 2) == 23:
                        break
            
        try:
            with open(LOL_path, "r") as file:
                subprocess.Popen([file.read().strip(), '--launch-product=league_of_legends', '--launch-patchline=live'])
        except:
            try:
                os.remove(LOL_path)
            except:
                None
            for unidade in unidades:
                if encontrar_e_salvar_pasta_instalacao_lol(unidade, 1) == 23:
                    break
            if pasta_instalacao==None:
                for unidade in unidades:
                    if encontrar_e_salvar_pasta_instalacao_lol(unidade, 2) == 23:
                        break
            time.sleep(0.5)
            try:
                with open(LOL_path, "r") as file:
                    subprocess.Popen([file.read().strip(), '--launch-product=league_of_legends', '--launch-patchline=live'])
            except:
                None

def LOL():
    global tela, Role_1, Role_2, modo_de_jogo, botoes_roles, roles

    def tela_selecao_de_modo():
        global tela, Role_1, Role_2, modo_de_jogo, roles
        tela = "game mode selection"
        modo_de_jogo=None
        Role_1=None
        Role_2=None
        frame_botoes_roles.pack_forget()
        frame_botoes_roles.place_forget()
        label_auto_aceitar.pack_forget()
        label_auto_aceitar.place_forget()

        frame_borda_inferior.pack()
        frame_borda_inferior.place(relx=0.4988888888888888, rely=0.9435, anchor="center")
        frame_borda_topo.pack()
        frame_borda_topo.place(relx=0.3235, rely=0.0125)
        label_borda_topo.config(bg="#151515")
        label_borda_topo.pack()
        frame_botao_desfazer.pack()
        frame_botao_desfazer.place(relx=0.0275, rely=0.9155)
        frame_botao_confirmar.pack()
        frame_botao_confirmar.place(relx=0.8065, rely=0.9155)
        frame_botoes_modos_de_jogo.pack()
        frame_botoes_modos_de_jogo.place(relx=0.0275, rely=0.0635)
        label_borda_topo.config(text="Escolha o modo de jogo")
        texto_inferior.set("Modo de jogo\nescolhido:")
        botao_desfazer.config(text="Desfazer")
        centralizar_janela(root, 378, 410)

    def tela_selecao_de_role():
        global tela, botoes_roles, roles
        tela = "role selection"
        frame_botoes_modos_de_jogo.pack_forget()
        frame_botoes_modos_de_jogo.place_forget()
        frame_botoes_roles.pack()
        label_borda_topo.config(text="Escolha em que posição você vai jogar")
        if Role_1 == None:
            botao_desfazer.config(text="Menu anterior")
        else:
            botao_desfazer.config(text="Desfazer")
        if modo_de_jogo == "Blitz do Nexus":
            frame_botoes_roles.place(relx=0.0275, rely=0.1235)
            frame_botao_desfazer.place(rely=0.836)
            frame_botao_confirmar.place(rely=0.836)
            frame_borda_topo.place(relx=0.2235, rely=0.0245)
            frame_borda_inferior.place(relx=0.4988888888888888, rely=0.89, anchor="center")
            texto_inferior.set("Posição escolhida:")
            for botao in botoes_roles:
                botao.destroy()
            roles = ["Jungle", "Rota", "Preencher"]
            botoes_roles = [tk.Button(frame_botoes_roles, text=texto2, command=lambda t=texto2: Atualizar_Roles(t)) for texto2 in roles]
            for botao in botoes_roles:
                botao.config(width=50, height=2, bg="#1f1f1f", fg="#f0f0f0", bd=1)
                botao.pack(pady=5)
            centralizar_janela(root, 378, 214)
        else:
            frame_botoes_roles.place(relx=0.0275, rely=0.071)
            frame_botao_desfazer.place(rely=0.902)
            frame_botao_confirmar.place(rely=0.902)
            frame_borda_topo.place(relx=0.2235, rely=0.0125)
            frame_borda_inferior.place(relx=0.4988888888888888, rely=0.937, anchor="center")
            texto_inferior.set(f"Primeira role:\nSegunda role:")
            for botao in botoes_roles:
                botao.destroy()
            roles = ["Top", "Jungle", "Mid", "ADC", "Suporte", "Preencher"]
            botoes_roles = [tk.Button(frame_botoes_roles, text=texto2, command=lambda t=texto2: Atualizar_Roles(t)) for texto2 in roles]
            for botao in botoes_roles:
                botao.config(width=50, height=2, bg="#1f1f1f", fg="#f0f0f0", bd=1)
                botao.pack(pady=5)
            centralizar_janela(root, 378, 361)            

    def tela_auto_aceitar():
        global tela, roles
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

        label_auto_aceitar.pack()
        label_auto_aceitar.place(relx=0.4988888888888888, rely=0.315, anchor="center")
        botao_desfazer.config(text="Menu principal")
        frame_botao_desfazer.place(relx=0.38175, rely=0.62)

        centralizar_janela(root, 375, 100)

        thread_imagem = threading.Thread(target=WhereToClick)
        thread_imagem.daemon = True
        thread_imagem.start()

        thread_mensagem = threading.Thread(target=atualizar_mensagem)
        thread_mensagem.daemon = True
        thread_mensagem.start()

    def centralizar_janela(root, width, height):
        global screen_width, screen_height, x, y, roles
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")
    
    def atualizar_mensagem():
        mensagens = ["Encontrando partida", "Encontrando partida.", "Encontrando partida..", "Encontrando partida..."]
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
        if tela == "game mode selection":
            if modo_de_jogo == "Apenas auto aceitar":
                root.after(500, lambda: tela_auto_aceitar() if modo_de_jogo == "Apenas auto aceitar" else None)
                if modo_de_jogo == "Apenas auto aceitar":
                    return

            if modo_de_jogo == None:
                texto_inferior.set("Selecione um modo de jogo!")
                root.after(2000, lambda: texto_inferior.set("Modo de jogo\nescolhido:") if modo_de_jogo == None else None)
            root.after(0, lambda: tela_auto_aceitar() if modo_de_jogo == "ARAM" or modo_de_jogo == "Arena" or modo_de_jogo == "URF" else tela_selecao_de_role() if modo_de_jogo is not None else None)
        elif tela == "role selection":
            if (modo_de_jogo != "Blitz do Nexus" and (Role_1 != "Preencher" and Role_2 == None)):
                texto_inferior.set("As duas roles devem\nser preenchidas!")
                if modo_de_jogo!="Blitz do Nexus":
                    root.after(2000, lambda: texto_inferior.set("Primeira role:\nSegunda role:") if tela=="role selection" and Role_1 == None else None)
                    root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role:") if tela=="role selection" and Role_2==None and Role_1 != None and Role_1 != "Preencher" else None)
                    root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role: {Role_2}") if tela=="role selection" and Role_1 != None and Role_2!=None else None)
                else: root.after(2000, lambda: texto_inferior.set("Posição escolhida:") if tela=="role selection" and Role_1 == None else None)
            elif modo_de_jogo== "Blitz do Nexus" and Role_1==None:
                texto_inferior.set("A role deve\nser preenchida!")
                root.after(2000, lambda: texto_inferior.set("Posição escolhida:") if tela=="role selection" and Role_1 == None else None)
            else:
                root.after(500, lambda: tela_auto_aceitar())

    def desfazer():
        global modo_de_jogo, tela, Role_1, Role_2, roles
        if tela == "game mode selection":
            modo_de_jogo = None
            texto_inferior.set("Modo de jogo\nescolhido:")
        elif tela == "role selection":
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
                tela_selecao_de_modo()
        elif tela=="auto aceitar":
            modo_de_jogo=None
            Role_1=None
            Role_2=None
            tela_selecao_de_modo()

    def Atualizar_Modo_de_Jogo(valor):
        global modo_de_jogo, roles
        modo_de_jogo = valor
        texto_inferior.set(f"Modo de jogo\nescolhido: {modo_de_jogo}")

    def Atualizar_Roles(valor):
        global Role_1, Role_2, roles
        if Role_1 == None or modo_de_jogo == "Blitz do Nexus":
            Role_1 = valor
            botao_desfazer.config(text="Desfazer")
            if modo_de_jogo != "Blitz do Nexus":
                if Role_1!="Preencher":
                    texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role:")
                    frame_borda_inferior.place(relx=0.4988888888888888, rely=0.937, anchor="center")
                    
                else:
                    texto_inferior.set(f"Role escolhida: {Role_1}")
                    frame_borda_inferior.place(relx=0.4988888888888888, rely=0.9335, anchor="center")
            else:
                texto_inferior.set(f"Posição escolhida: {Role_1}")
        elif Role_2 == None and Role_1 != "Preencher" and modo_de_jogo != "Blitz do Nexus":
            Role_2 = valor
            texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role: {Role_2}")
            if Role_1 == Role_2:
                Role_2 = None
                texto_inferior.set(f"A primeira e a segunda\nposição não podem ser iguais!")
                root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role:") if tela=="role selection" and Role_2==None else None if Role_1 != None and Role_2==None else None)
                root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role: {Role_2}") if tela=="role selection" else None if Role_1 != None and Role_2!=None else None)

    def fechar_janela():
        root.destroy()
        exit()
    
    def KeepSearchingImageAndClickWhenFound(image):
        if not tela=="auto aceitar":
            return
        
        while True:
            if not tela=="auto aceitar":
                return
            if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                tela_selecao_de_modo()
                break
            try:
                lol_window = gw.getWindowsWithTitle('League of Legends')[0]
                image_path_image = os.path.join("Images"+f" {lol_window.width}x{lol_window.height}", image)
                image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

                # If the image is found, click on it
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

                # Wait a short time before trying again
                time.sleep(0.5)

            except: None
    
    def SearchImageForXSecondsAndClickWhenFound(image, seconds):
        if not tela=="auto aceitar":
            return
        start_time = time.time()
     
        while (time.time() - start_time) < seconds:  # Keep searching for X seconds tops
            if not tela=="auto aceitar":
                return
            try:
                lol_window = gw.getWindowsWithTitle('League of Legends')[0]
                image_path_image = os.path.join("Images"+f" {lol_window.width}x{lol_window.height}", image)
                image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

                # If the image is found, click on it
                if image_position_image:
                    print(image)
                    image_center = pyautogui.center(image_position_image)
                    pyautogui.click(image_center.x, image_center.y)
                    return 23

                # Wait a short time before trying again
                time.sleep(0.5)

            except: None
    
    def Role1(image):
        if not tela=="auto aceitar":
            return
        
        while True:
            if not tela=="auto aceitar":
                return
            try:
                if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                    tela_selecao_de_modo()
                    break
                lol_window = gw.getWindowsWithTitle('League of Legends')[0]
                image_path_Encontrar_partida = os.path.join("Images"+f" {lol_window.width}x{lol_window.height}", "Encontrar partida.png")
                image_position_Encontrar_partida = pyautogui.locateOnScreen(image_path_Encontrar_partida, confidence=0.8)

                # If the image is found, click on it with x adjusted
                if image_position_Encontrar_partida:
                    image_center = pyautogui.center(image_position_Encontrar_partida)
                    if lol_window.width==1600:
                        x_adjusted = image_center.x + 155  # Ajuste a coordenada x aqui\
                    elif lol_window.width==1280:
                        x_adjusted = image_center.x + 124  # Ajuste a coordenada x aqui\
                    elif lol_window.width==1024:
                        x_adjusted = image_center.x + 99   # Ajuste a coordenada x aqui\
                    else:
                        root.destroy()
                        exit()
                    pyautogui.click(x_adjusted, image_center.y)
                    break

                # Wait a short time before trying again
                time.sleep(0.5)

            except: None

        while True:
            if not tela=="auto aceitar":
                return
            try:
                if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                    tela_selecao_de_modo()
                    break
                lol_window = gw.getWindowsWithTitle('League of Legends')[0]
                image_path_image = os.path.join("Images"+f" {lol_window.width}x{lol_window.height}", image+".png")
                image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

                # If the image is found, click on it
                if image_position_image:
                    image_center = pyautogui.center(image_position_image)
                    pyautogui.click(image_center.x, image_center.y)
                    break

                # Wait a short time before trying again
                time.sleep(0.5)

            except: None

        time.sleep(0.5)
        if (image_path_image == os.path.join("Images"+f" {lol_window.width}x{lol_window.height}", "Preencher" + ".png")):
            return 23
    
    def Role2(image):
        if not tela=="auto aceitar":
            return
        
        while True:
            if not tela=="auto aceitar":
                return
            try:
                if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                    tela_selecao_de_modo()
                    break
                lol_window = gw.getWindowsWithTitle('League of Legends')[0]
                image_path_Encontrar_partida = os.path.join("Images"+f" {lol_window.width}x{lol_window.height}", "Encontrar partida.png")
                image_position_Encontrar_partida = pyautogui.locateOnScreen(image_path_Encontrar_partida, confidence=0.8)

                # If the image is found, click on it with x adjusted
                if image_position_Encontrar_partida:
                    image_center = pyautogui.center(image_position_Encontrar_partida)
                    if lol_window.width==1600:
                        x_adjusted = image_center.x + 200  # Ajuste a coordenada x aqui
                    elif lol_window.width==1280:
                        x_adjusted = image_center.x + 160  # Ajuste a coordenada x aqui
                    elif lol_window.width==1024:
                        x_adjusted = image_center.x + 128  # Ajuste a coordenada x aqui
                    else:
                        root.destroy()
                        exit()
                    pyautogui.click(x_adjusted, image_center.y)
                    break

                # Wait a short time before trying again
                time.sleep(0.5)

            except: None

        while True:
            if not tela=="auto aceitar":
                return
            try:
                if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                    tela_selecao_de_modo()
                    break
                lol_window = gw.getWindowsWithTitle('League of Legends')[0]
                image_path_image = os.path.join("Images"+f" {lol_window.width}x{lol_window.height}", image+".png")
                image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

                # If the image is found, click on it
                if image_position_image:
                    image_center = pyautogui.center(image_position_image)
                    pyautogui.click(image_center.x, image_center.y)
                    break

                # Wait a short time before trying again
                time.sleep(0.5)
                
            except: None

        time.sleep(0.5)

    def WhereToClick():
        if not tela=="auto aceitar":
            return
        if not modo_de_jogo=="Apenas auto aceitar":
            pyautogui.hotkey('alt', 'tab')
            janela_ativa = gw.getActiveWindow()
            pyautogui.hotkey('alt', 'tab')
            if not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
                # Wait until the window is fully open
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
                if modo_de_jogo!="ARAM" and modo_de_jogo!="Arena" and modo_de_jogo!="URF":
                    if not Role_1==None:
                        if not Role1(Role_1)==23:
                            Role2(Role_2)
                    else:
                        tela_selecao_de_modo()
                        return
                KeepSearchingImageAndClickWhenFound("Encontrar partida.png")
                time.sleep(1)
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

    def Verificar_Atualizacoes():
        try:
            versao = requests.get("https://api.github.com/repos/Saralapa/Buscador-de-Partida-no-LOL/releases/latest")
            versao.raise_for_status()
            versao = versao.json()

            if versao["target_commitish"].replace("v","") != versao_atual:
                resposta = messagebox.askquestion("Atualização Disponível", f"Versão atual: {versao_atual}\nVersão mais recente: {versao['target_commitish'].replace("v","")}\n\n\nDeseja baixar agora?")
                if resposta == "yes":
                    webbrowser.open("https://github.com/Saralapa/Buscador-de-Partida-no-LOL/releases/latest")

        except requests.exceptions.RequestException as e:
            pass
    root =tk.Tk()

    root.title("Buscador de Partida no LOL - Saralapa")
    root.iconbitmap('icon.ico')
    root.config(bg="#151515")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", fechar_janela)
    
    frame_borda_topo = tk.LabelFrame(root, bg="#151515", width=210, height=30, bd=0)
    frame_borda_topo.pack(side="top", anchor="center", pady=5)

    label_borda_topo = tk.Label(frame_borda_topo, text="Escolha o modo de jogo", bg="#151515", fg="#f0f0f0", height=0)
    label_borda_topo.pack()

    lista_modos_de_jogo = ["Escolha alternada", "Ranqueada solo duo", "ARAM", "Blitz do Nexus", "Arena", "URF", "Apenas auto aceitar"]    
    roles = ["Top", "Jungle", "Mid", "ADC", "Suporte", "Preencher"]

    frame_botoes_modos_de_jogo = tk.Frame(root, bg="#151515")

    botoes_modos_de_jogo = [tk.Button(frame_botoes_modos_de_jogo, text=texto1, command=lambda t=texto1: Atualizar_Modo_de_Jogo(t)) for texto1 in lista_modos_de_jogo]

    for botao in botoes_modos_de_jogo:
        botao.config(width=50, height=2, bg="#1f1f1f", fg="#f0f0f0", bd=1)
        botao.pack(pady=5)

    frame_botoes_modos_de_jogo.pack()

    frame_botoes_roles = tk.Frame(root, bg="#151515")
    
    botoes_roles = [tk.Button(frame_botoes_roles, text=texto2, command=lambda t=texto2: Atualizar_Roles(t)) for texto2 in roles]

    for botao in botoes_roles:
        botao.config(width=50, height=2, bg="#1f1f1f", fg="#f0f0f0", bd=1)
        botao.pack(pady=5)

    frame_botoes_roles.pack()

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

    label_auto_aceitar = tk.Label(root, font=("Arial", 18), bg="#151515", fg="#f0f0f0")
    label_auto_aceitar.pack()

    x=378
    y=410
    root.geometry(f"{x}x{y}+{(root.winfo_screenwidth() - x) // 2}+{(root.winfo_screenheight() - y) // 2}")

    tela_selecao_de_modo()
    Verificar_Atualizacoes()
    root.mainloop()

chamar_funcao_encontrar_pasta_LOL()
LOL()