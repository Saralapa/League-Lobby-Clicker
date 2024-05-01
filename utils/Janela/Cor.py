from PIL import Image
import os

def Definir_Cor():
    caminho_cor = os.path.join(os.path.expanduser("~"),"League Lobby Clicker - Saralapa", "League_Lobby_Clicker_cor-Saralapa.txt")
    if os.path.exists(caminho_cor):
        try:
            with open(caminho_cor, "r") as file:
                cor = file.read()
                if cor == "":
                    cor = "#ffffff"
        except:
            None
    else:
        try:
            with open(caminho_cor, "w") as file:
                file.write("#ffffff")
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

def Botoes_Cores(imagem_cor):
    from utils.Janela.Janela import tk, root, tela_selecao_de_cor, cor, Atualizar_Cor
    from tkinter import colorchooser
    global botao_cor_pressionado
    botao_cor_pressionado = False

    def MouseSobreBotaoCor(event, botao_cor, i):
        global mouse_sobre_botao_cor
        mouse_sobre_botao_cor = True
    
    def MouseForaBotaoCor(event, botao_cor, i):
        global mouse_sobre_botao_cor
        mouse_sobre_botao_cor = False

    def BotaoCorPressionado(event, botao_cor, i):
        global botao_cor_pressionado, cor_atual
        cor_atual = botao_cor[i].cget("text")
        botao_cor_pressionado = True
        botao_cor[i].config(bg="#f0f0f0", fg="#f0f0f0", relief="sunken")

    def BotaoCorSolto(event, botao_cor, i):
        global botao_cor_pressionado
        botao_cor_pressionado = False
        if mouse_sobre_botao_cor:
            Atualizar_Cor(botao_cor[i].cget("text"))
        botao_cor[i].config(bg=cor_atual, fg=cor_atual, relief="raised")

    botao_icone_cor = tk.Button(root, image=imagem_cor, command=tela_selecao_de_cor, bd=0, bg="#191919", width=31, height=31)
    botao_icone_cor.pack()
    
    cores_padrao = ["#ff0000", "#00ff00",
                    "#00ffff", "#ffff00",
                    "#ff7f00", "#ff00ff",
                    "#9044ff", "#ffffff"]
    botoes_cores = [tk.Label(root, text=texto4, relief="raised") for texto4 in cores_padrao]

    for i in range(len(botoes_cores)):
        botoes_cores[i].bind("<Enter>", lambda event, i=i: MouseSobreBotaoCor(event, botoes_cores, i))
        botoes_cores[i].bind("<Leave>", lambda event, i=i: MouseForaBotaoCor(event, botoes_cores, i))
        botoes_cores[i].bind("<ButtonPress-1>", lambda event, i=i: BotaoCorPressionado(event, botoes_cores, i))
        botoes_cores[i].bind("<ButtonRelease-1>", lambda event, i=i: BotaoCorSolto(event, botoes_cores, i))
    
    frame_botao_cor_personalizada = tk.Frame(root, bg=cor, bd=2)
    frame_botao_cor_personalizada.pack()
    botao_cor_personalizada = tk.Button(frame_botao_cor_personalizada, text="Cor personalizada", command=lambda: Atualizar_Cor(colorchooser.askcolor()[1]), bg="#1f1f1f", fg=cor)
    botao_cor_personalizada.pack()

    i=0
    for botao in botoes_cores:
        botao.config(bg=cores_padrao[i], fg=cores_padrao[i])
        botao.pack()
        i+=1
    
    return botao_icone_cor, botoes_cores, frame_botao_cor_personalizada, botao_cor_personalizada