import jogo_da_velha

game = jogo_da_velha.Game()

while game.winner == 0:
    game.play(input("Escolha uma posição no tabuleiro. \n"))
    game.checkWinner()

if game.winner == -1:
    print("Empate")
else:
    print(f'Jogador {game.winner} ganhou')
