def atualizar_mensagem():
    from utils.Janela.Janela import idioma
    if idioma=="Portugues":
        mensagens = ["Encontrando partida"]
        for i in range(1,4):
            mensagens.append(mensagens[0] + "." * i)
    elif idioma=="English":
        mensagens = ["Finding match"]
        for i in range(1,4):
            mensagens.append(mensagens[0] + "." * i)
    i = 0
    while True:
        from utils.Janela.Janela import tela, label_auto_aceitar, time
        if tela != "auto aceitar":
            return
        try:
            label_auto_aceitar.config(text=mensagens[i])
            i = (i + 1) % len(mensagens)
            time.sleep(0.75)
        except:
            None