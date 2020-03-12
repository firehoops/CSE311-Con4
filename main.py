from tkinter import *
import tkinter.font
import tkinter.messagebox
import time
import os

#Text-Based and GUI
class View:
    def __init__(self):
        self.ROW_COUNT = 6
        self.COL_COUNT = 7
    #Use this to get user text input
    def getUserInput(self, message):
        userInput = input(message)
        return userInput

    #Params: board, row count, col count, user col choice, and
    #Return: Returns nothing prints out the gameboard
    def displayBoard(self,board):
        printBoard = ""

        boardRotate = board[::-1]
        for r in range(self.ROW_COUNT):
            for c in range(self.COL_COUNT):
                printBoard += "|" + str(boardRotate[r][c])
            printBoard += "|\n"
        print(printBoard)

#Handle Logic
#This is where the board is created and stored during runtime.
class Model:

    def __init__(self):

        self.playerValue = 1
        self.ROW_COUNT = 6
        self.COL_COUNT = 7
        self.board = [[0] * self.COL_COUNT for r in range(self.ROW_COUNT)]
        self.moveCount = 0

    #Returns the board
    def getBoard(self):
        return self.board

    def winnerExists(self):

        # Check Horizontal
        for row in range(self.ROW_COUNT):
            for col in range(self.COL_COUNT - 3):
                if self.board[row][col] == self.playerValue \
                        and self.board[row][col + 1] == self.playerValue \
                        and self.board[row][col + 2] == self.playerValue \
                        and self.board[row][col + 3] == self.playerValue:
                    return True

        # Check Vertical
        for row in range(self.ROW_COUNT - 3):
            for col in range(self.COL_COUNT):
                if self.board[row][col] == self.playerValue \
                        and self.board[row + 1][col] == self.playerValue \
                        and self.board[row + 2][col] == self.playerValue \
                        and self.board[row + 3][col] == self.playerValue:
                    return True

        # Check Diagonal \
        for row in range(self.ROW_COUNT - 3):
            for col in range(self.COL_COUNT - 3):
                if self.board[row][col] == self.playerValue \
                        and self.board[row + 1][col + 1] == self.playerValue \
                        and self.board[row + 2][col + 2] == self.playerValue \
                        and self.board[row + 3][col + 3] == self.playerValue:
                    return True

        # Check Diagonal /
        for row in range(3, self.ROW_COUNT):
            for col in range(self.COL_COUNT - 3):
                if self.board[row][col] == self.playerValue \
                        and self.board[row - 1][col + 1] == self.playerValue \
                        and self.board[row - 2][col + 2] == self.playerValue \
                        and self.board[row - 3][col + 3] == self.playerValue:
                    return True


    #Checking if row is free
    #Params: Board, col choice, and amount of rows
    #Returns: Returns the row number if valid
    def checkRow(self, board ,colChoice, ROW_COUNT):
        for rowNum in range(ROW_COUNT):
            if board[rowNum][colChoice] == 0:
                return rowNum

    def makeMove(self, colChoice):

        #Makes sure the column is valid
        try:
            row = model.checkRow(model.getBoard(), colChoice, self.ROW_COUNT)
            model.getBoard()[row][colChoice] = self.playerValue
            self.moveCount += 1
            #********need a  check that they can't go out of range*****
            if self.moveCount == 43:
                print("No Winner")

            if model.winnerExists():
                #start.c.grid_forget()
                #start.bottomFrame.grid_forget()
                header = tkinter.font.Font(size=40, weight=tkinter.font.BOLD)
                if self.playerValue == 1:
                    time.sleep(.75)
                    lab = Label(root, text = "Player 1 is the Winner!!",font = header).grid(row = 2, column = 2, rowspan = 4, columnspan = 4)
                    print("Player 1 is the Winner!!")
                    return False
                else:
                    time.sleep(.75)
                    lab = Label(root, text="Player 2 is the Winner!!", font=header).grid(row=2, column=2, rowspan=4, columnspan=4)
                    print("Player 2 is the Winner!!")
                    return False

            if self.playerValue == 1:
                self.playerValue += 1
            else:
                self.playerValue -= 1
            return True
        except:
            print("Please Enter A Valid Column \n")
            time.sleep(.5)
            return True



# Initialize View and Model
model = Model()
view = View()

