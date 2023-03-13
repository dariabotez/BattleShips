from board import Board
from enemy_board import EnemyBoard
from ship import Ship


class Player:

    ships = {"Aircraft Carrier": 5, "Crusier": 4, "Destroyer": 3, "Submarine": 2}

    def __init__(self, name):
        self.board = Board()
        self.enemy_board = EnemyBoard()
        self.name = name
        self.fleet = []

   # Function uses player input to set up fleet positions on a player board.
   # For each ship, a ship object containing relevant coordinates is appended to self.fleet

    def set_fleet(self):
        input("Boats are placed from left to right horizontally.")
        input("Boats are placed from the upper side to lower side vertically.")
        for ship, size in self.ships.items():

            flag = True
            while flag:
                self.view_console()
                try:
                    print("Place your %s" % (ship))
                    row = int(input("Pick a row -----> "))
                    col = int(input("Pick a column -----> "))
                    orientation = str(input("Vertical or Horizontal? (choose v or h) -----> "))

                    if orientation in ["v", "V"]:
                        if self.board.can_use_row(row, col, size):
                            self.board.set_ship_row(row, col, size)
                            boat = Ship(ship, size)
                            boat.plot_vertical(row, col)
                            self.fleet.append(boat)
                            flag = False
                        else:
                            input("Overlapping ships, try again")

                    elif orientation in ["h", "H"]:
                        if self.board.can_use_col(row, col, size):
                            self.board.set_ship_col(row, col, size)
                            boat = Ship(ship, size)
                            boat.plot_horizontal(row, col)
                            self.fleet.append(boat)
                            flag = False
                        else:
                            input("Invalid position, try again")

                    else:
                        continue

                    self.view_console()

                except ValueError:
                    print("Don't you remember your training?\nType a number..\n")

    # Function displays player board in readable format

    def view_console(self):
        print("Enemy's Board")
        self.enemy_board.view_enemy_board()
        print("-------------------")
        print("Your Board")
        self.board.view_board()

    # Function checks status of ship objects within player fleet

    def register_hit(self, row, col):
        for boat in self.fleet:
            if (row, col) in boat.coords:
                boat.coords.remove((row, col))
                if boat.check_status():
                    self.fleet.remove(boat)
                    print("%s's %s has been sunk!" % (self.name, boat.ship_type))

    # Player interface for initiating in-game strikes,
    # updates the state of the boards of both players

    def strike(self, target):
        self.view_console()
        try:
            print("\n%s Pick your target..." % self.name)
            row = int(input("Pick a row -----> a column ----- "))
            col = int(input("Pick> "))

            if self.board.valid_row(row) and self.board.valid_col(col):
                if target.board.getitem((row, col)) == "S":
                    print("DIRECT HIT!!!")
                    target.board.setitem((row, col), "X")
                    target.register_hit(row, col)
                    self.enemy_board.setitem((row, col), "X")

                else:
                    if self.enemy_board.getitem((row, col)) == "0":
                        print("Area already hit....Check your enemy board!")
                        self.strike(target)
                    else:
                        print("Negative...")
                        self.enemy_board.setitem((row, col), "0")

            else:
                print("Coordinates out of range...")
                self.strike(target)

        except ValueError:
            print("You need to provide a number....\n")
            self.strike(target)
        input()