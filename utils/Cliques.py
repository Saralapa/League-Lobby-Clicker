import pyautogui
import pygetwindow as gw
import os
import time
from utils.Encontrar_Pasta import chamar_funcao_encontrar_pasta_LOL

aux = False
def KeepSearchingImageAndClickWhenFound(image):
    global jogo_está_aberto, aux
    from utils.Janela import tela_selecao_de_modo, idioma, tela_auto_aceitar
    if not tela == "auto aceitar" or aux == True:
        return
    print("Procurando:", image)
    
    while True:
        if not tela == "auto aceitar" or aux == True:
            return
        if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
            jogo_está_aberto = True
            tela_selecao_de_modo()
            break
        else:
            while not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
                aux = True
                chamar_funcao_encontrar_pasta_LOL()
                time.sleep(10)
            if aux:
                return
        try:
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("Images", "Languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image)
            image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

            if image_position_image:
                print("Clicou em:", image)
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
    from utils.Janela import idioma
    if not tela == "auto aceitar" or aux == True:
        return
    print("Procurando:", image)
    start_time = time.time()
    
    while (time.time() - start_time) < seconds:  
        if not tela == "auto aceitar" or aux == True:
            return
        try:
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("Images", "Languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image)
            image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

            if image_position_image:
                print("Clicou em:", image)
                image_center = pyautogui.center(image_position_image)
                pyautogui.click(image_center.x, image_center.y)
                return 23

            time.sleep(0.5)

        except: None

def Role1(image):
    global jogo_está_aberto, aux
    from utils.Janela import tela_selecao_de_modo, idioma, root, tela_auto_aceitar
    if not tela == "auto aceitar" or aux == True:
        return
    print("Procurando:", image)
    
    while True:
        if not tela == "auto aceitar" or aux == True:
            return
        try:
            if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                jogo_está_aberto = True
                tela_selecao_de_modo()
                break
            else:
                while not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
                    aux = True
                    chamar_funcao_encontrar_pasta_LOL()
                    time.sleep(10)
                if aux:
                    return
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_Encontrar_partida = os.path.join("Images", "Languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", "Encontrar partida.png")
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
                else:
                    root.destroy()
                    exit()
                pyautogui.click(x_adjusted, image_center.y)
                break

            time.sleep(0.5)

        except: None

    while True:
        if not tela == "auto aceitar" or aux == True:
            return
        try:
            if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                jogo_está_aberto = True
                tela_selecao_de_modo()
                break
            else:
                while not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
                    aux = True
                    chamar_funcao_encontrar_pasta_LOL()
                    time.sleep(10)
                if aux:
                    return
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("Images", "Languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image+".png")
            image_position_image = pyautogui.locateOnScreen(image_path_image, confidence=0.8)

            if image_position_image:
                print("Clicou em:", image)
                image_center = pyautogui.center(image_position_image)
                pyautogui.click(image_center.x, image_center.y)
                break

            time.sleep(0.5)

        except: None

    time.sleep(0.5)
    if image_path_image == os.path.join("Images", "Languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", "Preencher" + ".png") or image_path_image == os.path.join("Images", "Languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", "Fill" + ".png") :
        return 23

def Role2(image):
    global jogo_está_aberto, aux
    from utils.Janela import tela_selecao_de_modo, idioma, root, tela_auto_aceitar
    if not tela == "auto aceitar" or aux == True:
        return
    print("Procurando:", image)
    
    while True:
        if not tela == "auto aceitar" or aux == True:
            return
        try:
            if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                jogo_está_aberto = True
                tela_selecao_de_modo()
                break
            else:
                while not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
                    aux = True
                    chamar_funcao_encontrar_pasta_LOL()
                    time.sleep(10)
                if aux:
                    return
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_Encontrar_partida = os.path.join("Images", "Languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", "Encontrar partida.png")
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
                else:
                    root.destroy()
                    exit()
                pyautogui.click(x_adjusted, image_center.y)
                break

            time.sleep(0.5)

        except: None

    while True:
        if not tela == "auto aceitar" or aux == True:
            return
        try:
            if [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
                jogo_está_aberto = True
                tela_selecao_de_modo()
                break
            else:
                while not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
                    aux = True
                    chamar_funcao_encontrar_pasta_LOL()
                    time.sleep(10)
                if aux:
                    return
            lol_window = gw.getWindowsWithTitle('League of Legends')[0]
            image_path_image = os.path.join("Images", "Languages", idioma, "Images"+f" {lol_window.width}x{lol_window.height}", image+".png")
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
    global tela, aux
    from utils.Janela import modo_de_jogo, tela, tela_selecao_de_modo, Role_1, Role_2
    aux = False
    if not tela == "auto aceitar":
        return
    while not [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"]:
        chamar_funcao_encontrar_pasta_LOL()
        time.sleep(10)
    if  modo_de_jogo!="Apenas auto aceitar" and modo_de_jogo!="Just auto accept":
        pyautogui.hotkey('alt', 'tab')
        janela_ativa = gw.getActiveWindow()
        pyautogui.hotkey('alt', 'tab')
        if not [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
            [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"][0].minimize()
            [window for window in gw.getWindowsWithTitle("League of Legends") if window.title == "League of Legends"][0].restore()
            KeepSearchingImageAndClickWhenFound("inicio.png")
            if aux == True:
                WhereToClick()
                return
            if SearchImageForXSecondsAndClickWhenFound("OK.png", 1) == 23:
                KeepSearchingImageAndClickWhenFound("inicio.png")
                if aux == True:
                    WhereToClick()
                    return
            if SearchImageForXSecondsAndClickWhenFound("grupo.png",1) == 23:
                KeepSearchingImageAndClickWhenFound("sair do grupo.png")
                if aux == True:
                    WhereToClick()
                    return
                SearchImageForXSecondsAndClickWhenFound("sair do grupo.png",1)
                SearchImageForXSecondsAndClickWhenFound("Sim.png", 1)
                time.sleep(0.5)
                SearchImageForXSecondsAndClickWhenFound("sair do grupo.png",1)
                KeepSearchingImageAndClickWhenFound("inicio.png")
                if aux == True:
                    WhereToClick()
                    return
            KeepSearchingImageAndClickWhenFound("Jogar.png")
            if aux == True:
                WhereToClick()
                return
            KeepSearchingImageAndClickWhenFound("PVP.png")
            if aux == True:
                WhereToClick()
                return
            if modo_de_jogo=="Escolha alternada" or modo_de_jogo=="Ranqueada solo duo":
                KeepSearchingImageAndClickWhenFound("Summoner's Rift.png")
                if aux == True:
                    WhereToClick()
                    return
            if not modo_de_jogo==None:
                KeepSearchingImageAndClickWhenFound(modo_de_jogo+".png")
                if aux == True:
                    WhereToClick()
                    return
            else:
                tela_selecao_de_modo()
                return
            time.sleep(0.5)
            KeepSearchingImageAndClickWhenFound("Confirmar.png")
            if aux == True:
                WhereToClick()
                return
            if modo_de_jogo!="ARAM" and modo_de_jogo!="Arena" and modo_de_jogo!="URF" and modo_de_jogo!="One for all" and modo_de_jogo !="Todos por um":
                if not Role_1==None:
                    if not Role1(Role_1)==23:
                        if aux == True:
                            WhereToClick()
                            return
                        Role2(Role_2)
                        if aux == True:
                            WhereToClick()
                            return
                    if aux == True:
                        WhereToClick()
                        return
                else:
                    tela_selecao_de_modo()
                    return
            KeepSearchingImageAndClickWhenFound("Encontrar partida.png")
            if aux == True:
                WhereToClick()
                return
            time.sleep(2)
            janela_ativa.activate()
    while True:
        if not tela == "auto aceitar":
            return
        if not [window for window in gw.getWindowsWithTitle("League of Legends (TM) Client") if window.title == "League of Legends (TM) Client"]:
            KeepSearchingImageAndClickWhenFound("Aceitar.png")
            if aux == True:
                WhereToClick()
                return
            time.sleep(5)
        else:
            tela_selecao_de_modo()
            return