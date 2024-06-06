from PIL import Image
import os


def Definir_Cor():
    caminho_cor = os.path.join(
        os.path.expanduser("~"),
        "League Lobby Clicker - Saralapa",
        "League_Lobby_Clicker_cor-Saralapa.txt",
    )
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
    if hex_string.startswith("#"):
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

    tolerancia = 25
    for i, pixel in enumerate(pixel_data):
        if (
            (
                pixel[0] > cor_original[0] - tolerancia
                or pixel[0] < cor_original[0] + tolerancia
            )
            and (
                pixel[1] > cor_original[1] - tolerancia
                or pixel[1] < cor_original[1] + tolerancia
            )
            and (
                pixel[2] > cor_original[2] - tolerancia
                or pixel[2] < cor_original[2] + tolerancia
            )
        ):
            pixel_data[i] = (cor_nova[0], cor_nova[1], cor_nova[2], pixel[3])

    imagem_modificada.putdata(pixel_data)
    return imagem_modificada


def Atualizar_Cor(valor):
    from utils.Janela.Janela import (
        cor,
        frame_botao_desfazer,
        botao_desfazer,
        frame_botao_confirmar,
        botao_confirmar,
        label_borda_topo,
        label_borda_inferior,
        frame_botoes_idiomas,
        botoes_idiomas,
        frame_botoes_modos_de_jogo,
        botoes_modos_de_jogo,
        frame_botoes_roles,
        botoes_roles,
        label_auto_aceitar,
        frame_botao_cor_personalizada,
        botao_cor_personalizada,
        label_titulo,
        botao_minimizar,
        botao_fechar,
        imagem_cor,
        imagem_idioma,
        imagem_doacao,
        botao_icone_cor,
        botao_icone_idioma,
        botao_doacao,
    )
    from PIL import ImageTk

    if valor != None:
        cor = valor
        caminho_cor = os.path.join(
            os.path.expanduser("~"),
            "League Lobby Clicker - Saralapa",
            "League_Lobby_Clicker_cor-Saralapa.txt",
        )
        with open(caminho_cor, "w") as file:
            file.write(cor)

        frame_botao_desfazer.config(bg=cor)
        botao_desfazer.config(fg=cor)
        frame_botao_confirmar.config(bg=cor)
        botao_confirmar.config(fg=cor)
        label_borda_topo.config(fg=cor)
        label_borda_inferior.config(fg=cor)
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
        botao_minimizar.config(fg=cor)
        botao_fechar.config(fg=cor)

        imagem_cor = ImageTk.PhotoImage(
            Alterar_Cor("Images/Color-change.png", "#000000", cor)
        )
        botao_icone_cor.config(image=imagem_cor)

        imagem_idioma = ImageTk.PhotoImage(
            Alterar_Cor("Images/Language.png", "#ffffff", cor)
        )
        botao_icone_idioma.config(image=imagem_idioma)

        imagem_doacao = ImageTk.PhotoImage(
            Alterar_Cor("Images/Doacao.png", "#ef9ba0", cor)
        )
        botao_doacao.config(image=imagem_doacao)

        return (
            cor,
            imagem_cor,
            botao_icone_cor,
            imagem_idioma,
            botao_icone_idioma,
            imagem_doacao,
            botao_doacao,
        )


def CriarBotoesCores(imagem_cor):
    from utils.Janela.Janela import tk, root, tela_selecao_de_cor, cor, func_Cor
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
            func_Cor(botao_cor[i].cget("text"))
        botao_cor[i].config(bg=cor_atual, fg=cor_atual, relief="raised")

    botao_icone_cor = tk.Button(
        root,
        image=imagem_cor,
        command=tela_selecao_de_cor,
        bd=0,
        bg="#191919",
        width=31,
        height=31,
    )

    cores_padrao = [
        "#ff0000",
        "#00ff00",
        "#00ffff",
        "#ffff00",
        "#ff7f00",
        "#ff00ff",
        "#9044ff",
        "#ffffff",
    ]
    botoes_cores = [
        tk.Label(root, text=texto4, relief="raised") for texto4 in cores_padrao
    ]

    for i in range(len(botoes_cores)):
        botoes_cores[i].bind(
            "<Enter>", lambda event, i=i: MouseSobreBotaoCor(event, botoes_cores, i)
        )
        botoes_cores[i].bind(
            "<Leave>", lambda event, i=i: MouseForaBotaoCor(event, botoes_cores, i)
        )
        botoes_cores[i].bind(
            "<ButtonPress-1>",
            lambda event, i=i: BotaoCorPressionado(event, botoes_cores, i),
        )
        botoes_cores[i].bind(
            "<ButtonRelease-1>",
            lambda event, i=i: BotaoCorSolto(event, botoes_cores, i),
        )

    frame_botao_cor_personalizada = tk.Frame(root, bg=cor, bd=2)
    botao_cor_personalizada = tk.Button(
        frame_botao_cor_personalizada,
        text="Cor personalizada",
        command=lambda: func_Cor(colorchooser.askcolor()[1]),
        bg="#1f1f1f",
        fg=cor,
    )
    botao_cor_personalizada.pack()

    i = 0
    for botao in botoes_cores:
        botao.config(bg=cores_padrao[i], fg=cores_padrao[i])
        i += 1

    return (
        botao_icone_cor,
        botoes_cores,
        frame_botao_cor_personalizada,
        botao_cor_personalizada,
    )
