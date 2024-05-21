import sys
from utils.Idioma import definir_idioma, Atualizar_Idioma

def Argumentos():
    """
    Processa os argumentos de linha de comando fornecidos ao script.
    
    Esta função analisa os argumentos de linha de comando para configurar o modo de jogo,
    as roles e o idioma. Os argumentos são especificados através de flags como --gamemode,
    --role1, --role2 e --language. Se um idioma é especificado, a função também atualiza
    o idioma do sistema.
    
    Returns:
        tuple: Retorna uma tupla contendo o modo de jogo, Role_1, Role_2, um booleano indicando
               se algum argumento foi fornecido, e o idioma configurado, todos como strings.
               O booleano possui_argumentos é True se algum argumento foi fornecido; caso contrário, False.
    """
    Argumentos_Disponiveis = {
    "modo_de_jogo" : [None, "--gamemode"],
    "Role_1" : [None, "--role1"],
    "Role_2" : [None, "--role2"],
    "idioma" : [definir_idioma(), "--language"]
    }
    possui_argumentos = False
        
    def AtribuirArgumentos(variavel, string):
        """
        Atribui valores aos argumentos com base nos parâmetros de linha de comando.
        
        Args:
            variavel (str): A variável que será atribuída com o valor do argumento.
            string (str): A string que identifica o argumento na linha de comando.
        
        Returns:
            str: O valor do argumento após ser processado.
        """
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
                
    return modo_de_jogo, Role_1, Role_2, possui_argumentos, idioma.lower() #type: ignore #type: ignore