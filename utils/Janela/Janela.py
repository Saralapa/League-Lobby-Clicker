import threading
import pygetwindow as gw
import tkinter as tk
import time
from PIL import ImageTk, Image
from utils.Janela import (
    Texto_Tela_Auto_Aceitar,
    Cor,
    Botoes,
    Barra_de_Titulo,
    Configuracoes_da_Janela,
    Abrir_Janela_Fechar_Janela,
    Argumentos,
)
from utils import Cliques, Idioma


def tela_selecao_de_modo(jogo_está_aberto):
    global tela, Role_1, Role_2, modo_de_jogo, roles, possui_argumentos
    Configuracoes_da_Janela.centralizar_janela(root, 378, 506)
    root.title("League Lobby Clicker - Saralapa")
    label_titulo.config(text=root.title())
    frame_barra_de_titulo.config(width=root.winfo_width())
    botao_fechar.place(x=root.winfo_width() - 45)
    botao_minimizar.place(x=root.winfo_width() - 45 * 2)
    botao_doacao.place(x=root.winfo_width() - 45 * 3)

    frame_topo_janela.config(width=root.winfo_width())
    frame_esquerda_janela.config(height=root.winfo_height())
    frame_direita_janela.config(height=root.winfo_height())
    frame_direita_janela.place(x=root.winfo_width() - 1)
    frame_base_janela.config(width=root.winfo_width())
    frame_base_janela.place(y=root.winfo_height() - 1)

    tela = "seleção de modo de jogo"
    for frame in frame_botoes_roles:
        frame.place_forget()
    for botao in botoes_roles:
        botao.place_forget()
    label_auto_aceitar.place_forget()
    for frame in frame_botoes_idiomas:
        frame.place_forget()
    for botao in botoes_idiomas:
        botao.place_forget()
    for botao in botoes_cores:
        botao.place_forget()
    frame_botao_cor_personalizada.place_forget()

    if idioma.lower() == "portugues":
        modos_de_jogo = [
            "Escolha alternada",
            "Ranqueada solo duo",
            "ARAM",
            "Blitz do Nexus",
            "Arena",
            "URF",
            "Todos por um",
            "Apenas auto aceitar",
        ]
    elif idioma.lower() == "english":
        modos_de_jogo = [
            "Draft pick",
            "Ranked solo duo",
            "ARAM",
            "Nexus Blitz",
            "Arena",
            "URF",
            "One for all",
            "Just auto accept",
        ]

    botao_icone_idioma.place(relx=0.8915, rely=0.075375)
    botao_icone_cor.place(relx=0.0195, rely=0.072375)
    frame_borda_topo.pack()
    frame_borda_topo.place(relx=0.4988888888888888, rely=0.1095, anchor="center")
    label_borda_topo.pack()
    frame_borda_inferior.pack()
    frame_borda_inferior.place(relx=0.4988888888888888, rely=0.956, anchor="center")
    frame_botao_desfazer.config(bd=1)
    frame_botao_desfazer.pack()
    frame_botao_desfazer.place(relx=0.025, rely=0.9815, anchor="sw")
    frame_botao_confirmar.pack()
    frame_botao_confirmar.place(relx=0.975, rely=0.9815, anchor="se")

    i = 0
    for botao in botoes_modos_de_jogo:
        frame_botoes_modos_de_jogo[i].place(relx=0.0245, rely=0.1565 + i * 0.09675)
        botao.config(
            text=modos_de_jogo[i], command=lambda t=modos_de_jogo[i]: func_ModoDeJogo(t)
        )
        botao.place(relx=0.0275, rely=0.158 + i * 0.0968)
        i += 1

    if idioma.lower() == "portugues":
        label_borda_topo.config(text="Escolha o modo de jogo")
        if modo_de_jogo == None:
            texto_inferior.set("Modo de jogo\nescolhido:")
        else:
            texto_inferior.set(f"Modo de jogo\nescolhido: {modo_de_jogo.capitalize()}")
        botao_desfazer.config(text="Desfazer")
        botao_confirmar.config(text="Confirmar")
    elif idioma.lower() == "english":
        label_borda_topo.config(text="Select game mode")
        if modo_de_jogo == None:
            texto_inferior.set("Selected game\nmode:")
        else:
            texto_inferior.set(f"Selected game\nmode: {modo_de_jogo.capitalize()}")
        botao_desfazer.config(text="Undo")
        botao_confirmar.config(text="Confirm")
    botao_desfazer.config(height=0)

    def Jogo_Aberto(jogo_está_aberto):
        global modo_de_jogo
        while True:
            if jogo_está_aberto == False:
                return
            for i in range(30, 0, -1):
                time.sleep(1)
                print(i)

            if (
                not [
                    window
                    for window in gw.getWindowsWithTitle(
                        "League of Legends (TM) Client"
                    )
                    if window.title == "League of Legends (TM) Client"
                ]
                and jogo_está_aberto == True
            ):
                if tela == "seleção de modo de jogo":
                    if idioma.lower() == "portugues":
                        modo_de_jogo = "Apenas auto aceitar"
                    elif idioma.lower() == "english":
                        modo_de_jogo = "Just auto accept"
                    jogo_está_aberto = False
                    tela_auto_aceitar()
                return

    if possui_argumentos:
        possui_argumentos = False
        tela_auto_aceitar()
    else:
        Role_1 = None
        Role_2 = None
    if jogo_está_aberto == True:
        thread_jogo_aberto = threading.Thread(target=Jogo_Aberto(jogo_está_aberto))
        thread_jogo_aberto.daemon = True
        thread_jogo_aberto.start()


