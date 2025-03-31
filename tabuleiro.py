class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [' ' for _ in range(9)]
        self.vitorias = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]

    def verificar_vitoria(self, jogador):
        for vitoria in self.vitorias:
            if self.tabuleiro[vitoria[0]] == self.tabuleiro[vitoria[1]] == self.tabuleiro[vitoria[2]] == jogador:
                return True
        return False

    def tabuleiro_cheio(self):
        return ' ' not in self.tabuleiro

    def fazer_jogada(self, pos, jogador):
        if self.tabuleiro[pos] == ' ':
            self.tabuleiro[pos] = jogador
            return True
        return False

    def limpar_casa(self, pos):
        self.tabuleiro[pos] = ' '
