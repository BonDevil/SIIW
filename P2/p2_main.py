from P2.game_utils import *


if __name__ == '__main__':

    mainBoard = readBoard()
    turn = 'player_one'
    while True:
        if turn == 'player_one':
            x, y = getComputerMove(mainBoard, PLAYER_ONE_TILE)
            mainBoard = makeMove(mainBoard, PLAYER_ONE_TILE, x, y)
            if not getValidMoves(mainBoard, PLAYER_TWO_TILE):
                break
            else:
                turn = 'player_two'

        else:
            x, y = getComputerMove(mainBoard, PLAYER_TWO_TILE)
            mainBoard = makeMove(mainBoard, PLAYER_TWO_TILE, x, y)
            if getValidMoves(mainBoard, PLAYER_ONE_TILE) == []:
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

