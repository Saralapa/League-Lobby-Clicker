import pyautogui
import pygetwindow as gw
import os
import time
import threading
from utils.Encontrar_Pasta import chamar_funcao_encontrar_pasta_LOL

def KeepSearchingImageAndClickWhenFound(image):
    from utils.Janela.Janela import idioma, tela
    if tela != "auto aceitar":
        return
    print("Procurando:", image)
    
    while True:
        from utils.Janela.Janela import tela
        if tela != "auto aceitar":
            return
        if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
            raise Exception("tela seleção de modo")
        elif not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
            raise
        try:
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("Images/languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image)
            image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

            if image_position_image:
                print("Clicou em:", image)
                if image == "Aceitar.png":
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
    from utils.Janela.Janela import idioma, tela
    if tela != "auto aceitar":
        return
    print("Procurando:", image)
    start_time = time.time()
    
    while (time.time() - start_time) < seconds:
        from utils.Janela.Janela import tela
        if tela != "auto aceitar":
            return
        try:
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("Images/languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image)
            image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

            if image_position_image:
                print("Clicou em:", image)
                image_center = pyautogui.center(image_position_image)
                pyautogui.click(image_center.x, image_center.y)
                return 23

            time.sleep(0.5)

        except: None

def Role1(image):
    from utils.Janela.Janela import idioma, tela
    if tela != "auto aceitar":
        return
    print("Procurando seleção de role 1")
    
    while True:
        from utils.Janela.Janela import tela
        if tela != "auto aceitar":
            return
        
        if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
            raise Exception("tela seleção de modo")
        elif not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
            raise
        try:
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_Encontrar_partida = os.path.join("Images/languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", "Encontrar partida.png")
            image_position_Encontrar_partida = pyautogui.locateOnScreen(image_path_Encontrar_partida, confidence=0.8)

            if image_position_Encontrar_partida:
                print("Clicou na seleção de role 1")
                image_center = pyautogui.center(image_position_Encontrar_partida)
                if lol_window.width==1600:
                    x_adjusted = image_center.x + 155  
                elif lol_window.width==1280:
                    x_adjusted = image_center.x + 124  
                elif lol_window.width==1024:
                    x_adjusted = image_center.x + 99
                pyautogui.click(x_adjusted, image_center.y)
                break

            time.sleep(0.5)

        except: None
    
    print("Procurando:", image)

    while True:
        from utils.Janela.Janela import tela
        if tela != "auto aceitar":
            return
        if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
            raise Exception("tela seleção de modo")
        elif not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
            raise
        try:
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("Images/languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image+".png")
            image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

            if image_position_image:
                print("Clicou em:", image)
                image_center = pyautogui.center(image_position_image)
                pyautogui.click(image_center.x, image_center.y)
                break

            time.sleep(0.5)

        except: None

    time.sleep(0.5)
    if image in ["Preencher", "Fill"]:
        return 23

def Role2(image):
    from utils.Janela.Janela import idioma, tela
    if tela != "auto aceitar":
        return
    print("Procurando seleção de role 2")
    
    while True:
        from utils.Janela.Janela import tela
        if tela != "auto aceitar":
            return
        if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
            raise Exception("tela seleção de modo")
        elif not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
            raise
        try:
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_Encontrar_partida = os.path.join("Images/languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", "Encontrar partida.png")
            image_position_Encontrar_partida = pyautogui.locateOnScreen(image_path_Encontrar_partida, confidence=0.8)

            if image_position_Encontrar_partida:
                print("Clicou na seleção de role 2")
                image_center = pyautogui.center(image_position_Encontrar_partida)
                if lol_window.width==1600:
                    x_adjusted = image_center.x + 200  
                elif lol_window.width==1280:
                    x_adjusted = image_center.x + 160  
                elif lol_window.width==1024:
                    x_adjusted = image_center.x + 128
                pyautogui.click(x_adjusted, image_center.y)
                break

            time.sleep(0.5)

        except: None

    print("Procurando:", image)

    while True:
        from utils.Janela.Janela import tela
        if tela != "auto aceitar":
            return
        if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
            raise Exception("tela seleção de modo")
        elif not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
            raise
        try:
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("Images/Languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image+".png")
            image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

            if image_position_image:
                print("Clicou em:", image)
                image_center = pyautogui.center(image_position_image)
                pyautogui.click(image_center.x, image_center.y)
                break

            time.sleep(0.5)
            
        except: None

    time.sleep(0.5)

def WhereToClick():
    from utils.Janela.Janela import modo_de_jogo, tela, tela_selecao_de_modo, Role_1, Role_2, jogo_está_aberto
    if tela != "auto aceitar":
        return
    try:
        for _ in range (3):
            if [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
                break
            chamar_funcao_encontrar_pasta_LOL()
            time.sleep(5)
        if modo_de_jogo.lower() not in ["Apenas auto aceitar", "Just auto accept"]:
            pyautogui.hotkey('alt', 'tab')
            janela_ativa = gw.getActiveWindow()
            pyautogui.hotkey('alt', 'tab')
            while not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
                time.sleep(1)
                if tela != "auto aceitar":
                    return
            if not [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"][0].minimize()
                [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"][0].restore()
                [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"][0].activate()
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
                if modo_de_jogo.lower() in ["escolha alternada", "ranqueada solo duo", "draft pick", "ranked solo duo"]:
                    KeepSearchingImageAndClickWhenFound("Summoner's Rift.png")
                if modo_de_jogo == None:
                    tela_selecao_de_modo(jogo_está_aberto)
                    return
                KeepSearchingImageAndClickWhenFound(modo_de_jogo+".png")
                time.sleep(0.5)
                KeepSearchingImageAndClickWhenFound("Confirmar.png")
                if not modo_de_jogo.lower() in ["aram", "arena", "urf", "one for all", "todos por um"]:
                    if Role_1 == None:
                        tela_selecao_de_modo(jogo_está_aberto)
                        return
                    if Role1(Role_1) != 23:
                        Role2(Role_2)
                KeepSearchingImageAndClickWhenFound("Encontrar partida.png")
                from utils.Janela.Janela import tela
                if tela == "auto aceitar":
                    time.sleep(2)
                    print("Eu vou ativar", janela_ativa)
                    janela_ativa.activate()
        while True:
            from utils.Janela.Janela import tela, jogo_está_aberto
            if tela != "auto aceitar":
                jogo_está_aberto = False
                tela_selecao_de_modo(jogo_está_aberto)
                return
            if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                jogo_está_aberto = True
                thread_tela_selecao_de_modo = threading.Thread(target=lambda: tela_selecao_de_modo(jogo_está_aberto))
                thread_tela_selecao_de_modo.daemon = True
                thread_tela_selecao_de_modo.start()
                return
            KeepSearchingImageAndClickWhenFound("Aceitar.png")
            time.sleep(5)
    except Exception as e:
        if e.args[0] == "tela seleção de modo":
            jogo_está_aberto = True
            thread_tela_selecao_de_modo = threading.Thread(target=lambda: tela_selecao_de_modo(jogo_está_aberto))
            thread_tela_selecao_de_modo.daemon = True
            thread_tela_selecao_de_modo.start()
            return
        
        print("Cliente fechado. Reinciando...")
        thread_Cliques = threading.Thread(target=WhereToClick)
        thread_Cliques.daemon = True
        thread_Cliques.start()
        return