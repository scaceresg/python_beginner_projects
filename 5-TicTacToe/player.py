# 5-1 Create a Player class to define the X/O players: It can be a computer or a human
import math
import random


# Create the class player defining their letter: X or O
class Player:
    def __init__(self, letter):
        self.letter = letter

    # Get each player's next move
    def get_move(self, game):
        pass


# Create a random computer player using inheritance
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # Get a random available spot
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


# Create a human player using inheritance
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # Get a valid move from the player
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # Use try-except to check the human's input
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


# Create a Genius Computer Player based on the minimax algorithm
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # If all moves are available, choose randomly, else get the square based off the minimax algorithm
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    # Define the minimax algorithm which receives a screenshot of the game (state)
    def minimax(self, state, player):
        # Define the players
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # Check if the previous move is a winner and return position and score
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player
                    else -1 * (state.num_empty_squares() + 1)}
        # No empty squares
        elif not state.empty_squares():
            return {'position': None,
                    'score': 0}

        # Each score should be maximized (score = -infinite) when player is max_player
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        # Iterate each possible move to obtain the minimax
        for possible_move in state.available_moves():
            # Step 1. Make a move and try that spot
            state.make_move(possible_move, player)

            # Step 2. Recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)

            # Step 3. Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # Step 4. Update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
