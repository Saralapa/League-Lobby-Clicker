from utils.Encontrar_Pasta import chamar_funcao_encontrar_pasta_LOL
from utils.Atualizacoes import Verificar_Atualizacoes
from utils.Janela.Janela import Criar_Janela

if __name__ == "__main__":
    chamar_funcao_encontrar_pasta_LOL()
    if Verificar_Atualizacoes() != "yes":
        Criar_Janela()
