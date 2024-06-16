import sys
from utils.Idioma import definir_idioma, Atualizar_Idioma


def Argumentos():
    """
    Parses command line arguments and assigns values to corresponding variables.

    Returns:
    tuple: A tuple containing the assigned values of the command line arguments, a flag indicating the presence of command line arguments, and the selected language.

    This function iterates through the command line arguments, identifies the specified strings, and assigns the subsequent argument values to the corresponding variables.
    If the subsequent argument is part of a multi-word value, it concatenates the words to form the complete value.
    The function also sets the 'possui_argumentos' flag to True if command line arguments are present.
    """
    Argumentos_Disponiveis = {
        "modo_de_jogo": [None, "--gamemode"],
        "Role_1": [None, "--role1"],
        "Role_2": [None, "--role2"],
        "idioma": [definir_idioma(), "--language"],
    }

    possui_argumentos = False

    def AtribuirArgumentos(variable: str, string: str) -> str:
        """
        Assigns command line arguments to a variable based on a specified string.

        Parameters:
        variable (str): The variable to which the command line argument will be assigned. Eg. ("modo_de_jogo")
        string (str): The specified string used to identify the command line argument. Eg. ("--gamemode")

        Returns:
        str: The assigned value of the command line argument.

        This function iterates through the command line arguments, identifies the specified string, and assigns the subsequent argument value to the variable. If the subsequent argument is part of a multi-word value, it concatenates the words to form the complete value. The function also sets the 'possui_argumentos' flag to True if command line arguments are present.
        """
        nonlocal possui_argumentos
        if len(sys.argv) > 1:
            possui_argumentos = True
            args = sys.argv[1:]
            for i in range(len(args)):
                if args[i].lower().startswith("--") and not any(
                    args[i].lower() in values
                    for values in Argumentos_Disponiveis.values()
                ):
                    raise ValueError(f'Argument "{args[i]}" not supported yet.')
                if args[i].lower() == string:
                    variable = args[i + 1].lower().replace("ê", "e")
                    try:
                        j = i
                        while not args[j + 2].startswith("--"):
                            variable += " " + args[j + 2].lower().replace("ê", "e")
                            j += 1
                    except:
                        pass
                    print(variable)
        return variable

    for chave, valor in Argumentos_Disponiveis.items():
        globals()[f"{chave}"] = valor[0]
        globals()[f"{chave}"] = AtribuirArgumentos(globals()[f"{chave}"], valor[1])

    if modo_de_jogo != None and modo_de_jogo.lower() not in [  # type: ignore
        "escolha alternada",
        "ranqueada solo duo",
        "aram",
        "blitz do nexus",
        "arena",
        "urf",
        "todos por um",
        "apenas auto aceitar",
        "draft pick",
        "ranked solo duo",
        "nexus blitz",
        "one for all",
        "just auto accept",
    ]:
        raise ValueError("Game mode not supported yet.")

    roles = [
        "jungle",
        "rota",
        "preencher",
        "lane",
        "fill",
        "top",
        "mid",
        "adc",
        "suporte",
        "support",
    ]

    if Role_1 != None and Role_1.lower() not in roles:  # type: ignore
        print(Role_1, "role 1 aqui ó")  # type: ignore
        raise ValueError("Role 1 not supported yet")

    if Role_2 != None and Role_2.lower() not in roles:  # type: ignore
        raise ValueError("Role 2 not supported yet")

    if not idioma.lower() in [  # type: ignore
        "portugues",
        "english",
        None,
    ]:
        raise ValueError("Language not implemented yet.")

    if Argumentos_Disponiveis["idioma"][1] in sys.argv:
        Atualizar_Idioma(idioma)  # type: ignore

    return modo_de_jogo, Role_1, Role_2, possui_argumentos, idioma.lower()  # type: ignore
