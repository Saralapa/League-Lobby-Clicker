import os


def definir_idioma():
    caminho_idioma = os.path.join(
        os.path.expanduser("~"),
        "League Lobby Clicker - Saralapa",
        "League_Lobby_Clicker_idioma-Saralapa.txt",
    )
    if os.path.exists(caminho_idioma):
        try:
            with open(caminho_idioma, "r") as file:
                idioma = file.read()
                if not idioma.lower() in ["portugues", "english"]:
                    with open(caminho_idioma, "w") as file:
                        file.write("Portugues")
                    idioma = file.read()
            return idioma.lower()
        except:
            None
    try:
        with open(caminho_idioma, "w") as file:
            file.write("Portugues")
        with open(caminho_idioma, "r") as file:
            idioma = file.read()
        return idioma.lower()
    except:
        None


def Atualizar_Idioma(valor):
    from utils.Janela.Janela import idioma, botao_desfazer, texto_inferior

    idioma = valor.replace("ê", "e")
    caminho_idioma = os.path.join(
        os.path.expanduser("~"),
        "League Lobby Clicker - Saralapa",
        "League_Lobby_Clicker_idioma-Saralapa.txt",
    )
    with open(caminho_idioma, "w") as file:
        file.write(idioma)
    if idioma.lower() == "portugues":
        botao_desfazer.config(text="Confirmar")
        texto_inferior.set(f"Idioma selecionado: {valor}")
    elif idioma.lower() == "english":
        botao_desfazer.config(text="Confirm")
        texto_inferior.set(f"Selected language: {valor}")

    return idioma.lower()


def CriarBotoesIdiomas(imagem_idioma):
    from utils.Janela.Janela import tk, root, cor, func_Idioma, tela_alterar_idioma

    lista_idiomas = ["Português", "English"]

    botao_icone_idioma = tk.Button(
        root,
        image=imagem_idioma,
        command=tela_alterar_idioma,
        bd=0,
        bg="#191919",
        width=31,
        height=31,
    )

    frame_botoes_idiomas = [tk.Frame(root, bg=cor) for _ in lista_idiomas]

    botoes_idiomas = [
        tk.Button(root, text=texto3, command=lambda t=texto3: func_Idioma(t))
        for texto3 in lista_idiomas
    ]

    for botao in botoes_idiomas:
        botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)

    for frame in frame_botoes_idiomas:
        frame.config(width=360, height=41, bd=0)

    return botao_icone_idioma, lista_idiomas, frame_botoes_idiomas, botoes_idiomas
