from PIL import Image
import os

def Definir_Cor():
    caminho_cor = os.path.join(os.path.expanduser("~"),"League_Lobby_Clicker_cor-Saralapa.txt")
    if os.path.exists(caminho_cor):
        try:
            with open(caminho_cor, "r") as file:
                cor = file.read()
                if cor == "":
                    cor = "#9044ff"
        except:
            None
    else:
        try:
            with open(caminho_cor, "w") as file:
                file.write("#9044ff")
            with open(caminho_cor, "r") as file:
                cor = file.read()
        except:
            None
    return cor

def hex_to_rgb(hex_string):
    if hex_string.startswith('#'):
        hex_string = hex_string[1:]

    r = int(hex_string[0:2], 16)
    g = int(hex_string[2:4], 16)
    b = int(hex_string[4:6], 16)

    return r, g, b

def Alterar_Cor(image, cor_original, cor_nova):
    cor_original = hex_to_rgb(cor_original)
    cor_nova = hex_to_rgb(cor_nova)
    imagem_original = Image.open(image)
    imagem_modificada = imagem_original.copy()
    imagem_modificada = imagem_modificada.convert("RGBA")
    pixel_data = list(imagem_modificada.getdata())

    for i, pixel in enumerate(pixel_data):
        if (pixel[0] > cor_original[0]-50 or pixel[0] < cor_original[0]+50) and (pixel[1] > cor_original[1]-50 or pixel[1] < cor_original[1]+50) and (pixel[2] > cor_original[2]-50 or pixel[2] < cor_original[2]+50):
            pixel_data[i] = (cor_nova[0], cor_nova[1], cor_nova[2], pixel[3])

    imagem_modificada.putdata(pixel_data)
    return imagem_modificada