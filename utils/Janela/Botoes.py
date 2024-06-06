class Confirmar:
    def confirmar():
        from utils.Janela.Janela import (
            idioma,
            tela,
            modo_de_jogo,
            root,
            tela_auto_aceitar,
            texto_inferior,
            tela_selecao_de_role,
            Role_1,
            Role_2,
        )
        import utils.Janela.Janela

        if idioma.lower() == "portugues":
            if tela == "seleção de modo de jogo":
                if modo_de_jogo == "Apenas auto aceitar":
                    root.after(
                        500,
                        lambda: (
                            tela_auto_aceitar()
                            if modo_de_jogo == "Apenas auto aceitar"
                            else None
                        ),
                    )
                    if modo_de_jogo == "Apenas auto aceitar":
                        return

                if modo_de_jogo == None:
                    texto_inferior.set("Selecione um modo de jogo!")
                    root.after(
                        2000,
                        lambda: (
                            texto_inferior.set("Modo de jogo\nescolhido:")
                            if utils.Janela.Janela.modo_de_jogo == None
                            else None
                        ),
                    )
                root.after(
                    0,
                    lambda: (
                        tela_auto_aceitar()
                        if modo_de_jogo in ["ARAM", "Arena", "URF", "Todos por um"]
                        else tela_selecao_de_role() if modo_de_jogo != None else None
                    ),
                )
            elif tela == "seleção de role":
                if modo_de_jogo != "Blitz do Nexus" and (
                    Role_1 != "Preencher" and Role_2 == None
                ):
                    texto_inferior.set("As duas roles devem\nser preenchidas!")
                    if modo_de_jogo != "Blitz do Nexus":
                        root.after(
                            2000,
                            lambda: (
                                texto_inferior.set("Primeira role:\nSegunda role:")
                                if utils.Janela.Janela.tela == "seleção de role"
                                and utils.Janela.Janela.Role_1 == None
                                else None
                            ),
                        )
                        root.after(
                            2000,
                            lambda: (
                                texto_inferior.set(
                                    f"Primeira role: {utils.Janela.Janela.Role_1}\nSegunda role:"
                                )
                                if utils.Janela.Janela.tela == "seleção de role"
                                and utils.Janela.Janela.Role_2 == None
                                and utils.Janela.Janela.Role_1 != None
                                and utils.Janela.Janela.Role_1 != "Preencher"
                                else None
                            ),
                        )
                        root.after(
                            2000,
                            lambda: (
                                texto_inferior.set(
                                    f"Primeira role: {utils.Janela.Janela.Role_1}\nSegunda role: {utils.Janela.Janela.Role_2}"
                                )
                                if utils.Janela.Janela.tela == "seleção de role"
                                and utils.Janela.Janela.Role_1 != None
                                and utils.Janela.Janela.Role_2 != None
                                else None
                            ),
                        )
                    else:
                        root.after(
                            2000,
                            lambda: (
                                texto_inferior.set("Posição escolhida:")
                                if utils.Janela.Janela.tela == "seleção de role"
                                and utils.Janela.Janela.Role_1 == None
                                else None
                            ),
                        )
                elif modo_de_jogo == "Blitz do Nexus" and Role_1 == None:
                    texto_inferior.set("A role deve\nser preenchida!")
                    root.after(
                        2000,
                        lambda: (
                            texto_inferior.set("Posição escolhida:")
                            if utils.Janela.Janela.tela == "seleção de role"
                            and utils.Janela.Janela.Role_1 == None
                            else None
                        ),
                    )
                else:
                    root.after(500, lambda: tela_auto_aceitar())

        elif idioma.lower() == "english":
            if tela == "seleção de modo de jogo":
                if modo_de_jogo == "Just auto accept":
                    root.after(
                        500,
                        lambda: (
                            tela_auto_aceitar()
                            if modo_de_jogo == "Just auto accept"
                            else None
                        ),
                    )
                    if modo_de_jogo == "Just auto accept":
                        return

                if modo_de_jogo == None:
                    texto_inferior.set("Select a game mode!")
                    root.after(
                        2000,
                        lambda: (
                            texto_inferior.set("Selected game\nmode:")
                            if utils.Janela.Janela.modo_de_jogo == None
                            else None
                        ),
                    )
                root.after(
                    0,
                    lambda: (
                        tela_auto_aceitar()
                        if modo_de_jogo in ["ARAM", "Arena", "URF", "One for all"]
                        else tela_selecao_de_role() if modo_de_jogo != None else None
                    ),
                )
            elif tela == "seleção de role":
                if modo_de_jogo != "Nexus Blitz" and (
                    Role_1 != "Fill" and Role_2 == None
                ):
                    texto_inferior.set("Both roles must\nbe selected!")
                    if modo_de_jogo != "Nexus Blitz":
                        root.after(
                            2000,
                            lambda: (
                                texto_inferior.set("First role:\nSecond role:")
                                if utils.Janela.Janela.tela == "seleção de role"
                                and utils.Janela.Janela.Role_1 == None
                                else None
                            ),
                        )
                        root.after(
                            2000,
                            lambda: (
                                texto_inferior.set(
                                    f"First role: {utils.Janela.Janela.Role_1}\nSecond role:"
                                )
                                if utils.Janela.Janela.tela == "seleção de role"
                                and utils.Janela.Janela.Role_2 == None
                                and utils.Janela.Janela.Role_1 != None
                                and utils.Janela.Janela.Role_1 != "Fill"
                                else None
                            ),
                        )
                        root.after(
                            2000,
                            lambda: (
                                texto_inferior.set(
                                    f"First role: {utils.Janela.Janela.Role_1}\nSecond role: {utils.Janela.Janela.Role_2}"
                                )
                                if utils.Janela.Janela.tela == "seleção de role"
                                and utils.Janela.Janela.Role_1 != None
                                and utils.Janela.Janela.Role_2 != None
                                else None
                            ),
                        )
                    else:
                        root.after(
                            2000,
                            lambda: (
                                texto_inferior.set("Selected role:")
                                if utils.Janela.Janela.tela == "seleção de role"
                                and utils.Janela.Janela.Role_1 == None
                                else None
                            ),
                        )
                elif modo_de_jogo == "Nexus Blitz" and Role_1 == None:
                    texto_inferior.set("The role must\nbe selected!")
                    root.after(
                        2000,
                        lambda: (
                            texto_inferior.set("Selected role:")
                            if utils.Janela.Janela.tela == "seleção de role"
                            and utils.Janela.Janela.Role_1 == None
                            else None
                        ),
                    )
                else:
                    root.after(500, lambda: tela_auto_aceitar())

    def CriarBotaoConfirmar():
        from utils.Janela.Janela import tk, root, cor

        frame_botao_confirmar = tk.Frame(root, bg=cor, width=65, height=24, bd=1)
        frame_botao_confirmar.pack()

        botao_confirmar = tk.Button(
            frame_botao_confirmar,
            text="Confirmar",
            command=lambda: Confirmar.confirmar(),
            bg="#1f1f1f",
            fg=cor,
            bd=1,
        )
        botao_confirmar.pack()
        return frame_botao_confirmar, botao_confirmar


