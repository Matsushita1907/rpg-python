def calcular_dano(ataque, defesa):
    dano = ataque - (defesa // 2)

    if dano < 0:
        dano = 0

    return dano
