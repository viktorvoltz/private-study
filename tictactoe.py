class TicTacToe:

    def __init__(self):

        self._board = [[' '] * 3 for j in range(3)]
        self._player = 'x'

    def mark(self, i, j):

        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        if self.winner() is not None:
            #raise ValueError('Game already complete')
            print(self.winner())
        self._board[i][j] = self._player
        if self._player == 'x':
            self._player = 'o'
        else:
            self._player = 'x'


    def _is_win(self, mark):

        board = self._board
        #check if we have a winner
        return (mark == board[0][0] == board[0][1] == board[0][2] or # row 0
                mark == board[1][0] == board[1][1] == board[1][2] or # row 1
                mark == board[2][0] == board[2][1] == board[2][2] or # row 2
                mark == board[0][0] == board[1][0] == board[2][0] or # column 0
                mark == board[0][1] == board[1][1] == board[2][1] or # column 1
                mark == board[0][2] == board[1][2] == board[2][2] or # column 2
                mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
                mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self):

        for mark in 'xo':
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):

        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)


game = TicTacToe()

game.mark(1, 1); game.mark(0, 2)
game.mark(2, 2); game.mark(0, 1)
game.mark(0, 0); game.mark(2, 1)
game.mark(1, 2); game.mark(1, 0)
game.mark(2, 0)


print(game)
winner = game.winner()
if winner is None:
    print('Tie')
else:
    print(winner, "wins")
