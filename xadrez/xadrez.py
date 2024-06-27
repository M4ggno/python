class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.turno = 'branco'

    def print_tabuleiro(self):
        for row in self.tabuleiro:
            print(' '.join(row))

    def move(self, inicio, destino):
        inicio_x, inicio_y = self.posicao_para_indice(inicio)
        destino_x, destino_y = self.posicao_para_indice(destino)
        peca = self.tabuleiro[inicio_x][inicio_y]
        self.tabuleiro[inicio_x][inicio_y] = ' '
        self.tabuleiro[destino_x][destino_y] = peca

        self.turno = 'preto' if self.turno == 'branco' else 'branco'

    def posicao_para_indice(self, posicao):
        colunas = 'abcdefgh'
        coluna = colunas.index(posicao[0])
        linha = 8 - int(posicao[1])
        return linha, coluna

    def jogar(self):
        while True:
            print("Tabuleiro:")
            self.print_tabuleiro()

            if self.turno == 'branco':
                print("Vez das peças brancas.")
            else:
                print("Vez das peças pretas.")
            inicio = input("Digite a posição da peça que deseja mover (ex: e2): ")
            destino = input("Digite a posição para onde deseja mover a peça (ex: e4): ")

            self.move(inicio, destino)


tab = Tabuleiro()
tab.jogar()
