import tkinter as tk
from jogo_da_velha import JogoDaVelha

def escolher_modo(root):
    for widget in root.winfo_children():
        widget.destroy()

    frame_menu = tk.Frame(root)
    frame_menu.pack(padx=20, pady=20)

    titulo = tk.Label(frame_menu, text="Escolha o Modo de Jogo", font=("Arial", 18))
    titulo.pack()

    def selecionar_dificuldade(modo):
        for widget in root.winfo_children():
            widget.destroy()

        frame_dificuldade = tk.Frame(root)
        frame_dificuldade.pack(padx=20, pady=20)

        titulo = tk.Label(frame_dificuldade, text="Escolha a Dificuldade", font=("Arial", 18))
        titulo.pack()

        botao_normal = tk.Button(frame_dificuldade, text="Normal", width=20, height=2, font=("Arial", 14),
                                 command=lambda: JogoDaVelha(root, modo, escolher_modo, 9))
        botao_normal.pack(pady=10)

        botao_dificil = tk.Button(frame_dificuldade, text="Morte Subita", width=20, height=2, font=("Arial", 14),
                                  command=lambda: JogoDaVelha(root, modo, escolher_modo,6))
        botao_dificil.pack(pady=10)

    botao_1player = tk.Button(frame_menu, text="1 Jogador (vs IA)", width=20, height=2, font=("Arial", 14),
                              command=lambda: selecionar_dificuldade("1"))
    botao_1player.pack(pady=10)

    botao_2players = tk.Button(frame_menu, text="2 Jogadores", width=20, height=2, font=("Arial", 14),
                                command=lambda: selecionar_dificuldade("2")) 
    botao_2players.pack(pady=10)


root = tk.Tk()
escolher_modo(root)
root.mainloop()
