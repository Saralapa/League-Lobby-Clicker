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