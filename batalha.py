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

        elif acao == "2":

            print()
            print("Você usou um ATAQUE FORTE!")

            dano = jogador.ataque * 2
            inimigo.receber_dano(dano)

            print("Você causou", dano, "de dano!")
            print("HP do inimigo:", inimigo.hp)

        elif acao == "3":

            print()
            print("Você entrou em posição defensiva!")

            dano = inimigo.ataque - jogador.defesa

            if dano < 0:
                dano = 0

            jogador.receber_dano(dano)

            print("O", inimigo.nome, "atacou!")
            print("Você bloqueou parte do ataque!")
            print("Você perdeu", dano, "de HP!")
             
        elif acao == "4":

            print()
            print("Você fugiu da batalha!")

            return "fugiu"
        
        else:

            print()
            print("Opção inválida!")

            continue

        if inimigo.esta_vivo():

            dano = calcular_dano(inimigo.ataque, jogador.defesa)

            jogador.receber_dano(dano)

            print()
            print(inimigo.nome, "atacou você!")
            print("Você perdeu", dano, "de HP!")        