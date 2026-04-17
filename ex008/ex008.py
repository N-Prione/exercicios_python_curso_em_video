from rich.panel import Panel
from rich import print

class Gamer:
    def __init__(self, name, nick_name):
        self.name = name
        self.nick_name = nick_name
        self.jogos_fav = []

    def add_favoritos(self, jogo):
        self.jogos_fav.append(jogo)
        self.jogos_fav.sort()

    def ficha(self):
        texto = f'''Nome do jogador: [red on white] {self.name} [/]
Jogos Favoritos:'''
        for jogo in self.jogos_fav:
            texto += f'\n:joystick: [yellow]{jogo}[/]'
        painel = Panel(texto, title=f'Jogador << [green]{self.nick_name}[/] >>', width=45)
        print(painel)

jogador1 = Gamer('Pedro Henrique', 'troll_selvagem')
jogador1.add_favoritos('God Of War')
jogador1.add_favoritos('Subnautica')
jogador1.add_favoritos('Mortal Kombat')
jogador1.add_favoritos('Allan Walker')
jogador1.ficha()

jogador2 = Gamer('Gabriela Silva', 'safira_noturna')
jogador2.add_favoritos('Zelda')
jogador2.add_favoritos('Mario Card')
jogador2.add_favoritos('Stardew Valley')
jogador2.add_favoritos('Hogwards Legacy')
jogador2.ficha()