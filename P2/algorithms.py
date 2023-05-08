from P2.game_utils import *


# gives a bonus to the player who controls the corners of the board.
# This is because the corners are the most stable positions and cannot be flipped by the opponent.
def heuristic_corners(board, player_tile):
    corners = 0
    opponent_tile = PLAYER_TWO_TILE if player_tile == PLAYER_ONE_TILE else PLAYER_ONE_TILE
    for x in [0, 7]:
        for y in [0, 7]:
            if board[x][y] == player_tile:
                corners += 1
            elif board[x][y] == opponent_tile:
                corners -= 1
    return 25 * corners


# evaluates the number of valid moves available to each player.
# A higher number indicates that the player has more options available and
# is therefore more likely to make a strong move
def heuristic_mobility(board, player_tile):
    player_moves = len(get_valid_moves(board, player_tile))
    opponent_moves = len(get_valid_moves(board, PLAYER_TWO_TILE if player_tile == PLAYER_ONE_TILE else PLAYER_ONE_TILE))
    if player_moves + opponent_moves == 0:
        return 0
    return 100 * (player_moves - opponent_moves) / (player_moves + opponent_moves)


# calculates the difference in the number of tiles owned by each player.
# A higher number indicates that the player has more tiles on the board and thus more control over the game.
def heuristic_coin_parity(board, player_tile):
    scores = get_score_of_board(board)
    return scores[player_tile] - scores[PLAYER_TWO_TILE if player_tile == PLAYER_ONE_TILE else PLAYER_ONE_TILE]


def heuristic_default(board, player_tile):
    return 0


# def minimax(board, depth, maximizing_player, player_tile, heuristic=heuristic_default, print_tree=False, indent=0):
#     if depth == 0 or is_game_over(board):
#         score = get_score_of_board(board)[player_tile] + heuristic(board, player_tile)
#         if print_tree:
#             print(f"{' ' * indent}Score: {score}")
#         return score, None
#
#     if maximizing_player and len(get_valid_moves(board, player_tile)) > 0:
#         max_eval = float('-inf')
#         best_move = None
#         for move in get_valid_moves(board, player_tile):
#             new_board = make_move(board, player_tile, move[0], move[1])
#             if print_tree:
#                 print(f"{' ' * indent}Player {player_tile} ({move[0]}, {move[1]})")
#             eval, _ = minimax(new_board, depth - 1, False, 3 - player_tile, heuristic, print_tree, indent + 2)
#
#             if eval > max_eval:
#                 max_eval = eval
#                 best_move = move
#         if print_tree:
#             print(f"{' ' * indent}Max Eval: {max_eval}")
#         return max_eval, best_move
#     else:
#         min_eval = float('inf')
#         best_move = None
#         for move in get_valid_moves(board, player_tile):
#             new_board = make_move(board, player_tile, move[0], move[1])
#             if print_tree:
#                 print(f"{' ' * indent}Player {player_tile} ({move[0]}, {move[1]})")
#             eval, _ = minimax(new_board, depth - 1, True, 3 - player_tile, heuristic, print_tree, indent + 2)
#             if eval < min_eval:
#                 min_eval = eval
#                 best_move = move
#         if print_tree:
#             print(f"{' ' * indent}Min Eval: {min_eval}")
#         return min_eval, best_move


def minimax_ab(board, depth, alpha, beta, maximizing_player, player_tile, heuristic=heuristic_default):
    if depth == 0 or is_game_over(board):
        return get_score_of_board(board)[player_tile] + heuristic(board, player_tile), None

    if maximizing_player and len(get_valid_moves(board, player_tile)) > 0:
        max_eval = float('-inf')
        best_move = None
        for move in get_valid_moves(board, player_tile):
            new_board = make_move(board, player_tile, move[0], move[1])
            eval, _ = minimax_ab(new_board, depth - 1, alpha, beta, False, 3 - player_tile)

            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_valid_moves(board, player_tile):
            new_board = make_move(board, player_tile, move[0], move[1])
            eval, _ = minimax_ab(new_board, depth - 1, alpha, beta, True, 3 - player_tile)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move
