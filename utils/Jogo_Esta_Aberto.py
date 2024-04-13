import time
import pygetwindow as gw

def Jogo_Aberto():
    from main import modo_de_jogo, jogo_está_aberto, idioma, tela_auto_aceitar
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