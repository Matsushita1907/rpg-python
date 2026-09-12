def calcular_dano(ataque, defesa):
    dano = ataque - (defesa // 2)

    if dano < 0:
        dano = 0

    return dano

def batalha(jogador, inimigo):

    print()
    print("INIMIGO ENCONTRADO")

    inimigo.mostrar_status()

    while jogador.esta_vivo() and inimigo.esta_vivo():

        print()
        print("BATALHA")

        print("Seu HP:", jogador.hp)
        print("HP do", inimigo.nome + ":", inimigo.hp)

        print()
        print("[1] Ataque normal")
        print("[2] Ataque forte")
        print("[3] Defender")
        print("[4] Fugir")

        acao = input("Escolha sua ação: ")

        if acao == "1":

            print()
            print("Você atacou o", inimigo.nome + "!")

            dano = jogador.ataque
            inimigo.receber_dano(dano)

            print("Você causou", dano, "de dano!")
            print("HP do inimigo:", inimigo.hp)