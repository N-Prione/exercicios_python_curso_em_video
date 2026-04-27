from rich.panel import Panel
from rich import print

class ControleRemoto:
    vol_min:int = 1
    vol_max:int = 10
    ch_min:int = 1
    ch_max:int = 6

    def __init__(self, canal = 1, volume = 5):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False
    
    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.liga_desliga:
            if self.canal_atual == ControleRemoto.ch_max:
                self.canal_atual = ControleRemoto.ch_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.liga_desliga:
            if self.canal_atual == ControleRemoto.ch_min:
                self.canal_atual = ControleRemoto.ch_max
            else:
                self.canal_atual -= 1

    def vol_mais(self):
        if self.liga_desliga:
            if self.volume_atual != ControleRemoto.vol_max:
                self.volume_atual += 1

    def vol_menos(self):
        if self.liga_desliga:
            if self.volume_atual != ControleRemoto.vol_min:
                self.volume_atual -= 1

    def painel(self):
        if self.ligado == False:
            texto = 'TV Desligada'
        else:
            texto = f'CANAL  = '
            for canais in range(ControleRemoto.ch_min, ControleRemoto.ch_max+1):
                if canais == self.canal_atual:
                    texto += f'[black on white] {canais} [/]'
                else:
                    texto += f' {canais} '

            texto += '\nVOLUME = '
            for vol in range(ControleRemoto.vol_min, ControleRemoto.vol_max+1):
                if vol <= self.volume_atual:
                    texto += '[black on red] [/]'
                else:
                    texto += '[black on white] [/]'

        tv = Panel(texto, title=' --- TELEVISÃO ---', width=45)
        print(tv)

tv = ControleRemoto()
while True:
    tv.painel()
    print('(@ liga) -- (* sair)')
    comando = input('< CH >   + VOL -  ')
    match comando:
        case '@':
            tv.liga_desliga()
        case '*':
            break
        case '<':
            tv.canal_menos()
        case '>':
            tv.canal_mais()
        case '+':
            tv.vol_mais()
        case '-':
            tv.vol_menos()