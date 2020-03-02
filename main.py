from tkinter import *
import tkinter.font
import tkinter.messagebox
import numpy


#Text-Based and GUI
class view():

    def __init__(self, master):
        option = input("Type text or gui for your version of Connect Four")
        if option == "gui":
            # mainFrame = Frame(master,width = 1000, height = 1000)
            # mainFrame.grid()
            header = tkinter.font.Font(size = 20, weight = tkinter.font.BOLD)
            Label(master, text = "Connect Four" , anchor = N, font = header).grid(row =0, column =0)

            player1= True

            c = Canvas(master, width = 700, height = 600)
            c.create_rectangle(0,0,700,600, fill = "gray")
            c.grid()
            # Create Seperation from Board to have buttons and exit/switch view buttons
            bottomFrame = Frame(master, width=700, height = 200)
            bottomFrame.grid(row=3, column = 0)

            row1 = Button(bottomFrame, text = "Add Piece to Row 1", command = lambda: self.addPiece(c, player1))
            row1.grid(row = 4 , column = 0, sticky = E)
            row2 = Button(bottomFrame, text="Add Piece to Row 2", command= lambda: self.addPiece(c,player1))
            row2.grid(row=4, column=1, sticky=E)
        else:

            self.textView()

    #
    def addPiece(self,canvas, player1):
        x,y = 20,20

        if player1:
            canvas.create_oval(x, y, 6, 6, fill="black")

            player1 = False
        else:
            canvas.create_oval(x, y, .5, .5, fill="red")
            canvas.grid(row=1, column=0)
            player1 = True

    def textView(self):

        #Build Board
        board = numpy.zeros((6,7))
        run = True
        playerValue = 1
        row = 0



        def checkRow(board,colChoice):
            for rowNum in range(6):
                if board[rowNum][colChoice] == 0:
                    return rowNum


        while(run):
            colChoice = int(input("Which Column 0,1,2,3,4,5, or 6"))

            if playerValue == 1:
                row = checkRow(board,colChoice)
                board[row][colChoice] = playerValue
                playerValue += 1
            else:
                row = checkRow(board, colChoice)
                board[row][colChoice] = playerValue
                playerValue -= 1

            if colChoice == 7:
                break
            print(board)



root = Tk()
start = view(root)
root.mainloop()



#Handle Connecting view and model
class controller():

    def __init__(self):
        pass



#Handle Logic
class model():

    def __init__(self):
        pass
