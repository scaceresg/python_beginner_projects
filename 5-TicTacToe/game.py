import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


# Create a Game class to define the elements of the game
class TicTacToe:
    def __init__(self):
        # First, we need to define the 3x3 board
        self.board = [' ' for _ in range(9)]
        # Then, we need to keep track of the winner
        self.current_winner = None

    # Print the board
    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # Print the board numbers using a static method
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    # Define the available moves on the board
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    # Get empty squares on the board - Returns a boolean
    def empty_squares(self):
        return ' ' in self.board

    # Get the number of empty squares
    def num_empty_squares(self):
        return self.board.count(' ')

    # Make a move: if valid, make the move (assign square to letter) then return True,
    # if invalid return False. Also, check for the winner
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # Determine a winner for the game: In TicTacToe - 3 in a row anywhere
    def winner(self, square, letter):
        # Check rows
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Check columns
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals: Diagonals are only possible for even numbers (0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # If all checks fail, return False
        return False


# Define a function outside the class to create a game and return a winner or None for a tie
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    # Iterate while the game still has empty squares or a winner is defined
    letter = 'X'
    while game.empty_squares():
        # Get a move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Make a valid move, print the board and alternate letters
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            # Alternate players
            letter = 'O' if letter == 'X' else 'X'

        # Create tiny break to make things easier to read
        if print_game:
            time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')


# First game
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

# Second game
# if __name__ == '__main__':
#     x_wins = 0
#     o_wins = 0
#     ties = 0
#     for _ in range(1000):
#         x_player = RandomComputerPlayer('X')
#         o_player = RandomComputerPlayer('O')
#         t = TicTacToe()
#         result = play(t, x_player, o_player, print_game=False)
#         if result == 'X':
#             x_wins += 1
#         elif result == 'O':
#             o_wins += 1
#         else:
#             ties += 1
#
#     print(f'After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins and {ties} ties')