class Controller:
    #Main method
    def __init__(self, master):
        self.coords_col_1 = [0, 500, 100, 600]
        self.coords_col_2 = [100, 500, 200, 600]
        self.coords_col_3 = [200, 500, 300, 600]
        self.coords_col_4 = [300, 500, 400, 600]
        self.coords_col_5 = [400, 500, 500, 600]
        self.coords_col_6 = [500, 500, 600, 600]
        self.coords_col_7 = [600, 500, 700, 600]
        self.c = Canvas(master, width=700, height=600, bg="lightsky blue")
        self.buttonFrame = Frame(master, width=700, height=200)
        self.playerScoreFrame = Frame(master, width=700, height=50)
        self.bottomFrame = Frame(master, width=700, height=50)
        # Starting the game
        option = view.getUserInput("Type text or gui for your version of Connect Four\n")
        if option.lower() == "gui":
            self.gui(master)
        if option == "txt":
            self.textView(master)
        # else:
        #     self.textView(master)
    # Creates the gui
    # Params: master is the main root
    # Returns: Creates a gui
    def gui(self, master):

        header = tkinter.font.Font(size=20, weight=tkinter.font.BOLD)
        Label(master, text="Connect Four", anchor=N, font=header).grid(row=0, column=2, columnspan=3)

        # Create Seperation from Board to have buttons and exit/switch view buttons
        self.c.grid(row=1, column=0, rowspan=6, columnspan=7)
        self.buttonFrame.grid(row=8, column=0, columnspan=7)
        self.playerScoreFrame.grid(row=9, column=0, columnspan=7)
        self.bottomFrame.grid(row=10, column=0, columnspan=7)
        colTracker = [*range(7)]

        Button(self.buttonFrame, text="Row 1", relief = "groove", width= 12,command=lambda: \
            self.addPiece(colTracker[0],master)).grid(row=8, column=0, padx = 3)
        Button(self.buttonFrame, text="Row 2", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[1],master)).grid(row=8, column=1, padx =3)
        Button(self.buttonFrame, text="Row 3", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[2],master)).grid(row=8, column=2, padx =3)
        Button(self.buttonFrame, text="Row 4", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[3],master)).grid(row=8, column=3, padx =3)
        Button(self.buttonFrame, text="Row 5", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[4],master)).grid(row=8, column=4, padx =3)
        Button(self.buttonFrame, text="Row 6", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[5],master)).grid(row=8, column=5, padx =3)
        Button(self.buttonFrame, text="Row 7", relief = "groove",width= 12,command=lambda: \
            self.addPiece(colTracker[6],master)).grid(row=8, column=6, padx =3)


        Button(self.bottomFrame, text="Exit", relief = "groove",width=15,command=lambda: self.quit(master)).grid(row=10, column=2, pady = 30, padx = 15)
        Button(self.bottomFrame, text="Switch Views", relief = "groove",width= 15,command=lambda: self.switchToText(master)).grid(row=10,column=4)


    def textView(self,master):
        run = True
        #Game Loop
        while run:

            #User Input Loop
            while True:

                #Try/Except to make sure user gives valid input
                #try:
                    view.displayBoard(model.getBoard())

                    colChoice = int(
                        view.getUserInput("Which Column 0,1,2,3,4,5, or 6 (or type 9 to go into gui view) \n"))
                    if colChoice == 8 or colChoice == 7:
                        break #Continues game
                    if colChoice == 9:
                        #Supposed to bring window back up
                        self.createNewWindow(master)
                        # root.iconify()
                        # root.update()
                        # root.deiconify()
                        break
                    run = model.makeMove(colChoice)

                    break #Exits the User Input Loop
                #except:
                    #print("Please Enter A Valid Column \n")
                    #time.sleep(.5)
        exit()
    def createNewWindow(self,master):
        master.destroy()
        dup = Tk()
        header = tkinter.font.Font(size=20, weight=tkinter.font.BOLD)
        Label(dup, text="Connect Four", anchor=N, font=header).grid(row=0, column=2, columnspan=3)
        dup.mainloop()

    #Adds a piece to the board
    #Params:Canvas, Boolean player value, col which was selected
    #Returns: Creates a piece on the board
    def addPiece(self, col,master):
        #Starting coord for row 1 , x0 =5 , y0 = 500 , x1 = 105 , y1= 600
        playerValueFont = tkinter.font.Font(size=15, weight=tkinter.font.BOLD)

        if col == 0:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_1[0], self.coords_col_1[1], self.coords_col_1[2], self.coords_col_1[3], fill="black")
                Label(master, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_1[1] -= 100
                self.coords_col_1[3] -= 100
                model.makeMove(col)

            else:
                self.c.create_oval(self.coords_col_1[0], self.coords_col_1[1], self.coords_col_1[2], self.coords_col_1[3], fill="red")
                Label(master, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_1[1] -= 100
                self.coords_col_1[3] -= 100
                model.makeMove(col)
        if col == 1:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_2[0], self.coords_col_2[1], self.coords_col_2[2], self.coords_col_2[3], fill="black")
                Label(master, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_2[1] -= 100
                self.coords_col_2[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_2[0], self.coords_col_2[1], self.coords_col_2[2], self.coords_col_2[3], fill="red")
                Label(master, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)

                self.coords_col_2[1] -= 100
                self.coords_col_2[3] -= 100
                model.makeMove(col)
        if col == 2:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_3[0], self.coords_col_3[1], self.coords_col_3[2], self.coords_col_3[3], fill="black")
                Label(master, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_3[1] -= 100
                self.coords_col_3[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_3[0], self.coords_col_3[1], self.coords_col_3[2], self.coords_col_3[3], fill="red")
                Label(master, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_3[1] -= 100
                self.coords_col_3[3] -= 100
                model.makeMove(col)
        if col == 3:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_4[0], self.coords_col_4[1], self.coords_col_4[2], self.coords_col_4[3], fill="black")
                Label(master, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_4[1] -= 100
                self.coords_col_4[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_4[0], self.coords_col_4[1], self.coords_col_4[2], self.coords_col_4[3], fill="red")
                Label(master, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_4[1] -= 100
                self.coords_col_4[3] -= 100
                model.makeMove(col)

        if col == 4:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_5[0], self.coords_col_5[1], self.coords_col_5[2], self.coords_col_5[3], fill="black")
                Label(master, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_5[1] -= 100
                self.coords_col_5[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_5[0], self.coords_col_5[1], self.coords_col_5[2], self.coords_col_5[3], fill="red")
                Label(master, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_5[1] -= 100
                self.coords_col_5[3] -= 100
                model.makeMove(col)
        if col == 5:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_6[0], self.coords_col_6[1], self.coords_col_6[2],self.coords_col_6[3], fill="black")
                Label(master, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_6[1] -= 100
                self.coords_col_6[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_6[0], self.coords_col_6[1], self.coords_col_6[2],self.coords_col_6[3], fill="red")
                Label(master, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_6[1] -= 100
                self.coords_col_6[3] -= 100
                model.makeMove(col)
        if col == 6:
            if model.playerValue == 1:
                self.c.create_oval(self.coords_col_7[0], self.coords_col_7[1], self.coords_col_7[2], self.coords_col_7[3], fill="black")
                Label(master, text="Player " + str(model.playerValue+1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan = 3)
                self.coords_col_7[1] -= 100
                self.coords_col_7[3] -= 100
                model.makeMove(col)
            else:
                self.c.create_oval(self.coords_col_7[0], self.coords_col_7[1], self.coords_col_7[2], self.coords_col_7[3], fill="red")
                Label(master, text="Player " + str(model.playerValue-1) + " move", font = playerValueFont).grid(row=9, column=2, columnspan=3)
                self.coords_col_7[1] -= 100
                self.coords_col_7[3] -= 100
                model.makeMove(col)
    #Switches the veiw from the GUI to the text view
    #Params: Master represents the root
    #Returns: Closes the GUI and runs the text view
    def switchToText(self,master):
        root.withdraw()
        self.textView(master)

    # Closes the GUI
    # Params: Master represents the root
    # Returns: Nothing
    def quit(self,master):
        master.quit()
    #Runs the text view
    #Params: None
    #Returns: Creates the text view board

#Starts Tkinter window and runs in loop until user exits

def newWindow(master):
    newWin  = Toplevel(master)
    Label(newWin, text ="test")

root = Tk()
start = Controller(root)
root.mainloop()
