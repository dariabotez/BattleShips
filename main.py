from multiplayer import MultiPlayer

# Script initiates game of battleships


def main():
    print("\n\n***********************")
    print("Welcome to Battleships!")
    print("***********************\n")

    print("\n 1) Play")
    print("\n 0) Exit")

    flag = True

    while flag:
        try:
            mode = int(input("\n\nPick a number to select a game mode ----> "))
            if mode == 1:
                flag = False
                MultiPlayer()
            elif mode == 0:
                flag = False

            else:
                print("Please enter a valid option")
                continue
        except ValueError:
            print("You can only pick either option 1 or 0")

main()