def sum(a, b, c):
    return a+b+c

def printBoard(xState, zState):
    zero="x" if xState[0] else ("o" if zState[0] else 0)
    one="x" if xState[1] else ("o" if zState[1] else 1)
    two="x" if xState[2] else ("o" if zState[2] else 2)
    three="x" if xState[3] else ("o" if zState[3] else 3)
    four="x" if xState[4] else ("o" if zState[4] else 4)
    five="x" if xState[5] else ("o" if zState[5] else 5)
    six="x" if xState[6] else ("o" if zState[6] else 6)
    seven="x" if xState[7] else ("o" if zState[7] else 7)
    eight="x" if xState[8] else ("o" if zState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print("---------")
    print(f"{three} | {four} | {five}")
    print("---------")
    print(f"{six} | {seven} | {eight}")


def Checkwin(xState, zState):
    xwins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in xwins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X won the game")
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O won the game")
            return 0
    return -1
    
if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Tic Tac Toe")
    while True:
         printBoard(xState, zState)
         
         if(turn==1):
            print("X's turn")
            value=int(input(" Enter a value to continue...: "))
            xState[value]=1
           
         else:
            print("O's turn")
            value=int(input(" Enter a value to continue...: "))
            zState[value]=1
            cwin=Checkwin(xState, zState)
            if cwin!=-1:
                print("Game Over")
                break
         turn=1-turn
        