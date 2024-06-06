import os
import subprocess
import pygetwindow as gw
import time


def encontrar_e_salvar_pasta_instalacao_lol(unidade, flagPF):
    unidade = unidade + "\\"
    global pasta_instalacao
    pasta_instalacao = None

    if flagPF == 1:

        pastas_padrao = rf"{unidade}\Riot Games\League of Legends"

        for pasta in pastas_padrao:
            if os.path.exists(pastas_padrao):
                pasta_instalacao = pastas_padrao
                pasta_instalacao = os.path.dirname(pasta_instalacao)
                pasta_instalacao = os.path.join(
                    pasta_instalacao, "Riot Client", "RiotClientServices.exe"
                )
                pasta_instalacao = pasta_instalacao.replace("\\\\", "\\")

                LOL_path = os.path.join(
                    os.path.expanduser("~"),
                    "League Lobby Clicker - Saralapa",
                    "League_Lobby_Clicker_LOL_path-Saralapa.txt",
                )
                LOL_path = LOL_path.replace("\\\\", "\\")
                with open(LOL_path, "w") as arquivo:
                    arquivo.write(pasta_instalacao)

                if pasta_instalacao:
                    return 23
                return

        for pasta, subpastas, arquivos in os.walk(unidade):
            if (
                "Program Files" in pasta
                or "ProgramData" in pasta
                or "AppData" in pasta
                or "Windows" in pasta
            ):
                del subpastas[:]
                continue
            if "League of Legends" in subpastas and "Riot Games" in pasta:
                pasta_instalacao = os.path.join(
                    pasta, "Riot Client", "RiotClientServices.exe"
                )
                pasta_instalacao = pasta_instalacao.replace(
                    f"{unidade}", f"{unidade}\\"
                )

                LOL_path = os.path.join(
                    os.path.expanduser("~"),
                    "League Lobby Clicker - Saralapa",
                    "League_Lobby_Clicker_LOL_path-Saralapa.txt",
                )
                LOL_path = LOL_path.replace("\\\\", "\\")
                with open(LOL_path, "w") as arquivo:
                    arquivo.write(pasta_instalacao)

                return 23

            if pasta_instalacao:
                return

        if not pasta_instalacao:
            print("A pasta de instalação do League of Legends não foi encontrada.")

    elif flagPF == 2:
        for pasta, subpastas, arquivos in os.walk(unidade):
            print(pasta, subpastas, arquivos)

            if "Riot Client" in subpastas and "League of Legends" in subpastas:
                riot_client_index = subpastas.index("Riot Client")
                lol_index = subpastas.index("League of Legends")

                if lol_index == riot_client_index + 1:
                    pasta_instalacao = os.path.join(
                        pasta, "Riot Client", "RiotClientServices.exe"
                    )
                    pasta_instalacao = pasta_instalacao.replace(
                        f"{unidade}", f"{unidade}\\"
                    )

                    LOL_path = os.path.join(
                        os.path.expanduser("~"),
                        "League Lobby Clicker - Saralapa",
                        "League_Lobby_Clicker_LOL_path-Saralapa.txt",
                    )
                    LOL_path = LOL_path.replace("\\\\", "\\")
                    with open(LOL_path, "w") as arquivo:
                        arquivo.write(pasta_instalacao)

                    return 23

            if pasta_instalacao:
                return

        if not pasta_instalacao:
            print("A pasta de instalação do League of Legends não foi encontrada.")


def chamar_funcao_encontrar_pasta_LOL():
    if not os.path.exists(
        os.path.join(os.path.expanduser("~"), "League Lobby Clicker - Saralapa")
    ):
        os.mkdir(
            os.path.join(os.path.expanduser("~"), "League Lobby Clicker - Saralapa")
        )
    unidades = [
        f"{disco}:"
        for disco in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if os.path.exists(f"{disco}:")
    ]
    if not [
        window
        for window in gw.getWindowsWithTitle("League of Legends")
        if window.title == "League of Legends"
    ]:
        LOL_path = os.path.join(
            os.path.expanduser("~"),
            "League Lobby Clicker - Saralapa",
            "League_Lobby_Clicker_LOL_path-Saralapa.txt",
        )
        LOL_path = LOL_path.replace("\\\\", "\\")

        if not os.path.exists(LOL_path):
            for unidade in unidades:
                if encontrar_e_salvar_pasta_instalacao_lol(unidade, 1) == 23:
                    break
            if pasta_instalacao == None:
                for unidade in unidades:
                    if encontrar_e_salvar_pasta_instalacao_lol(unidade, 2) == 23:
                        break

        try:
            with open(LOL_path, "r") as file:
                subprocess.Popen(
                    [
                        file.read().strip(),
                        "--launch-product=league_of_legends",
                        "--launch-patchline=live",
                    ]
                )
        except:
            try:
                os.remove(LOL_path)
            except:
                None
            for unidade in unidades:
                if encontrar_e_salvar_pasta_instalacao_lol(unidade, 1) == 23:
                    break
            if pasta_instalacao == None:
                for unidade in unidades:
                    if encontrar_e_salvar_pasta_instalacao_lol(unidade, 2) == 23:
                        break
            time.sleep(0.5)
            try:
                with open(LOL_path, "r") as file:
                    subprocess.Popen(
                        [
                            file.read().strip(),
                            "--launch-product=league_of_legends",
                            "--launch-patchline=live",
                        ]
                    )
            except:
                None