def tela_selecao_de_role():
    global tela, botoes_roles, roles
    tela = "seleção de role"
    for botao in botoes_modos_de_jogo:
        botao.place_forget()
    for frame in frame_botoes_modos_de_jogo:
        frame.place_forget()
    botao_icone_idioma.place_forget()
    botao_icone_cor.place_forget()

    if idioma.lower() == "portugues":
        label_borda_topo.config(text="Escolha em que posição você vai jogar")
        if Role_1 == None:
            botao_desfazer.config(text="Menu anterior")
        else:
            botao_desfazer.config(text="Desfazer")
    elif idioma.lower() == "english":
        label_borda_topo.config(text="Choose which position you will play")
        if Role_1 == None:
            botao_desfazer.config(text="Previous menu")
        else:
            botao_desfazer.config(text="Undo")

    if modo_de_jogo == "Blitz do Nexus" or modo_de_jogo == "Nexus Blitz":
        Configuracoes_da_Janela.centralizar_janela(root, 378, 265)
        frame_barra_de_titulo.config(width=root.winfo_width())
        frame_topo_janela.config(width=root.winfo_width())
        frame_esquerda_janela.config(height=root.winfo_height())
        frame_direita_janela.config(height=root.winfo_height())
        frame_direita_janela.place(x=root.winfo_width() - 1)
        frame_base_janela.config(width=root.winfo_width())
        frame_base_janela.place(y=root.winfo_height() - 1)

        frame_botao_desfazer.place(rely=0.966)
        frame_botao_confirmar.place(rely=0.966)
        frame_borda_topo.place(relx=0.4988888888888888, y=28, anchor="center")
        frame_borda_inferior.place(relx=0.4988888888888888, rely=0.914, anchor="center")
        if idioma.lower() == "portugues":
            texto_inferior.set("Posição escolhida:")
        elif idioma.lower() == "english":
            texto_inferior.set("Selected role:")

        for botao in botoes_roles:
            botao.destroy()

        if idioma.lower() == "portugues":
            roles = ["Jungle", "Rota", "Preencher"]
        elif idioma.lower() == "english":
            roles = ["Jungle", "Lane", "Fill"]

        botoes_roles = [
            tk.Button(root, text=texto2, command=lambda t=texto2: func_Roles(t))
            for texto2 in roles
        ]
        i = 0
        for botao in botoes_roles:
            frame_botoes_roles[i].place(relx=0.0245, y=83 + i * 49)
            botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)
            botao.place(relx=0.0275, y=84 + i * 49)
            i += 1

    else:
        Configuracoes_da_Janela.centralizar_janela(root, 378, 410)
        frame_barra_de_titulo.config(width=root.winfo_width())
        frame_topo_janela.config(width=root.winfo_width())
        frame_esquerda_janela.config(height=root.winfo_height())
        frame_direita_janela.config(height=root.winfo_height())
        frame_direita_janela.place(x=root.winfo_width() - 1)
        frame_base_janela.config(width=root.winfo_width())
        frame_base_janela.place(y=root.winfo_height() - 1)

        frame_botao_desfazer.place(rely=0.9775)
        frame_botao_confirmar.place(rely=0.9775)
        frame_borda_inferior.place(relx=0.4988888888888888, rely=0.946, anchor="center")
        frame_borda_topo.place(relx=0.4988888888888888, y=11, anchor="center")
        if idioma.lower() == "portugues":
            texto_inferior.set(f"Primeira role:\nSegunda role:")
        elif idioma.lower() == "english":
            texto_inferior.set(f"First role:\nSecond role:")

        for botao in botoes_roles:
            botao.destroy()

        if idioma.lower() == "portugues":
            roles = ["Top", "Jungle", "Mid", "ADC", "Suporte", "Preencher"]
        elif idioma.lower() == "english":
            roles = ["Top", "Jungle", "Mid", "ADC", "Support", "Fill"]
        botoes_roles = [
            tk.Button(root, text=texto2, command=lambda t=texto2: func_Roles(t))
            for texto2 in roles
        ]

        i = 0
        for botao in botoes_roles:
            frame_botoes_roles[i].place(relx=0.0245, y=81 + i * 49)
            botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)
            botao.place(relx=0.0275, y=82 + i * 49)
            i += 1


