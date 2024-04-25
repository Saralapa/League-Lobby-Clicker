import os

def definir_idioma():
    caminho_idioma = os.path.join(os.path.expanduser("~"),"League Lobby Clicker - Saralapa", "League_Lobby_Clicker_idioma-Saralapa.txt")
    if os.path.exists(caminho_idioma):
        try:
            with open(caminho_idioma, "r") as file:
                idioma = file.read()
        except:
            None
    else:
        try:
            with open(caminho_idioma, "w") as file:
                file.write("Portugues")
            with open(caminho_idioma, "r") as file:
                idioma = file.read()
        except:
            None
    return idioma