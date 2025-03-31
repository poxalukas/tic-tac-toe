import tkinter as tk
import math
from tabuleiro import Tabuleiro

class JogoDaVelha:
    def __init__(self, root, modo_jogo, voltar_menu, dificuldade):
        self.root = root
        self.modo_jogo = modo_jogo
        self.tabuleiro = Tabuleiro()
        self.jogador_turno = True
        self.voltar_menu = voltar_menu 
        self.jogando = True
        self.historico_jogadas = [] 
        self.botao_tabuleiro = [None for _ in range(9)]
        self.limite_jogadas = dificuldade

        for widget in root.winfo_children():
            widget.destroy()

        for i in range(9):
            botao = tk.Button(root, text=' ', width=10, height=3, font=('Arial', 24),
                              command=lambda i=i: self.fazer_jogada(i))
            botao.grid(row=i // 3, column=i % 3)
            self.botao_tabuleiro[i] = botao

        self.mensagem = tk.Label(root, text="É sua vez, jogador X!", font=('Arial', 16))
        self.mensagem.grid(row=3, column=0, columnspan=3)

        self.botao_reiniciar = tk.Button(root, text="Reiniciar", font=('Arial', 14), command=lambda: self.voltar_menu(root))       
        self.botao_reiniciar.grid(row=4, column=0, columnspan=3, pady=10)

    def exibir_tabuleiro(self):
        for i in range(9):
            self.botao_tabuleiro[i].config(text=self.tabuleiro.tabuleiro[i])

    def fazer_jogada(self, pos):
        if not self.jogando:
            return

        jogador = 'X' if self.jogador_turno else 'O'
        if self.tabuleiro.fazer_jogada(pos, jogador):
            self.historico_jogadas.append(pos)

            if len(self.historico_jogadas) > self.limite_jogadas:
                jogada_removida = self.historico_jogadas.pop(0)
                self.tabuleiro.limpar_casa(jogada_removida)

            self.exibir_tabuleiro()

            if self.tabuleiro.verificar_vitoria(jogador):
                self.mensagem.config(text=f"Jogador {jogador} venceu!")
                self.jogando = False
                return
            elif self.tabuleiro.tabuleiro_cheio():
                self.mensagem.config(text="Empate!")
                self.jogando = False
                return

            self.jogador_turno = not self.jogador_turno
            jogador_atual = 'X' if self.jogador_turno else 'O'
            self.mensagem.config(text=f"É a vez do jogador {jogador_atual}!")

            if not self.jogador_turno and self.modo_jogo == "1":
                self.root.after(500, self.ia_jogar)  

    def ia_jogar(self):
        posicao = self.melhor_jogada()
        self.fazer_jogada(posicao)

    def melhor_jogada(self):
        melhor_valor = -math.inf
        melhor_movimento = -1

        for i in range(9):
            if self.tabuleiro.tabuleiro[i] == ' ':
                self.tabuleiro.tabuleiro[i] = 'O'
                valor = self.minimax(False, -math.inf, math.inf)
                self.tabuleiro.tabuleiro[i] = ' '

                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_movimento = i

        return melhor_movimento

    def minimax(self, maximizando, alpha, beta):
        if self.tabuleiro.verificar_vitoria('O'):
            return 10
        elif self.tabuleiro.verificar_vitoria('X'):
            return -10
        elif self.tabuleiro.tabuleiro_cheio():
            return 0

        if maximizando:
            melhor_valor = -math.inf
            for i in range(9):
                if self.tabuleiro.tabuleiro[i] == ' ':
                    self.tabuleiro.tabuleiro[i] = 'O'
                    valor = self.minimax(False, alpha, beta)
                    self.tabuleiro.tabuleiro[i] = ' '
                    melhor_valor = max(melhor_valor, valor)
                    alpha = max(alpha, valor)
                    if beta <= alpha:
                        break
            return melhor_valor
        else:
            melhor_valor = math.inf
            for i in range(9):
                if self.tabuleiro.tabuleiro[i] == ' ':
                    self.tabuleiro.tabuleiro[i] = 'X'
                    valor = self.minimax(True, alpha, beta)
                    self.tabuleiro.tabuleiro[i] = ' '
                    melhor_valor = min(melhor_valor, valor)
                    beta = min(beta, valor)
                    if beta <= alpha:
                        break
            return melhor_valor
