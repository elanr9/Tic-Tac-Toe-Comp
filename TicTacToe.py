import os

board = [' ' for x in range(10)]


def clear():
    os.system('clear')


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[3] == le and bo[6] == le and bo[9] == le) or \
           (bo[1] == le and bo[5] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    print("You are playing with 'X'.")
    while run == True:
        move = input("Type a number based on the Board numbers above to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print("Sorry, this space is occupied.")

            else:
                print("Please type a number within the range.")
        except:
            print("Please type a number!")


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for let in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move


def selectRandom(lst):
    import random
    ln = len(lst)
    r = random.randrange(0, ln)
    return lst[r]


def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    return True


"""print("Board numbers:")
print("   |   |")
print(" 1 | 2 | 3")
print("   |   |")
print("-----------")
print("   |   |")
print(" 4 | 5 | 6")
print("   |   |")
print("-----------")
print("   |   |")
print(" 7 | 8 | 9")
print("   |   |")
"""
wins = 0
losses = 0
ties = 0
nums = 0
def main():
    global wins, losses, ties, nums
    print("""Board numbers:
   |   |
 1 | 2 | 3
   |   |
-----------
   |   |
 4 | 5 | 6
   |   |
-----------
   |   |
 7 | 8 | 9
   |   |
    """)
    print("")
    print("")
    print("")
    print("")
    print("Welcome to Elan's Tic Tac Toe!")
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, "O")):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, the computer won this time!")
            losses += 1
            break

        if not (isWinner(board, "X")):
            move = compMove()
            if move == 0:
                print("Tie Game!")
                ties += 1
            else:
                insertLetter("O", move)
                print('Computer placed an "O" in position', move, ':')
                printBoard(board)
        else:
            print("YOU WON! GOOD JOB!")
            wins += 1
            break

    answer = input("PLAY AGAIN? (Y/N): ").lower()  # ASKS USER IF THEY WANT TO PLAY AGAIN
    while True:
        if answer == "y":
            nums = 0
            break
        elif answer == "n":
            clear()
            print("WINS:", wins , "LOSSES:", losses, "TIES:", ties)
            print("THANKS FOR PLAYING!")  # IF 'N' IS TYPED: GAME WILL END AND TELL USER HOW MANY WINS TIES AND LOSSES
            nums = 1
            break
        else:
            print("Please type 'y' or 'n'")  # IF USER DOESNT TYPE 'Y' or 'N': ITLL ASK USER TO ANSWER AGAIN
            answer = input("PLAY AGAIN? (Y/N): ").lower()
            
    if nums == 0:
        clear()
        for i in range(10):
            board[i] = " "
        main()
main()