class Desfazer:
    def desfazer():
        from utils.Janela.Janela import (
            idioma,
            tela,
            modo_de_jogo,
            texto_inferior,
            Role_1,
            Role_2,
            botao_desfazer,
            tela_selecao_de_modo,
            jogo_está_aberto,
        )

        if idioma.lower() == "portugues":
            if tela == "seleção de modo de jogo":
                modo_de_jogo = None
                texto_inferior.set("Modo de jogo\nescolhido:")
            elif tela == "seleção de role":
                if Role_2 != None:
                    Role_2 = None
                    if modo_de_jogo != "Blitz do Nexus":
                        texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role:")
                    else:
                        texto_inferior.set("Posição escolhida:")
                elif Role_1 != None:
                    Role_1 = None
                    botao_desfazer.config(text="Menu anterior")
                    if modo_de_jogo != "Blitz do Nexus":
                        texto_inferior.set(f"Primeira role:\nSegunda role:")
                    else:
                        texto_inferior.set("Posição escolhida:")
                else:
                    jogo_está_aberto = False
                    tela_selecao_de_modo(jogo_está_aberto)
            elif tela == "auto aceitar":
                modo_de_jogo = None
                Role_1 = None
                Role_2 = None
                jogo_está_aberto = False
                tela_selecao_de_modo(jogo_está_aberto)
            elif tela == "alterar idioma":
                tela_selecao_de_modo(jogo_está_aberto)
            elif tela == "seleção de cor":
                tela_selecao_de_modo(jogo_está_aberto)
        elif idioma.lower() == "english":
            if tela == "seleção de modo de jogo":
                modo_de_jogo = None
                texto_inferior.set("Selected game\nmode:")
            elif tela == "seleção de role":
                if Role_2 != None:
                    Role_2 = None
                    if modo_de_jogo != "Nexus Blitz":
                        texto_inferior.set(f"First role: {Role_1}\nSecond role:")
                    else:
                        texto_inferior.set("Selected role:")
                elif Role_1 != None:
                    Role_1 = None
                    botao_desfazer.config(text="Previous menu")
                    if modo_de_jogo != "Nexus Blitz":
                        texto_inferior.set(f"First role:\nSecond role:")
                    else:
                        texto_inferior.set("Selected role:")
                else:
                    jogo_está_aberto = False
                    tela_selecao_de_modo(jogo_está_aberto)
            elif tela == "auto aceitar":
                modo_de_jogo = None
                Role_1 = None
                Role_2 = None
                jogo_está_aberto = False
                tela_selecao_de_modo(jogo_está_aberto)
            elif tela == "alterar idioma":
                tela_selecao_de_modo(jogo_está_aberto)
            elif tela == "seleção de cor":
                tela_selecao_de_modo(jogo_está_aberto)

        return modo_de_jogo, Role_1, Role_2, jogo_está_aberto

    def CriarBotaoDesfazer():
        from utils.Janela.Janela import tk, root, cor, func_Desfazer

        frame_botao_desfazer = tk.Frame(root, bg=cor, width=85, height=24, bd=1)
        frame_botao_desfazer.pack()

        botao_desfazer = tk.Button(
            frame_botao_desfazer,
            text="Desfazer",
            command=lambda: func_Desfazer(),
            bg="#1f1f1f",
            fg=cor,
            bd=1,
        )
        botao_desfazer.pack()
        return frame_botao_desfazer, botao_desfazer


