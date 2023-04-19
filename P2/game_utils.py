# Reversi
import copy
import random
import sys

PLAYER_ONE_TILE = 1
PLAYER_TWO_TILE = 2


def drawBoard(board):
    # This function prints out the board that it was passed. Returns None.
    HLINE = '-------------------------------------------------'

    print(HLINE)
    for y in range(8):
        for x in range(8):
            print('|  %s ' % (board[x][y]), end=' ')
        print("|")
        print(HLINE)


def readBoard():
    board = []
    for i in range(8):
        row = input().split()
        board.append([int(x) for x in row])
    return board


def isValidMove(board, player_tile, x_start, y_start):
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


def getValidMoves(board, tile):
    # Returns a list of [x,y] lists of valid moves for the given player on the given board.
    validMoves = []

    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y):
                validMoves.append([x, y])
    return validMoves


def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Returns a dictionary with keys 'X' and 'O'.
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == PLAYER_ONE_TILE:
                xscore += 1
            if board[x][y] == PLAYER_TWO_TILE:
                oscore += 1
    return {PLAYER_ONE_TILE: xscore, PLAYER_TWO_TILE: oscore}


def makeMove(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart, and flip any of the opponent's pieces.
    # Returns False if this is an invalid move, True if it is valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    new_board = copy.deepcopy(board)
    if not tilesToFlip:
        return new_board

    new_board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        new_board[x][y] = tile
    return new_board


def isOnCorner(x, y):
    # Returns True if the position is in one of the four corners.
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def getComputerMove(board, computerTile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as a [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)

    # randomize the order of the possible moves
    random.shuffle(possibleMoves)

    # always go for a corner if available.
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # Go through all the possible moves and remember the best scoring move
    bestScore = -1
    bestMove = possibleMoves[0]
    for x, y in possibleMoves:
        dupeBoard = copy.deepcopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove


def minimax(board, depth, maximizing_player, player_tile):
    if depth == 0 or is_game_over(board):
        return getScoreOfBoard(board)[player_tile], None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in getValidMoves(board, player_tile):
            new_board = makeMove(board, player_tile, move[0], move[1])
            eval, _ = minimax(new_board, depth - 1, False, 3 - player_tile)

            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in getValidMoves(board, player_tile):
            new_board = makeMove(board, player_tile, move[0], move[1])
            eval, _ = minimax(new_board, depth - 1, True, 3 - player_tile)
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move



def is_game_over(board):
    # Check if the board is full
    for row in board:
        if 0 in row:
            return False
    return True

def showPoints(playerTile, computerTile, board):
    # Prints out the current score.
    scores = getScoreOfBoard(board)
    print('You have %s points. The computer has %s points.' % (scores[playerTile], scores[computerTile]))
