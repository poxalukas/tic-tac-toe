# Jogo da Velha (Tic-Tac-Toe)

## Visão Geral
Este projeto implementa um jogo da velha (tic-tac-toe) utilizando a biblioteca Tkinter para a interface gráfica. O jogo pode ser jogado entre dois jogadores ou contra uma IA que utiliza o algoritmo Minimax para tomar decisões estratégicas. O objetivo é alinhar três símbolos iguais em uma linha, coluna ou diagonal antes do adversário.

## Tecnologias Utilizadas
- Python 3.x
- Tkinter (Interface Gráfica)
- Algoritmo Minimax (para a IA)

## Arquitetura
O projeto está organizado nas seguintes partes:

### Interface Gráfica (Tkinter)
Responsável pela criação dos elementos visuais do jogo, incluindo botões para as jogadas, mensagens de status e botões de reinício.

### Lógica do Jogo
Implementa as regras do jogo da velha, incluindo verificação de vitórias, empates e alternância de turnos entre os jogadores.

### Inteligência Artificial (Minimax)
Utiliza o algoritmo Minimax para calcular as melhores jogadas e desafiar o jogador.

## Como Rodar o Projeto
1. Certifique-se de ter o Python 3 instalado em seu computador.
2. Clone este repositório ou faça o download do código-fonte.
3. No terminal ou prompt de comando, navegue até a pasta do projeto e execute:
   ```bash
   python main.py
   ```
4. A interface gráfica do jogo será aberta e você poderá escolher o modo de jogo.

## Estrutura do Código
### Classe `JogoDaVelha`
Controla a execução do jogo e gerencia a interação entre o jogador e o tabuleiro.

- **Atributos:**
  - `root`: Referência à janela principal do Tkinter.
  - `modo_jogo`: Define se o jogo é para 1 ou 2 jogadores.
  - `tabuleiro`: Instância da classe `Tabuleiro`, que gerencia o estado do jogo.
  - `jogador_turno`: Booleano que indica de quem é a vez (True para 'X', False para 'O').
  - `botao_tabuleiro`: Lista de botões representando o tabuleiro.

- **Principais Métodos:**
  - `exibir_tabuleiro()`: Atualiza a interface gráfica do tabuleiro.
  - `fazer_jogada(pos)`: Registra a jogada e verifica vitórias ou empates.
  - `ia_jogar()`: Faz a IA calcular e executar sua jogada.
  - `minimax(maximizando, alpha, beta)`: Implementa o algoritmo Minimax para escolher a melhor jogada.

### Classe `Tabuleiro`
Gerencia o estado do jogo e verifica vitórias ou empates.

- **Métodos principais:**
  - `fazer_jogada(pos, jogador)`: Marca a jogada no tabuleiro.
  - `verificar_vitoria(jogador)`: Verifica se o jogador venceu.
  - `tabuleiro_cheio()`: Retorna True se todas as casas estiverem ocupadas.

## Base de Dados
O jogo não utiliza banco de dados, pois todas as informações são mantidas em memória durante a execução.

