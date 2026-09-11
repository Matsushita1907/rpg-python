print("        RPG BATTLEGROUND")

def mostrar_ficha(nome, classe, hp, ataque, defesa):
    print()
    print("PERSONAGEM CRIADO")

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
inimigo_hp = 50
inimigo_ataque = 10


print()
print("INIMIGO ENCONTRADO")

print("Inimigo:", inimigo_nome)
print("HP:", inimigo_hp)


while hp > 0 and inimigo_hp > 0:

    print()
    print("[1] Atacar")
    print("[2] Fugir")

    acao = input("O que você quer fazer? ")


    if acao == "1":

        print()
        print("Você atacou o", inimigo_nome)

        inimigo_hp = inimigo_hp - ataque

        print("O", inimigo_nome, "perdeu", ataque, "de HP!")
        print("HP do inimigo:", inimigo_hp)


        if inimigo_hp <= 0:

            print()
            print("O", inimigo_nome, "morreu!")

        else:

            print()
            print("O", inimigo_nome, "atacou você!")

            dano = inimigo_ataque - (defesa // 2)

        if dano < 0:
            dano = 0

        hp = hp - dano
        print("Você perdeu", dano, "de HP!")
        print("Seu HP:", hp)

    elif acao == "2":

        print()
        print("Você fugiu da batalha!")
        break


    else:

        print()
        print("❌ Opção inválida!")




print()
print("          FIM DA BATALHA")


if hp <= 0:

    print("Você morreu!")

elif inimigo_hp <= 0:

    print("Você venceu!")
    print("Você derrotou o", inimigo_nome)

else:

    print("Você fugiu da batalha!")
