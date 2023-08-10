# Definição das classes

class NPC:
    def __init__(self, nome, forcaAtaque):
        self.nome = nome
        self.forcaAtaque = forcaAtaque

    def Ataque(self, player):
        player.receberAtaque(self.forcaAtaque)


class Dragon(NPC):
    def __init__(self):
        super().__init__("Dragon", 15)


class Bowse(NPC):
    def __init__(self):
        super().__init__("Bowse", 10)


class Player:
    def __init__(self, nome, hp, defesa):
        self.nome = nome
        self.hp = hp
        self.defesa = defesa

    def receberAtaque(self, forcaAtaque):
        danoReal = max(0, forcaAtaque - self.defesa)
        self.hp -= danoReal


class PlayerFactory:
    @staticmethod
    def criarPlayer(nome, hp, defesa):
        return Player(nome, hp, defesa)


class NPCFactory:
    @staticmethod
    def criarNPC(nome):
        if nome == "Dragon":
            return Dragon()
        elif nome == "Bowse":
            return Bowse()
        else:
            return None


playerFactory = PlayerFactory()
npcFactory = NPCFactory()

player1 = playerFactory.criarPlayer("Mario", 100, 8)
player2 = playerFactory.criarPlayer("Joker", 120, 5)

npc1 = npcFactory.criarNPC("Dragon")
npc2 = npcFactory.criarNPC("Bowse")


npc1.Ataque(player1)
npc2.Ataque(player1)

npc2.Ataque(player2)
npc2.Ataque(player2)

print(f"HP do {player1.nome}: {player1.hp}")
print(f"HP do {player2.nome}: {player2.hp}")
