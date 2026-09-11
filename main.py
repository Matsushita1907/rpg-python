print("RPG BATTLEGROUND")

# Funções para exibir informações do personagem
def mostrar_ficha(nome, classe, hp, ataque, defesa):
    print()
    print("PERSONAGEM CRIADO")
    print("Nome:", nome)
    print("Classe:", classe)
    print("HP:", hp)
    print("Ataque:", ataque)
    print("Defesa:", defesa)


def mostrar_status(nome, classe, hp, ataque, defesa):
    print()
    print("STATUS")
    print("Nome:", nome)
    print("Classe:", classe)
    print("HP:", hp)
    print("Ataque:", ataque)
    print("Defesa:", defesa)

nome = input("Digite o nome do seu personagem: ")

print()
print("Escolha sua classe:")
print("[1] Guerreiro")
print("[2] Mago")
print("[3] Arqueiro")

classe = input("Escolha sua classe: ")

if classe == "1":

    classe = "Guerreiro"
    hp = 120
    ataque = 25
    defesa = 20

elif classe == "2":

    classe = "Mago"
    hp = 80
    ataque = 40
    defesa = 10

elif classe == "3":

    classe = "Arqueiro"
    hp = 100
    ataque = 30
    defesa = 15

else:

    print("Opção inválida!")
    exit()

mostrar_ficha(nome, classe, hp, ataque, defesa)

inimigo_nome = "Goblin"
inimigo_hp = 80
inimigo_ataque = 25


print()
print("INIMIGO ENCONTRADO")
print("Inimigo:", inimigo_nome)
print("HP:", inimigo_hp)
print("Ataque:", inimigo_ataque)

while hp > 0 and inimigo_hp > 0:

    print()
    print("           BATALHA")

    print("Seu HP:", hp)
    print("HP do", inimigo_nome + ":", inimigo_hp)

    print()
    print("[1] Ataque normal")
    print("[2] Ataque forte")
    print("[3] Defender")
    print("[4] Fugir")

    acao = input("Escolha sua ação: ")


    if acao == "1":

        print()
        print("⚔️ Você atacou o", inimigo_nome + "!")

        dano = ataque

        inimigo_hp = inimigo_hp - dano

        print("Você causou", dano, "de dano!")
        print("HP do inimigo:", inimigo_hp)

        if inimigo_hp <= 0:

            print()
            print("O", inimigo_nome, "morreu!")

        else:


            print()
            print("O", inimigo_nome, "atacou você!")

            dano_inimigo = inimigo_ataque - (defesa // 2)

            if dano_inimigo < 0:
                dano_inimigo = 0

            hp = hp - dano_inimigo

            print("Você perdeu", dano_inimigo, "de HP!")
            print("Seu HP:", hp)

    elif acao == "2":

        print()
        print("Você usou um ATAQUE FORTE!")

        dano_forte = ataque * 2

        inimigo_hp = inimigo_hp - dano_forte

        print("Você causou", dano_forte, "de dano!")
        print("HP do inimigo:", inimigo_hp)

        if inimigo_hp <= 0:

            print()
            print("O", inimigo_nome, "morreu!")

        else:

            print()
            print("O", inimigo_nome, "atacou você!")

            dano_inimigo = inimigo_ataque - (defesa // 2)

            if dano_inimigo < 0:
                dano_inimigo = 0

            hp = hp - dano_inimigo

            print("Você perdeu", dano_inimigo, "de HP!")
            print("Seu HP:", hp)

    elif acao == "3":

        print()
        print("Você entrou em posição defensiva!")

        dano_inimigo = inimigo_ataque - defesa

        if dano_inimigo < 0:
            dano_inimigo = 0

        hp = hp - dano_inimigo

        print("O", inimigo_nome, "atacou!")
        print("Você bloqueou parte do ataque!")
        print("Você perdeu", dano_inimigo, "de HP!")
        print("Seu HP:", hp)


    elif acao == "4":

        print()
        print("🏃 Você fugiu da batalha!")

        break

    else:

        print()
        print("❌ Opção inválida!")


print()
print("          FIM DA BATALHA")

if hp <= 0:

    print("Você morreu!")
    print("Fim de jogo.")


elif inimigo_hp <= 0:

    print("🏆 Você venceu!")
    print("💰 Você derrotou o", inimigo_nome + "!")

else:

    print("🏃 Você fugiu da batalha!")

if hp > 0:

    print()
    print("STATUS FINAL")
    print("Nome:", nome)
    print("Classe:", classe)
    print("HP:", hp)
    print("Ataque:", ataque)
    print("Defesa:", defesa)
