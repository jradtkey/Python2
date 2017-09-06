def checkerboard(board):
    for value in range(0, board):
        if value % 2 == 0:
            print("* " * spots)
        else:
            print(" *" * spots)

spots = 4

checkerboard(5)
