print ("-----RPG BATTLEGROUND-----")
nome = input("Digite o nome do seu personagem: ")
print ("Seja bem vindo,", nome)
print ("Escolha a sua classe !")
print("1 Guerreiro")
print("2 Mago")
print("3 Arqueiro")

classe = input("Escolha sua classe: ")

if classe == "1":
    print("Você é um guerreiro !")
elif classe == "2":
    print("Você é um mago !")
elif classe == "3":
    print("Você é um arqueiro !")
else:
    print("opção invalida")

