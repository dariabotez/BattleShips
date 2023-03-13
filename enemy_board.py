class EnemyBoard:

    """Creates a grid to track the state of an opponent's board grid"""

    def __init__(self, width=10, height=10):
        self.enemy_board = [["." for i in range(width)] for i in range(height)]

    def getitem(self, point):
        row, col = point
        return self.enemy_board[row][col]

    def setitem(self, point, value):
        row, col = point
        self.enemy_board[row][col] = value

    def view_enemy_board(self):
        for row in self.enemy_board:
            print(" ".join(row))