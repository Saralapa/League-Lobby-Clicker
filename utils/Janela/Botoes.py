def CriarBotaoConfirmar():
    from utils.Janela.Janela import tk, root, cor
    from utils.Janela.Botao_Confirmar import confirmar
    frame_botao_confirmar = tk.Frame(root, bg=cor, width=65, height=24, bd=1)
    frame_botao_confirmar.pack()

    botao_confirmar = tk.Button(frame_botao_confirmar, text="Confirmar", command=lambda: confirmar(), bg="#1f1f1f", fg=cor, bd=1)
    botao_confirmar.pack()
    return frame_botao_confirmar, botao_confirmar

def CriarBotaoDesfazer():
    from utils.Janela.Janela import tk, root, cor, desfazer
    frame_botao_desfazer = tk.Frame(root, bg=cor, width=85, height=24, bd=1)
    frame_botao_desfazer.pack()

    botao_desfazer = tk.Button(frame_botao_desfazer, text="Desfazer", command=lambda: desfazer(), bg="#1f1f1f", fg=cor, bd=1)
    botao_desfazer.pack()
    return frame_botao_desfazer, botao_desfazer

def CriarBotoesModosDeJogo():
    from utils.Janela.Janela import tk, root, cor, Atualizar_Modo_de_Jogo
    modos_de_jogo = ["Escolha alternada", "Ranqueada solo duo", "ARAM", "Blitz do Nexus", "Arena", "URF", "Todos por um", "Apenas auto aceitar"]

    frame_botoes_modos_de_jogo = [tk.Frame(root, bg=cor) for _ in modos_de_jogo]

    botoes_modos_de_jogo = [tk.Button(root, text=texto1, command=lambda t=texto1: Atualizar_Modo_de_Jogo(t)) for texto1 in modos_de_jogo]

    for botao in botoes_modos_de_jogo:
        botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)
        botao.pack(pady=5)

    for frame in frame_botoes_modos_de_jogo:
        frame.config(width=360, height=41, bd=0)

    return frame_botoes_modos_de_jogo, botoes_modos_de_jogo

def CriarBotoesRoles():
    from utils.Janela.Janela import tk, root, cor, Atualizar_Roles
    roles = ["Top", "Jungle", "Mid", "ADC", "Suporte", "Preencher"]

    frame_botoes_roles = [tk.Frame(root, bg=cor) for _ in roles]

    botoes_roles = [tk.Button(root, text=texto2, command=lambda t=texto2: Atualizar_Roles(t)) for texto2 in roles]

    for botao in botoes_roles:
        botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)
        botao.pack(pady=5)

    for frame in frame_botoes_roles:
        frame.config(width=360, height=41, bd=0)

    return frame_botoes_roles, botoes_roles