class Player:

    def __init__(self, nome, classe, hp, ataque, defesa):
        self.nome = nome
        self.classe = classe
        self.hp = hp
        self.hp_max = hp
        self.ataque = ataque
        self.defesa = defesa

    def mostrar_ficha(self):
        print()
        print("PERSONAGEM CRIADO")
        print("Nome:", self.nome)
        print("Classe:", self.classe)
        print("HP:", self.hp)
        print("Ataque:", self.ataque)
        print("Defesa:", self.defesa)

    def receber_dano(self, dano):
        self.hp -= dano

        if self.hp < 0:
            self.hp = 0

    def esta_vivo(self):
        return self.hp > 0
