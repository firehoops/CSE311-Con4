from tkinter import *
import tkinter.font
import tkinter.messagebox


#Text-Based and GUI
class View:

    def __init__(self,master):

        con = Controller()
        #print(con.setBoard())

        option = input("Type text or gui for your version of Connect Four")

        if option == "gui" or option == "GUI" or option == "Gui":
            self.gui(master)
        else:
            self.textView()

    def gui(self,master):
        header = tkinter.font.Font(size=20, weight=tkinter.font.BOLD)
        Label(master, text="Connect Four", anchor=N, font=header).grid(row=0, column=2, columnspan=2)

        # Tracking player
        player1 = True
        run = True

        # Main Canvas that board will be created and played on
        c = Canvas(master, width=700, height=600, bg="gray")

        # Create Seperation from Board to have buttons and exit/switch view buttons
        bottomFrame = Frame(master, width=700, height=200)
        bottomFrame.grid(row=8, columnspan=7)
        c.grid(row=1, column=0, rowspan=6, columnspan=7)

        colTracker = [*range(7)]
        print(colTracker)
        if player1:
            Button(bottomFrame, text="Add Piece to Row 1", command=lambda: self.addPiece(c, player1, colTracker[0])).grid(
                row=9, column=0, sticky=E)
            Button(bottomFrame, text="Add Piece to Row 2", command=lambda: self.addPiece(c, player1, colTracker[1])).grid(
                row=9, column=1, sticky=E)
            Button(bottomFrame, text="Exit", command=lambda: self.quit(master)).grid(row=9, column=2, sticky=E)
            Button(bottomFrame, text="Switch Views", command=lambda: self.switchView(master)).grid(row=9, column=3, sticky=E)

    def addPiece(self,canvas, player1, col):
        #Starting coord for row 1 , x0 =5 , y0 = 500 , x1 = 105 , y1= 600
        coords_col_1 = [5,500,105,600]
        coords_col_2 = [110, 500, 205, 600]


        if col == 0:
            if player1:
                canvas.create_oval(coords_col_1[0], coords_col_1[1], coords_col_1[2], coords_col_1[3], fill="black")
                coords_col_1[0] += 100
                coords_col_1[1] += 100
                coords_col_1[2] += 100
                coords_col_1[3] += 100


            else:
                canvas.create_oval(coords_col_1[0], coords_col_1[1], coords_col_1[2], coords_col_1[3], fill="red")
        if col == 1:
            if player1:
                canvas.create_oval(coords_col_2[0], coords_col_2[1], coords_col_2[2], coords_col_2[3], fill="black")
            else:
                canvas.create_oval(coords_col_2[0], coords_col_2[1], coords_col_2[2], coords_col_2[3], fill="red")

    def switchView(self,master):
        master.destroy()
        self.textView()

    def quit(self,master):
        master.quit()

    def textView(self):
        #Build Board
        ROW_COUNT = 6
        COL_COUNT = 7
        board = [[0] * COL_COUNT for r in range(ROW_COUNT)]
        run = True
        playerValue = 1
        printBoard = ""
        colChoice = 0

        #Initialize board
        #Params: board, row count, col count, user col choice, and
        #Return: Returns nothing prints out the gameboard
        def createBoard(board,ROW_COUNT, COL_COUNT, colChoice, printBoard):
            boardRotate = board[::-1]
            for r in range(ROW_COUNT):
                for c in range(COL_COUNT):
                    printBoard += "|" + str(boardRotate[r][c])
                printBoard += "|\n"
            print(printBoard)
        #Checking if row is free
        #Params: Board, col choice, and amount of rows
        def checkRow(board,colChoice,ROW_COUNT):
            for rowNum in range(ROW_COUNT):
                if board[rowNum][colChoice] == 0:
                    return rowNum


        while(run):
            createBoard(board,ROW_COUNT,COL_COUNT, colChoice,printBoard)
            colChoice = int(input("Select a Column 0,1,2,3,4,5,6, or select 8 to quit or 9 to switch to the GUI "))

            if colChoice == 8:
                break
            # if colChoice == 9:
            #     self.gui(master)

            if playerValue == 1:
                row = checkRow(board,colChoice,ROW_COUNT)
                board[row][colChoice] = playerValue
                createBoard(board,ROW_COUNT, COL_COUNT, colChoice,printBoard)
                playerValue += 1
            else:
                row = checkRow(board, colChoice, ROW_COUNT)
                board[row][colChoice] = playerValue
                createBoard(board, ROW_COUNT, COL_COUNT, colChoice,printBoard)
                playerValue -= 1


            print(board)



#Handle Connecting view and model
class Controller:

    def __init__(self):
        pass

    def getBoard(self):
        return self.board
    def setBoard(self):
        self.board = [[0] * 7 for r in range(6)]
        return self.board

#Handle Logic
class Model:

    def __init__(self):
        pass

#Starts Tkinter window and runs in loop until user exits
root = Tk()
start = View(root)
root.mainloop()