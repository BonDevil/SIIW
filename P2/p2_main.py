from P2.algorithms import *
from P2.game_utils import *



# comp vs comp game
if __name__ == '__main__':


    main_board = read_board()
    val, move = minimax(main_board, depth=5, maximizing_player=True, player_tile=PLAYER_ONE_TILE,
                                        print_tree=True)
    main_board = make_move(main_board, PLAYER_ONE_TILE, move[0], move[1])
    draw_board(main_board)
    # turn = 'player_one'
    # while True:
    #     if turn == 'player_one':
    #         val, move = minimax_ab(main_board, depth=5, maximizing_player=True, player_tile=PLAYER_ONE_TILE,
    #                                             alpha=float('-inf'), beta=float('inf'))
    #         main_board = make_move(main_board, PLAYER_ONE_TILE, move[0], move[1])
    #         draw_board(main_board)
    #         if not get_valid_moves(main_board, PLAYER_TWO_TILE):
    #             break
    #         else:
    #             turn = 'player_two'
    #
    #     else:
    #         val, move = minimax_ab(main_board, depth=1, maximizing_player=True, player_tile=PLAYER_TWO_TILE,
    #                                             alpha=float('-inf'), beta=float('inf'))
    #         main_board = make_move(main_board, PLAYER_TWO_TILE, move[0], move[1])
    #         draw_board(main_board)
    #         if not get_valid_moves(main_board, PLAYER_ONE_TILE):
    #             break
    #         else:
    #             turn = 'player_one'
    #
    # draw_board(main_board)
    # print(get_score_of_board(main_board))


# player vs computer game
# if __name__ == '__main__':
#
#     main_board = read_board()
#     draw_board(main_board)
#     turn = 'player_one'
#     while True:
#         if turn == 'player_one':
#             move = get_player_move(main_board, PLAYER_ONE_TILE)
#             main_board = make_move(main_board, PLAYER_ONE_TILE, move[0], move[1])
#             print("After player's move")
#             draw_board(main_board)
#             if not get_valid_moves(main_board, PLAYER_TWO_TILE):
#                 break
#             else:
#                 turn = 'player_two'
#
#         else:
#             print("Press key to make computer's move")
#             input()
#
#             # minimax with corner heuristic - without ab pruning
#             # val, move = minimax(main_board, depth=6, maximizing_player=True, player_tile=PLAYER_TWO_TILE, print_tree=True)
#
#             # minimax with corner heuristic - with ab pruning
#             val, move = minimax_ab(main_board, depth=6, maximizing_player=True, player_tile=PLAYER_TWO_TILE,
#                                    alpha=float('-inf'), beta=float('inf'))
#
#             # make move and draw board
#             main_board = make_move(main_board, PLAYER_TWO_TILE, move[0], move[1])
#             print("After computer's move")
#             draw_board(main_board)
#             if not get_valid_moves(main_board, PLAYER_ONE_TILE):
#                 break
#             else:
#                 turn = 'player_one'
#
#     draw_board(main_board)
#     print(get_score_of_board(main_board))


    """
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0
0 0 0 2 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

1 1 2 2 2 0 0 0
2 1 1 2 1 1 1 0
2 2 2 1 1 1 0 0
2 2 1 1 1 1 0 0
2 2 2 1 1 0 0 0
2 2 1 1 0 0 0 0
2 2 2 1 2 0 0 0
2 2 2 2 0 0 0 0

    """


