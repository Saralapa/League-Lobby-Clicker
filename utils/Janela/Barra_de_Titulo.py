def BotaoFechar():
    def MouseSobreBotaoFechar():
        from utils.Janela.Janela import botao_fechar
        global mouse_sobre_botao_fechar
        mouse_sobre_botao_fechar = True
        if not botao_fechar_pressionado:
            botao_fechar.config(bg="#c42b1c")

    def MouseForaBotaoFechar():
        from utils.Janela.Janela import botao_fechar, frame_barra_de_titulo
        global mouse_sobre_botao_fechar
        mouse_sobre_botao_fechar = False
        if not botao_fechar_pressionado:
            botao_fechar.config(bg=frame_barra_de_titulo.cget("background"))

    def BotaoFecharPressionado():
        from utils.Janela.Janela import botao_fechar
        global botao_fechar_pressionado
        botao_fechar_pressionado = True
        botao_fechar.config(bg="#d8534e")

    def BotaoFecharSolto():
        from utils.Janela.Janela import fechar_janela, root, botao_fechar, frame_barra_de_titulo
        global botao_fechar_pressionado
        botao_fechar_pressionado = False
        if mouse_sobre_botao_fechar:
            fechar_janela(root)
        botao_fechar.config(bg=frame_barra_de_titulo.cget("background"))

    from utils.Janela.Janela import tk, frame_barra_de_titulo
    global botao_fechar, botao_fechar_pressionado
    botao_fechar_pressionado = False
    botao_fechar = tk.Label(frame_barra_de_titulo, text="X", font=("Arial", 14), bg=frame_barra_de_titulo.cget("background"), fg="#f1f1f1", relief="flat")
    botao_fechar.place(width=45, height=frame_barra_de_titulo.winfo_reqheight())

    botao_fechar.bind("<Enter>", lambda event: MouseSobreBotaoFechar())
    botao_fechar.bind("<Leave>", lambda event: MouseForaBotaoFechar())
    botao_fechar.bind("<ButtonPress-1>", lambda event: BotaoFecharPressionado())
    botao_fechar.bind("<ButtonRelease-1>", lambda event: BotaoFecharSolto())

    return botao_fechar

def BotaoMinimizar():
    def MouseSobreBotaoMinimizar():
        global mouse_sobre_botao_minimizar
        mouse_sobre_botao_minimizar = True
        if not botao_minimizar_pressionado:
            botao_minimizar.config(bg="#2a2a2a")

    def MouseForaBotaoMinimizar():
        global mouse_sobre_botao_minimizar
        mouse_sobre_botao_minimizar = False
        if not botao_minimizar_pressionado:
            botao_minimizar.config(bg=frame_barra_de_titulo.cget("background"))

    def BotaoMinimizarPressionado():
        global botao_minimizar_pressionado
        botao_minimizar_pressionado = True
        botao_minimizar.config(bg="#2f2f2f")

    def BotaoMinimizarSolto():
        from utils.Janela.Janela import gw, root
        global botao_minimizar_pressionado
        botao_minimizar_pressionado = False
        if mouse_sobre_botao_minimizar:
            [window for window in gw.getWindowsWithTitle(root.title()) if window.title == root.title()][0].minimize()
        botao_minimizar.config(bg=frame_barra_de_titulo.cget("background"))

    from utils.Janela.Janela import tk, frame_barra_de_titulo
    global botao_minimizar_pressionado, botao_minimizar
    botao_minimizar_pressionado = False
    botao_minimizar = tk.Label(frame_barra_de_titulo, text="—", font=("Arial", 12), bg=frame_barra_de_titulo.cget("background"), fg="#f1f1f1")
    botao_minimizar.place(width=45, height=frame_barra_de_titulo.winfo_reqheight())

    botao_minimizar.bind("<Enter>", lambda event: MouseSobreBotaoMinimizar())
    botao_minimizar.bind("<Leave>", lambda event: MouseForaBotaoMinimizar())
    botao_minimizar.bind("<ButtonPress-1>", lambda event: BotaoMinimizarPressionado())
    botao_minimizar.bind("<ButtonRelease-1>", lambda event: BotaoMinimizarSolto())

    return botao_minimizar

