import copy
from colorama import Fore, Style


PLAYER_ONE_TILE = 1
PLAYER_TWO_TILE = 2


def draw_board(board):
    hline = '-----------------------------------------'

    print(hline)
    for y in range(8):
        for x in range(8):
            tile = board[x][y]
            if tile == PLAYER_ONE_TILE:
                print(f'|  {Fore.GREEN}{Style.BRIGHT}{tile}{Style.RESET_ALL}', end=' ')
            elif tile == PLAYER_TWO_TILE:
                print(f'|  {Fore.RED}{Style.BRIGHT}{tile}{Style.RESET_ALL}', end=' ')
            else:
                tile = str(x+1) + str(y+1)
                print(f'| {tile}', end=' ')
        print("|")
        print(hline)


def read_board():
    board = []
    for i in range(8):
        row = input().split()
        board.append([int(x) for x in row])
    return board


def get_player_move(board, player_tile):
    digits_1_to_8 = '1 2 3 4 5 6 7 8'.split()

    while True:
        print('Enter your move (two digits from 1-8)')
        move = input().lower()

        if len(move) == 2 and move[0] in digits_1_to_8 and move[1] in digits_1_to_8:
            x, y = int(move[0]) - 1, int(move[1]) - 1
            if is_valid_move(board, player_tile, x, y):
                break
            else:
                continue

        print('That is not a valid move.')

    return [x, y]


def is_valid_move(board, player_tile, x_start, y_start):
    # Check if the starting position is already occupied
    if board[x_start][y_start] != 0:
        return False

    # Define the opponent's tile
    if player_tile == PLAYER_ONE_TILE:
        opponent_tile = PLAYER_TWO_TILE
    else:
        opponent_tile = PLAYER_ONE_TILE

    # Check in all directions for valid moves
    flip_tiles = []
    for x_dir, y_dir in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
        x, y = x_start + x_dir, y_start + y_dir
        tiles_to_flip = []
        while 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == opponent_tile:
            tiles_to_flip.append((x, y))
            x += x_dir
            y += y_dir
        if tiles_to_flip and 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == player_tile:
            flip_tiles.extend(tiles_to_flip)

    # Return False if no tiles can be flipped
    if not flip_tiles:
        return False

    # Otherwise, return all tiles that would be flipped
    return flip_tiles


def get_valid_moves(board, tile):
    # Returns a list of [x,y] lists of valid moves for the given player on the given board.
    valid_moves = []

    for x in range(8):
        for y in range(8):
            if is_valid_move(board, tile, x, y):
                valid_moves.append([x, y])
    return valid_moves


def get_score_of_board(board):
    # Determine the score by counting the tiles. Returns a dictionary with keys 'X' and 'O'.
    x_score = 0
    o_score = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == PLAYER_ONE_TILE:
                x_score += 1
            if board[x][y] == PLAYER_TWO_TILE:
                o_score += 1
    return {PLAYER_ONE_TILE: x_score, PLAYER_TWO_TILE: o_score}


def make_move(board, tile, x_start, y_start):
    # Place the tile on the board at x_start, y_start, and flip any of the opponent's pieces.
    # Returns False if this is an invalid move, True if it is valid.
    tiles_to_flip = is_valid_move(board, tile, x_start, y_start)

    new_board = copy.deepcopy(board)
    if not tiles_to_flip:
        return new_board

    new_board[x_start][y_start] = tile
    for x, y in tiles_to_flip:
        new_board[x][y] = tile
    return new_board


def is_on_corner(x, y):
    # Returns True if the position is in one of the four corners.
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def is_game_over(board):
    # Check if the board is full
    for row in board:
        if 0 in row:
            return False
    return True


def show_points(player_tile, computer_tile, board):
    # Prints out the current score.
    scores = get_score_of_board(board)
    print('You have %s points. The computer has %s points.' % (scores[player_tile], scores[computer_tile]))



# def getComputerMove(board, computerTile):
#     # Given a board and the computer's tile, determine where to
#     # move and return that move as a [x, y] list.
#     possibleMoves = getValidMoves(board, computerTile)
#
#     # randomize the order of the possible moves
#     random.shuffle(possibleMoves)
#
#     # always go for a corner if available.
#     for x, y in possibleMoves:
#         if isOnCorner(x, y):
#             return [x, y]
#
#     # Go through all the possible moves and remember the best scoring move
#     bestScore = -1
#     bestMove = possibleMoves[0]
#     for x, y in possibleMoves:
#         dupeBoard = copy.deepcopy(board)
#         makeMove(dupeBoard, computerTile, x, y)
#         score = getScoreOfBoard(dupeBoard)[computerTile]
#         if score > bestScore:
#             bestMove = [x, y]
#             bestScore = score
#     return bestMove