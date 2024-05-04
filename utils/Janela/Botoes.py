class Confirmar():
    def confirmar():
        from utils.Janela.Janela import idioma, tela, modo_de_jogo, root, tela_auto_aceitar, texto_inferior, tela_selecao_de_role, Role_1, Role_2
        if idioma=="Portugues":
            if tela == "seleção de modo de jogo":
                if modo_de_jogo == "Apenas auto aceitar":
                    root.after(500, lambda: tela_auto_aceitar() if modo_de_jogo == "Apenas auto aceitar" else None)
                    if modo_de_jogo == "Apenas auto aceitar":
                        return

                if modo_de_jogo == None:
                    texto_inferior.set("Selecione um modo de jogo!")
                    root.after(2000, lambda: texto_inferior.set("Modo de jogo\nescolhido:") if modo_de_jogo == None else None)
                root.after(0, lambda: tela_auto_aceitar()
                            if modo_de_jogo == "ARAM"
                            or modo_de_jogo == "Arena"
                            or modo_de_jogo == "URF"
                            or modo_de_jogo == "Todos por um"
                            else tela_selecao_de_role() if modo_de_jogo is not None else None)
            elif tela == "seleção de role":
                if (modo_de_jogo != "Blitz do Nexus" and (Role_1 != "Preencher" and Role_2 == None)):
                    texto_inferior.set("As duas roles devem\nser preenchidas!")
                    if modo_de_jogo!="Blitz do Nexus":
                        root.after(2000, lambda: texto_inferior.set("Primeira role:\nSegunda role:") if tela=="seleção de role" and Role_1 == None else None)
                        root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role:") if tela=="seleção de role" and Role_2==None and Role_1 != None and Role_1 != "Preencher" else None)
                        root.after(2000, lambda: texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role: {Role_2}") if tela=="seleção de role" and Role_1 != None and Role_2!=None else None)
                    else: root.after(2000, lambda: texto_inferior.set("Posição escolhida:") if tela=="seleção de role" and Role_1 == None else None)
                elif modo_de_jogo== "Blitz do Nexus" and Role_1==None:
                    texto_inferior.set("A role deve\nser preenchida!")
                    root.after(2000, lambda: texto_inferior.set("Posição escolhida:") if tela=="seleção de role" and Role_1 == None else None)
                else:
                    root.after(500, lambda: tela_auto_aceitar())

        elif idioma=="English":
            if tela == "seleção de modo de jogo":
                if modo_de_jogo == "Just auto accept":
                    root.after(500, lambda: tela_auto_aceitar() if modo_de_jogo == "Just auto accept" else None)
                    if modo_de_jogo == "Just auto accept":
                        return

                if modo_de_jogo == None:
                    texto_inferior.set("Select a game mode!")
                    root.after(2000, lambda: texto_inferior.set("Selected game\nmode:") if modo_de_jogo == None else None)
                root.after(0, lambda: tela_auto_aceitar()
                            if modo_de_jogo == "ARAM"
                            or modo_de_jogo == "Arena"
                            or modo_de_jogo == "URF"
                            or modo_de_jogo == "One for all"
                            else tela_selecao_de_role() if modo_de_jogo is not None else None)
            elif tela == "seleção de role":
                if (modo_de_jogo != "Nexus Blitz" and (Role_1 != "Fill" and Role_2 == None)):
                    texto_inferior.set("Both roles must\nbe selected!")
                    if modo_de_jogo!="Nexus Blitz":
                        root.after(2000, lambda: texto_inferior.set("First role:\nSecond role:") if tela=="seleção de role" and Role_1 == None else None)
                        root.after(2000, lambda: texto_inferior.set(f"First role: {Role_1}\nSecond role:") if tela=="seleção de role" and Role_2==None and Role_1 != None and Role_1 != "Fill" else None)
                        root.after(2000, lambda: texto_inferior.set(f"First role: {Role_1}\nSecond role: {Role_2}") if tela=="seleção de role" and Role_1 != None and Role_2!=None else None)
                    else: root.after(2000, lambda: texto_inferior.set("Selected role:") if tela=="seleção de role" and Role_1 == None else None)
                elif modo_de_jogo== "Nexus Blitz" and Role_1==None:
                    texto_inferior.set("The role must\nbe selected!")
                    root.after(2000, lambda: texto_inferior.set("Selected role:") if tela=="seleção de role" and Role_1 == None else None)
                else:
                    root.after(500, lambda: tela_auto_aceitar())

    def CriarBotaoConfirmar():
        from utils.Janela.Janela import tk, root, cor
        frame_botao_confirmar = tk.Frame(root, bg=cor, width=65, height=24, bd=1)
        frame_botao_confirmar.pack()

        botao_confirmar = tk.Button(frame_botao_confirmar, text="Confirmar", command=lambda: Confirmar.confirmar(), bg="#1f1f1f", fg=cor, bd=1)
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

def CriarBotoesIdiomas(imagem_idioma):
    from utils.Janela.Janela import tk, root, cor, Atualizar_Idioma, ImageTk, tela_alterar_idioma
    lista_idiomas = ["Português", "English"]

    botao_icone_idioma = tk.Button(root, image=imagem_idioma, command=tela_alterar_idioma, bd=0, bg="#191919", width=31, height=31)

    frame_botoes_idiomas = [tk.Frame(root, bg=cor) for _ in lista_idiomas]

    botoes_idiomas = [tk.Button(root,text=texto3, command=lambda t=texto3: Atualizar_Idioma(t)) for texto3 in lista_idiomas]

    for botao in botoes_idiomas:
        botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)
        botao.pack(pady=5)

    for frame in frame_botoes_idiomas:
        frame.config(width=360, height=41, bd=0)

    return botao_icone_idioma, lista_idiomas, frame_botoes_idiomas, botoes_idiomas

def CriarBotoesCores(imagem_cor):
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