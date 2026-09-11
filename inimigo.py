class Enemy:

    def __init__(self, nome, hp, ataque, defesa):
        self.nome = nome
        self.hp = hp
        self.hp_max = hp
        self.ataque = ataque
        self.defesa = defesa

    def receber_dano(self, dano):
        self.hp -= dano

        if self.hp < 0:
            self.hp = 0

    def esta_vivo(self):
        return self.hp > 0

    def mostrar_status(self):
        print()
        print("INIMIGO")
        print("Nome:", self.nome)
        print("HP:", self.hp)
        print("Ataque:", self.ataque)
        print("Defesa:", self.defesa)