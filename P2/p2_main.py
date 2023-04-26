from P2.game_utils import *


#comp vs comp game
# if __name__ == '__main__':
#
#     mainBoard = readBoard()
#     turn = 'player_one'
#     while True:
#         if turn == 'player_one':
#             val, move = minimax(mainBoard, 5, True, PLAYER_ONE_TILE)
#             mainBoard = makeMove(mainBoard, PLAYER_ONE_TILE, move[0], move[1])
#             if getValidMoves(mainBoard, PLAYER_TWO_TILE) == []:
#                 break
#             else:
#                 turn = 'player_two'
#
#         else:
#             val, move = minimax(mainBoard, 1, True, PLAYER_TWO_TILE)
#             mainBoard = makeMove(mainBoard, PLAYER_TWO_TILE, move[0], move[1])
#             if getValidMoves(mainBoard, PLAYER_ONE_TILE) == []:
#                 break
#             else:
#                 turn = 'player_one'
#
#     drawBoard(mainBoard)
#     print(getScoreOfBoard(mainBoard))

#player vs computer game
if __name__ == '__main__':

    mainBoard = readBoard()
    drawBoard(mainBoard)
    turn = 'player_one'
    while True:
        if turn == 'player_one':
            move = getPlayerMove(mainBoard, PLAYER_ONE_TILE)
            mainBoard = makeMove(mainBoard, PLAYER_ONE_TILE, move[0], move[1])
            print("After player's move")
            drawBoard(mainBoard)
            if not getValidMoves(mainBoard, PLAYER_TWO_TILE):
                break
            else:
                turn = 'player_two'

        else:
            print("Press key to make computer's move")
            input()
            val, move = minimax(mainBoard, 1, True, PLAYER_TWO_TILE)
            mainBoard = makeMove(mainBoard, PLAYER_TWO_TILE, move[0], move[1])
            print("After computer's move")
            drawBoard(mainBoard)
            if not getValidMoves(mainBoard, PLAYER_ONE_TILE):
                break
            else:
                turn = 'player_one'

    drawBoard(mainBoard)
    print(getScoreOfBoard(mainBoard))



    """
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0
0 0 0 2 1 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
    """

