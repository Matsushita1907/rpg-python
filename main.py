print ("-----RPG BATTLEGROUND-----")
nome = input("Digite o nome do seu personagem: ")
print ("Seja bem vindo,", nome)
print ("Escolha a sua classe !")
print("1 Guerreiro")
print("2 Mago")
print("3 Arqueiro")

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

print()
print("Personagem criado ! ")
print("Nome", nome)
print("classe", classe)
print("hp", hp)
print("Ataque", ataque)
print("Defesa", defesa)

inimigo_nome = "Goblin"
inimigo_hp = 50
inimigo_ataque = 10

print()
print("Um inimigo apareceu!")
print("Inimigo:", inimigo_nome)
print("HP:", inimigo_hp)