def BotaoDoacao():
    def MouseSobreBotaoDoacao():
        global mouse_sobre_botao_doacao
        mouse_sobre_botao_doacao = True
        if not botao_doacao_pressionado:
            botao_doacao.config(bg="#2a2a2a")

    def MouseForaBotaoDoacao():
        global mouse_sobre_botao_doacao
        mouse_sobre_botao_doacao = False
        if not botao_doacao_pressionado:
            botao_doacao.config(bg=frame_barra_de_titulo.cget("background"))

    def BotaoDoacaoPressionado():
        global botao_doacao_pressionado
        botao_doacao_pressionado = True
        botao_doacao.config(bg="#2f2f2f")

    def BotaoDoacaoSolto():
        from utils.Janela.Janela import webbrowser
        global botao_doacao_pressionado
        botao_doacao_pressionado = False
        if mouse_sobre_botao_doacao:
            webbrowser.open("https://linktr.ee/Saralapa")
        botao_doacao.config(bg=frame_barra_de_titulo.cget("background"))

    from utils.Janela.Janela import frame_barra_de_titulo, imagem_doacao, tk
    global botao_doacao, botao_doacao_pressionado
    botao_doacao_pressionado = False
    botao_doacao = tk.Label(frame_barra_de_titulo, image=imagem_doacao, bg=frame_barra_de_titulo.cget("background"))
    botao_doacao.place(width=45,height=frame_barra_de_titulo.winfo_reqheight(), x=0, y=1)

    botao_doacao.bind("<Enter>", lambda event: MouseSobreBotaoDoacao())
    botao_doacao.bind("<Leave>", lambda event: MouseForaBotaoDoacao())
    botao_doacao.bind("<ButtonPress-1>", lambda event: BotaoDoacaoPressionado())
    botao_doacao.bind("<ButtonRelease-1>", lambda event: BotaoDoacaoSolto())

    return botao_doacao

def MoverJanela():
    def PosicaoCliqueBarraDeTitulo(event):
        global posicao_clique_barra_de_titulo_x, posicao_clique_barra_de_titulo_y
        posicao_clique_barra_de_titulo_x = event.x_root
        posicao_clique_barra_de_titulo_y = event.y_root

    def AlterarPosicaoJanela(event):
        global posicao_clique_barra_de_titulo_x, posicao_clique_barra_de_titulo_y
        nova_posicao_x = root.winfo_x() + (event.x_root - posicao_clique_barra_de_titulo_x)
        nova_posicao_y = root.winfo_y() + (event.y_root - posicao_clique_barra_de_titulo_y)
        
        root.geometry(f'+{nova_posicao_x}+{nova_posicao_y}')
        posicao_clique_barra_de_titulo_x = event.x_root
        posicao_clique_barra_de_titulo_y = event.y_root

    from utils.Janela.Janela import frame_barra_de_titulo, label_titulo, root, label_icone
    frame_barra_de_titulo.bind('<Button-1>', PosicaoCliqueBarraDeTitulo)
    frame_barra_de_titulo.bind('<B1-Motion>', AlterarPosicaoJanela)
    label_titulo.bind('<Button-1>', PosicaoCliqueBarraDeTitulo)
    label_titulo.bind('<B1-Motion>', AlterarPosicaoJanela)
    label_icone.bind('<Button-1>', PosicaoCliqueBarraDeTitulo)
    label_icone.bind('<B1-Motion>', AlterarPosicaoJanela)

def BordaJanela():
    from utils.Janela.Janela import tk, root
    frame_topo_janela = tk.Frame(root, bg="#404040", height=1)
    frame_topo_janela.place(x=0, y=0)

    frame_esquerda_janela = tk.Frame(root, bg="#404040", width=1)
    frame_esquerda_janela.place(x=0, y=0)

    frame_direita_janela = tk.Frame(root, bg="#404040", width=1)
    frame_direita_janela.place(y=0)

    frame_base_janela = tk.Frame(root, bg="#404040", height=1)
    frame_base_janela.place(x=0)

    return frame_topo_janela, frame_esquerda_janela, frame_direita_janela, frame_base_janela

def Criar_Barra_de_Titulo(icone):
    from utils.Janela.Janela import tk, root, cor
    frame_barra_de_titulo = tk.Frame(root, bg="#1f1f1f", height=30)
    frame_barra_de_titulo.pack()
    frame_barra_de_titulo.pack_propagate(0)
    frame_barra_de_titulo.place(x=0)

    label_icone = tk.Label(frame_barra_de_titulo, image=icone, bg=frame_barra_de_titulo.cget("background"))
    label_icone.place(x=6, y=4)

    label_titulo = tk.Label(frame_barra_de_titulo, text=root.title(), bg=frame_barra_de_titulo.cget("background"), fg=cor)
    label_titulo.place(x=26, y=4)
    
    return frame_barra_de_titulo, label_icone, label_titulo