class ModoDeJogo:
    def Atualizar_Modo_de_Jogo(valor):
        from utils.Janela.Janela import modo_de_jogo, idioma, texto_inferior

        modo_de_jogo = valor
        if idioma.lower() == "portugues":
            texto_inferior.set(f"Modo de jogo\nescolhido: {modo_de_jogo}")
        elif idioma.lower() == "english":
            texto_inferior.set(f"Selected game\nmode: {modo_de_jogo}")

        return modo_de_jogo

    def CriarBotoesModosDeJogo():
        from utils.Janela.Janela import tk, root, cor, func_ModoDeJogo

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

        frame_botoes_modos_de_jogo = [tk.Frame(root, bg=cor) for _ in modos_de_jogo]

        botoes_modos_de_jogo = [
            tk.Button(root, text=texto1, command=lambda t=texto1: func_ModoDeJogo(t))
            for texto1 in modos_de_jogo
        ]

        for botao in botoes_modos_de_jogo:
            botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)

        for frame in frame_botoes_modos_de_jogo:
            frame.config(width=360, height=41, bd=0)

        return frame_botoes_modos_de_jogo, botoes_modos_de_jogo


class Roles:
    def Atualizar_Roles(valor):
        from utils.Janela.Janela import (
            idioma,
            Role_1,
            Role_2,
            modo_de_jogo,
            botao_desfazer,
            texto_inferior,
            root,
            tela,
        )
        import utils.Janela.Janela

        if idioma.lower() == "portugues":
            if Role_1 == None or modo_de_jogo == "Blitz do Nexus":
                Role_1 = valor
                botao_desfazer.config(text="Desfazer")
                if modo_de_jogo != "Blitz do Nexus":
                    if Role_1 != "Preencher":
                        texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role:")
                    else:
                        texto_inferior.set(f"Posição escolhida: {Role_1}")
                else:
                    texto_inferior.set(f"Posição escolhida: {Role_1}")
                    if Role_1 != "Preencher":
                        Role_2 = "Preencher"
            elif (
                Role_2 == None
                and Role_1 != "Preencher"
                and modo_de_jogo != "Blitz do Nexus"
            ):
                Role_2 = valor
                texto_inferior.set(f"Primeira role: {Role_1}\nSegunda role: {Role_2}")
                if Role_1 == Role_2:
                    Role_2 = None
                    texto_inferior.set(
                        f"A primeira e a segunda\nposição não podem ser iguais!"
                    )
                    root.after(
                        2000,
                        lambda: (
                            texto_inferior.set(
                                f"Primeira role: {utils.Janela.Janela.Role_1}\nSegunda role:"
                            )
                            if utils.Janela.Janela.tela == "seleção de role"
                            and utils.Janela.Janela.Role_2 == None
                            and utils.Janela.Janela.Role_1 != None
                            else None
                        ),
                    )
                    root.after(
                        2000,
                        lambda: (
                            texto_inferior.set(
                                f"Primeira role: {utils.Janela.Janela.Role_1}\nSegunda role: {utils.Janela.Janela.Role_2}"
                            )
                            if utils.Janela.Janela.tela == "seleção de role"
                            and utils.Janela.Janela.Role_1 != None
                            and utils.Janela.Janela.Role_2 != None
                            else None
                        ),
                    )
        elif idioma.lower() == "english":
            if Role_1 == None or modo_de_jogo == "Nexus Blitz":
                Role_1 = valor
                botao_desfazer.config(text="Undo")
                if modo_de_jogo != "Nexus Blitz":
                    if Role_1 != "Fill":
                        texto_inferior.set(f"First role: {Role_1}\nSecond role:")
                    else:
                        texto_inferior.set(f"Selected role: {Role_1}")
                else:
                    texto_inferior.set(f"Selected role: {Role_1}")
                    if Role_1 != "Fill":
                        Role_2 = "Fill"
            elif Role_2 == None and Role_1 != "Fill" and modo_de_jogo != "Nexus Blitz":
                Role_2 = valor
                texto_inferior.set(f"First role: {Role_1}\nSecond role: {Role_2}")
                if Role_1 == Role_2:
                    Role_2 = None
                    texto_inferior.set(
                        f"The first and second\nroles cannot be the same!"
                    )
                    root.after(
                        2000,
                        lambda: (
                            texto_inferior.set(
                                f"First role: {utils.Janela.Janela.Role_1}\nSecond role:"
                            )
                            if utils.Janela.Janela.tela == "seleção de role"
                            and utils.Janela.Janela.Role_2 == None
                            and utils.Janela.Janela.Role_1 != None
                            else None
                        ),
                    )
                    root.after(
                        2000,
                        lambda: (
                            texto_inferior.set(
                                f"First role: {utils.Janela.Janela.Role_1}\nSecond role: {utils.Janela.Janela.Role_2}"
                            )
                            if utils.Janela.Janela.tela == "seleção de role"
                            and utils.Janela.Janela.Role_1 != None
                            and utils.Janela.Janela.Role_2 != None
                            else None
                        ),
                    )

        return Role_1, Role_2

    def CriarBotoesRoles():
        from utils.Janela.Janela import tk, root, cor, func_Roles

        roles = ["Top", "Jungle", "Mid", "ADC", "Suporte", "Preencher"]

        frame_botoes_roles = [tk.Frame(root, bg=cor) for _ in roles]

        botoes_roles = [
            tk.Button(root, text=texto2, command=lambda t=texto2: Roles.func_Roles(t))
            for texto2 in roles
        ]

        for botao in botoes_roles:
            botao.config(width=50, height=2, bg="#1f1f1f", fg=cor, bd=1)

        for frame in frame_botoes_roles:
            frame.config(width=360, height=41, bd=0)

        return frame_botoes_roles, botoes_roles