def tela_alterar_idioma():
    global tela
    altura_janela_idioma = 108 + len(lista_idiomas) * 49
    Configuracoes_da_Janela.centralizar_janela(root, 378, altura_janela_idioma)
    frame_barra_de_titulo.config(width=root.winfo_width())
    frame_topo_janela.config(width=root.winfo_width())
    frame_esquerda_janela.config(height=root.winfo_height())
    frame_direita_janela.config(height=root.winfo_height())
    frame_direita_janela.place(x=root.winfo_width() - 1)
    frame_base_janela.config(width=root.winfo_width())
    frame_base_janela.place(y=root.winfo_height() - 1)

    tela = "alterar idioma"
    frame_borda_topo.pack_forget()
    frame_borda_topo.place_forget()
    for botao in botoes_modos_de_jogo:
        botao.place_forget()
    for frame in frame_botoes_modos_de_jogo:
        frame.place_forget()
    for frame in frame_botoes_roles:
        frame.place_forget()
    frame_botao_confirmar.pack_forget()
    frame_botao_confirmar.place_forget()
    botao_icone_idioma.place_forget()
    botao_icone_cor.place_forget()

    i = 0
    for botao in botoes_idiomas:
        frame_botoes_idiomas[i].place(relx=0.0245, y=39 + i * 49)
        botao.place(x=(root.winfo_width() - botao.winfo_reqwidth()) // 2, y=40 + i * 49)
        i += 1

    frame_borda_inferior.pack()
    frame_borda_inferior.place(relx=0.4988888888888888, y=149, anchor="center")
    if idioma.lower() == "portugues":
        texto_inferior.set("Idioma selecionado: Português")
        botao_desfazer.config(text="Confirmar")
    elif idioma.lower() == "english":
        texto_inferior.set(f"Selected language: {idioma.capitalize()}")
        botao_desfazer.config(text="Confirm")

    frame_botao_desfazer.place(relx=0.4988888888888888, y=-19, anchor="center")


def tela_selecao_de_cor():
    global tela
    Configuracoes_da_Janela.centralizar_janela(root, 303, 388)
    root.title("League Lobby Clicker - S...")
    label_titulo.config(text=root.title())
    frame_barra_de_titulo.config(width=root.winfo_width())
    botao_fechar.place(x=root.winfo_width() - 45)
    botao_minimizar.place(x=root.winfo_width() - 45 * 2)
    botao_doacao.place(x=root.winfo_width() - 45 * 3)
    frame_topo_janela.config(width=root.winfo_width())
    frame_esquerda_janela.config(height=root.winfo_height())
    frame_direita_janela.config(height=root.winfo_height())
    frame_direita_janela.place(x=root.winfo_width() - 1)
    frame_base_janela.config(width=root.winfo_width())
    frame_base_janela.place(y=root.winfo_height() - 1)

    tela = "seleção de cor"
    frame_borda_topo.pack_forget()
    frame_borda_topo.place_forget()
    for botao in botoes_modos_de_jogo:
        botao.place_forget()
    for frame in frame_botoes_modos_de_jogo:
        frame.place_forget()
    for frame in frame_botoes_roles:
        frame.place_forget()
    frame_botao_confirmar.pack_forget()
    frame_botao_confirmar.place_forget()
    botao_icone_idioma.place_forget()
    botao_icone_cor.place_forget()
    frame_borda_inferior.pack_forget()
    frame_borda_inferior.place_forget()

    if idioma.lower() == "portugues":
        botao_desfazer.config(text="Confirmar")
        botao_cor_personalizada.config(text="Cor personalizada")
    elif idioma.lower() == "english":
        botao_desfazer.config(text="Confirm")
        botao_cor_personalizada.config(text="Custom color")
    botao_desfazer.config(height=2)
    frame_botao_desfazer.config(bd=2)
    frame_botao_desfazer.place(relx=0.4988888888888888, y=-30, anchor="center")
    botao_cor_personalizada.config(height=2)
    frame_botao_cor_personalizada.place(relx=0.4988888888888888, y=67, anchor="center")
    j = 0
    k = 0
    for i in range(len(botoes_cores)):
        if k == 2:
            k = 0
        if i % 2 == 0 and i != 0:
            j += 1
        botoes_cores[i].config(width=17, height=2, bd=2)
        botoes_cores[i].place(relx=0.04875 + k * 0.47725, y=105 + j * 56)
        k += 1


def tela_auto_aceitar():
    global tela, jogo_está_aberto
    Configuracoes_da_Janela.centralizar_janela(root, 375, 130)
    frame_barra_de_titulo.config(width=root.winfo_width())
    botao_fechar.place(x=root.winfo_width() - 45)
    botao_minimizar.place(x=root.winfo_width() - 45 * 2)
    botao_doacao.place(x=root.winfo_width() - 45 * 3)
    frame_topo_janela.config(width=root.winfo_width())
    frame_esquerda_janela.config(height=root.winfo_height())
    frame_direita_janela.config(height=root.winfo_height())
    frame_direita_janela.place(x=root.winfo_width() - 1)
    frame_base_janela.config(width=root.winfo_width())
    frame_base_janela.place(y=root.winfo_height() - 1)

    if [
        window
        for window in gw.getWindowsWithTitle("League of Legends (TM) Client")
        if window.title == "League of Legends (TM) Client"
    ]:
        jogo_está_aberto = True

    tela = "auto aceitar"
    frame_borda_topo.pack_forget()
    frame_borda_topo.place_forget()
    for botao in botoes_modos_de_jogo:
        botao.place_forget()
    for frame in frame_botoes_modos_de_jogo:
        frame.place_forget()
    for frame in frame_botoes_roles:
        frame.place_forget()
    for botao in botoes_roles:
        botao.place_forget()
    frame_botao_confirmar.pack_forget()
    frame_botao_confirmar.place_forget()
    frame_borda_inferior.pack_forget()
    frame_borda_inferior.place_forget()
    botao_icone_idioma.place_forget()
    botao_icone_cor.place_forget()

    label_auto_aceitar.place(relx=0.4988888888888888, y=62, anchor="center")

    if idioma.lower() == "portugues":
        botao_desfazer.config(text="Menu principal")
    elif idioma.lower() == "english":
        botao_desfazer.config(text="Main menu")
    frame_botao_desfazer.place(relx=0.4988888888888888, y=-24, anchor="center")

    thread_imagem = threading.Thread(target=Cliques.WhereToClick)
    thread_imagem.daemon = True
    thread_imagem.start()

    thread_mensagem = threading.Thread(
        target=Texto_Tela_Auto_Aceitar.atualizar_mensagem
    )
    thread_mensagem.daemon = True
    thread_mensagem.start()


def func_Desfazer():
    global modo_de_jogo, Role_1, Role_2, jogo_está_aberto
    modo_de_jogo, Role_1, Role_2, jogo_está_aberto = Botoes.Desfazer.desfazer()


def func_ModoDeJogo(valor):
    global modo_de_jogo
    modo_de_jogo = Botoes.ModoDeJogo.Atualizar_Modo_de_Jogo(valor)


def func_Roles(valor):
    global Role_1, Role_2
    Role_1, Role_2 = Botoes.Roles.Atualizar_Roles(valor)


def func_Cor(valor):
    global cor, imagem_cor, botao_icone_cor, imagem_idioma, botao_icone_idioma, imagem_doacao, botao_doacao
    (
        cor,
        imagem_cor,
        botao_icone_cor,
        imagem_idioma,
        botao_icone_idioma,
        imagem_doacao,
        botao_doacao,
    ) = Cor.Atualizar_Cor(valor)


def func_Idioma(valor):
    global idioma
    idioma = Idioma.Atualizar_Idioma(valor)


def Criar_Janela():
    global frame_botoes_roles, label_auto_aceitar, frame_botoes_idiomas, botoes_modos_de_jogo, botao_icone_idioma, frame_borda_topo, label_borda_topo, frame_borda_inferior, frame_botao_desfazer, frame_botao_confirmar, frame_botoes_modos_de_jogo, texto_inferior, botao_desfazer, botao_confirmar, root, lista_idiomas, idioma, jogo_está_aberto, botoes_roles, botoes_idiomas, botao_icone_cor, cor, botoes_cores, label_borda_inferior, imagem_cor, imagem_idioma, botao_cor_personalizada, modo_de_jogo, frame_botao_cor_personalizada, frame_barra_de_titulo, frame_topo_janela, frame_esquerda_janela, label_titulo, frame_direita_janela, frame_base_janela, label_icone, botao_fechar, botao_minimizar, imagem_doacao, botao_doacao, Role_1, Role_2, possui_argumentos

    idioma = Idioma.definir_idioma()
    cor = Cor.Definir_Cor()
    modo_de_jogo = None
    jogo_está_aberto = False
    root = tk.Tk()

    Configuracoes_da_Janela.ConfiguracoesJanela(root)

    frame_borda_topo = tk.LabelFrame(root, bg="#191919", width=210, height=30, bd=0)
    frame_borda_topo.pack(side="top", anchor="center", pady=5)
    label_borda_topo = tk.Label(
        frame_borda_topo,
        font=("Arial", 14),
        text="Escolha o modo de jogo",
        bg="#191919",
        fg=cor,
        height=0,
    )

    frame_borda_inferior = tk.LabelFrame(root, bg="#191919", width=210, height=30, bd=0)
    texto_inferior = tk.StringVar(frame_borda_inferior)
    label_borda_inferior = tk.Label(
        frame_borda_inferior, textvariable=texto_inferior, bg="#191919", fg=cor
    )
    label_borda_inferior.pack()

    label_auto_aceitar = tk.Label(root, font=("Arial", 18), bg="#191919", fg=cor)

    frame_botoes_modos_de_jogo, botoes_modos_de_jogo = (
        Botoes.ModoDeJogo.CriarBotoesModosDeJogo()
    )
    frame_botoes_roles, botoes_roles = Botoes.Roles.CriarBotoesRoles()

    imagem_idioma = ImageTk.PhotoImage(
        Cor.Alterar_Cor("Images/Language.png", "#ffffff", cor)
    )
    botao_icone_idioma, lista_idiomas, frame_botoes_idiomas, botoes_idiomas = (
        Idioma.CriarBotoesIdiomas(imagem_idioma)
    )

    imagem_cor = ImageTk.PhotoImage(
        Cor.Alterar_Cor("Images/Color-change.png", "#000000", cor)
    )
    (
        botao_icone_cor,
        botoes_cores,
        frame_botao_cor_personalizada,
        botao_cor_personalizada,
    ) = Cor.CriarBotoesCores(imagem_cor)

    frame_botao_desfazer, botao_desfazer = Botoes.Desfazer.CriarBotaoDesfazer()
    frame_botao_confirmar, botao_confirmar = Botoes.Confirmar.CriarBotaoConfirmar()

    icone = ImageTk.PhotoImage(Image.open("Images/icon.ico").resize((16, 16)))

    frame_barra_de_titulo, label_icone, label_titulo = (
        Barra_de_Titulo.Criar_Barra_de_Titulo(icone)
    )
    (
        frame_topo_janela,
        frame_esquerda_janela,
        frame_direita_janela,
        frame_base_janela,
    ) = Barra_de_Titulo.BordaJanela()

    botao_fechar = Barra_de_Titulo.BotoesBarraDeTitulo.BotaoFechar()

    botao_minimizar = Barra_de_Titulo.BotoesBarraDeTitulo.BotaoMinimizar()

    imagem_doacao = ImageTk.PhotoImage(
        Cor.Alterar_Cor("Images/Doacao.png", "#ef9ba0", cor)
    )
    botao_doacao = Barra_de_Titulo.BotoesBarraDeTitulo.BotaoDoacao()

    Barra_de_Titulo.MoverJanela()

    root.after(10, lambda: Abrir_Janela_Fechar_Janela.AbrirJanela(root.title()))

    modo_de_jogo, Role_1, Role_2, possui_argumentos, idioma = Argumentos.Argumentos()
    tela_selecao_de_modo(jogo_está_aberto)
    root.mainloop()
