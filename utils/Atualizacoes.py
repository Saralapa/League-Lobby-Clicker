import requests
import webbrowser
from tkinter import messagebox
from utils.Idioma import definir_idioma

versao_atual = "3.0"

def Verificar_Atualizacoes():
    try:
        idioma = definir_idioma()
        versao = requests.get("https://api.github.com/repos/Saralapa/League-Lobby-Clicker/releases/latest")
        versao.raise_for_status()
        versao = versao.json()

        if versao["tag_name"].replace("v","") != versao_atual:
            if idioma=="Portugues":
                resposta = messagebox.askquestion("Atualização Disponível", f"Versão atual: {versao_atual}\nVersão mais recente: {versao['tag_name'].replace("v","")}\n\n\nDeseja baixar agora?")
            elif idioma=="English":
                resposta = messagebox.askquestion("Update Available", f"Current version: {versao_atual}\nLatest Version: {versao['tag_name'].replace("v","")}\n\n\nDownload now?")
            if resposta == "yes":
                webbrowser.open("https://github.com/Saralapa/League-Lobby-Clicker/releases/latest")
    except: None