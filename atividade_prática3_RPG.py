from time import sleep
class Seres_Vivos:
    def __init__(self, ponto_de_vida, ponto_de_ataque):
        self.ponto_de_vida = ponto_de_vida
        self.ponto_de_ataque = ponto_de_ataque
    
    def causar_dano(self, alvo): #o alvo vai ser o objeto que está sendo atacado
        pontos_ganhos = self.ponto_de_ataque #os pontos ganhos com o ataque vão aumentar os pontos de ataque do atacante e diminuir os pontos de vida do atacado
        alvo.ponto_de_vida -= pontos_ganhos #diminui os pontos ganhos dos pontos de vida do alvo
        print(f'{self.__class__.__name__} causou {pontos_ganhos} pontos de dano em {alvo.__class__.__name__}!')
        if pontos_ganhos >= 30:
            sleep(2)
            print('SUPER-ATAQUE!!')
            sleep(1)
        print(f'{alvo.__class__.__name__} agora possui {alvo.ponto_de_vida} pontos de vida!!')
        if alvo.ponto_de_vida > 0:
            sleep(2)
            print('A BATALHA CONTINUA!')
            sleep(1)
        else:
            sleep(2)
            print('GAME OVER')

class Personagem(Seres_Vivos):
    def __init__(self, ponto_de_vida, ponto_de_ataque, nome):
        super().__init__(ponto_de_ataque, ponto_de_vida)
        self.nome = nome

class Monstro(Seres_Vivos):
    def __init__(self, ponto_de_vida, ponto_de_ataque, tipo):
        super().__init__(ponto_de_ataque, ponto_de_vida)
        self.tipo = tipo

class Lobo(Monstro):
    def __init__(self, ponto_de_vida, ponto_de_ataque, tipo, força):
        super().__init__(ponto_de_ataque, ponto_de_vida, tipo)
        self.força = força

class Goblin(Monstro):
    def __init__(self, ponto_de_vida, ponto_de_ataque, tipo, inteligencia):
        super().__init__(ponto_de_ataque, ponto_de_vida, tipo)
        self.inteligencia = inteligencia

goblinzinho = Goblin(90, 15, 'Pantanoso', 'Estrategista') #está com 60 pts de vida, e seu ataque causa 15 pts de dano
Lobinho = Lobo(50, 30, 'Lobo Alfa', 'Planetária') #está com 50 pts de vida e seu ataque causa 30 pts de dano
Lobinho.causar_dano(goblinzinho)
Lobinho.causar_dano(goblinzinho)
Lobinho.causar_dano(goblinzinho)

#atacar = recebe a quantidade de dano que pode causar e a quantidade de vida que o outro perdeu
#ataque É o dano causado
#qual ser vivo (personagem) vão receber esse dano
