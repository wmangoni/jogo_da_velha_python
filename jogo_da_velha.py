class Game:
    """Classe que representa o jogo da velha
        Exemplo of tabuleiro
        [A][B][C]
        [D][E][F]
        [G][H][I]
    """

    X = "X"

    O = "O"

    tabuleiro = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

    turn = 0

    turnA = True

    winner = 0

    switcher = {
        "A": "0-0",
        "B": "0-1",
        "C": "0-2",
        "D": "1-0",
        "E": "1-1",
        "F": "1-2",
        "G": "2-0",
        "H": "2-1",
        "I": "2-2"
    }

    def __init__(self):
        self.tabuleiro[0][0] = " "
        self.tabuleiro[0][1] = " "
        self.tabuleiro[0][2] = " "
        self.tabuleiro[1][0] = " "
        self.tabuleiro[1][1] = " "
        self.tabuleiro[1][2] = " "
        self.tabuleiro[2][0] = " "
        self.tabuleiro[2][1] = " "
        self.tabuleiro[2][2] = " "

        print("----Jogo da velha----")
        print("Estas são as posições disponíveis no tabuleiro.")
        print(f'[A][B][C]')
        print(f'[D][E][F]')
        print(f'[G][H][I]')

    def play(self, place):
        if self.turnA:
            self.setPosition(place.upper(), self.X)
            self.turnA = False
        else:
            self.setPosition(place.upper(), self.O)
            self.turnA = True

        self.showTabuleiro()
        self.turn += self.turn

    def setPosition(self, letter, player):
        if not letter in ("A", "B", "C", "D", "E", "F", "G", "H", "I"):
            print("posição inválida, escolha outra")
            return

        pos = self.switcher[letter].split("-")
        pos1 = int(pos[0])
        pos2 = int(pos[1])

        if self.tabuleiro[pos1][pos2] == self.X or self.tabuleiro[pos1][pos2] == self.O:
            print("posição inválida, escolha outra")
            return

        self.tabuleiro[pos1][pos2] = player

    def showTabuleiro(self):
        print(f'[A][B][C] | [{self.tabuleiro[0][0]}][{self.tabuleiro[0][1]}][{self.tabuleiro[0][2]}]')
        print(f'[D][E][F] | [{self.tabuleiro[1][0]}][{self.tabuleiro[1][1]}][{self.tabuleiro[1][2]}]')
        print(f'[G][H][I] | [{self.tabuleiro[2][0]}][{self.tabuleiro[2][1]}][{self.tabuleiro[2][2]}]')
        print("-----------------------------")

    def checkWinner(self):
        if self.checkLine(0, self.X) or self.checkLine(1, self.X) or self.checkLine(2, self.X):
            self.winner = 1
            return

        if self.checkLine(0, self.O) or self.checkLine(1, self.O) or self.checkLine(2, self.O):
            self.winner = 2
            return

        if self.checkColunm(0, self.X) or self.checkColunm(1, self.X) or self.checkColunm(2, self.X):
            self.winner = 1
            return

        if self.checkColunm(0, self.O) or self.checkColunm(1, self.O) or self.checkColunm(2, self.O):
            self.winner = 2
            return

        if self.checkDiagA(self.X) or self.checkDiagB(self.X):
            self.winner = 1

        if self.checkDiagA(self.O) or self.checkDiagB(self.O):
            self.winner = 2

        if self.tabuleiroCheio():
            self.winner = -1

    def checkLine(self, line, player):
        return self.tabuleiro[line][0] == player and self.tabuleiro[line][1] == player and self.tabuleiro[line][
            2] == player

    def checkColunm(self, col, player):
        return self.tabuleiro[0][col] == player and self.tabuleiro[1][col] == player and self.tabuleiro[2][
            col] == player

    def checkDiagA(self, player):
        return self.tabuleiro[0][0] == player and self.tabuleiro[1][1] == player and self.tabuleiro[2][2] == player

    def checkDiagB(self, player):
        return self.tabuleiro[0][2] == player and self.tabuleiro[1][1] == player and self.tabuleiro[2][0] == player

    def tabuleiroCheio(self):
        return self.tabuleiro[0][0] != " " and self.tabuleiro[0][1] != " " and self.tabuleiro[0][2] != " " and \
               self.tabuleiro[1][0] != " " and self.tabuleiro[1][1] != " " and self.tabuleiro[1][2] != " " and \
               self.tabuleiro[2][0] != " " and self.tabuleiro[2][1] != " " and self.tabuleiro[2][2] != " "
