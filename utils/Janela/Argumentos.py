import sys
from utils.Idioma import definir_idioma, Atualizar_Idioma

def Argumentos():
    Argumentos_Disponiveis = {
    "modo_de_jogo" : [None, "--gamemode"],
    "Role_1" : [None, "--role1"],
    "Role_2" : [None, "--role2"],
    "idioma" : [definir_idioma(), "--language"]
    }
    possui_argumentos = False
        
    def AtribuirArgumentos(variavel, string):
        nonlocal possui_argumentos
        if len(sys.argv) > 1:
            possui_argumentos = True
            args = sys.argv[1:]
            for i in range(len(args)):
                if args[i].lower() == string:
                    variavel = args[i+1]
                    try:
                        j = i
                        while not args[j+2].startswith("--"):
                            variavel += " " + args[j+2]
                            j+=1
                    except:
                        pass
                    print(variavel)
        return variavel
                    
    for chave, valor in Argumentos_Disponiveis.items():
        globals()[f"{chave}"] = valor[0]
        globals()[f"{chave}"] = AtribuirArgumentos(globals()[f"{chave}"], valor[1])
    
    if Argumentos_Disponiveis["idioma"][1] in sys.argv:
        Atualizar_Idioma(idioma) #type: ignore
                
    return modo_de_jogo, Role_1, Role_2, possui_argumentos, idioma #type: ignore