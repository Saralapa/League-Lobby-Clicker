import sys

def Argumentos():
    modo_de_jogo = None
    Role_1 = None
    Role_2 = None
    possui_argumentos = False
    if len(sys.argv) > 1:
        possui_argumentos = True
        args = sys.argv[1:]
        for i in range(len(args)):
            if args[i].lower() == "--gamemode":
                modo_de_jogo = args[i+1]
                print(modo_de_jogo)
            elif args[i].lower() == "--role1":
                Role_1 = args[i+1]
                print(Role_1)
            elif args[i].lower() == "--role2":
                Role_2 = args[i+1]
                print(Role_2)
                
        return modo_de_jogo, Role_1, Role_2, possui_argumentos
    
    return modo_de_jogo, Role_1, Role_2, possui_argumentos