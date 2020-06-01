from tkinter import *
import numpy
root=Tk()
root.title("Tic Tac Toe")
board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'
turn=0
def chance():
    global turn
    turn+=1

def click(number):
    if number==11:
        if turn%2==0:
            Button_11=Button(root, text="X",padx=40,pady=40)
            Button_11.grid(row=0,column=0)
            board[0][0]="X"
            if won(p1s):
                myLabel=Label(root,text="x wins")
                myLabel.grid(row=3,column=0)
            
        else:
            Button_11=Button(root, text="O",padx=40,pady=40)
            Button_11.grid(row=0,column=0)
            board[0][0]="O"
            if won(p2s):
                myLabel=Label(root,text="O wins")
                myLabel.grid(row=3,column=0)
                
    if number==12:
        if turn%2==0:
            Button_12=Button(root, text="X",padx=40,pady=40)
            Button_12.grid(row=0,column=1)
            board[0][1]="X"
            if won(p1s):
                myLabel=Label(root,text="x wins")
                myLabel.grid(row=3,column=0)
                
        else:
            Button_12=Button(root, text="O",padx=40,pady=40)
            Button_12.grid(row=0,column=1)
            board[0][1]="O"
            if won(p2s):
                myLabel=Label(root,text="O wins")
                myLabel.grid(row=3,column=0)
                
    if number==13:
        if turn%2==0:
            Button_13=Button(root, text="X",padx=40,pady=40)
            Button_13.grid(row=0,column=2)
            board[0][2]="X"
            if won(p1s):
                myLabel=Label(root,text="x wins")
                myLabel.grid(row=3,column=0)
                
        else:
            Button_13=Button(root, text="O",padx=40,pady=40)
            Button_13.grid(row=0,column=2)
            board[0][2]="O"
            if won(p2s):
                myLabel=Label(root,text="O wins")
                myLabel.grid(row=3,column=0)
                
    if number==21:
        if turn%2==0:
            Button_21=Button(root, text="X",padx=40,pady=40)
            Button_21.grid(row=1,column=0)
            board[1][0]="X"
            if won(p1s):
                myLabel=Label(root,text="x wins")
                myLabel.grid(row=3,column=0)
                
        else:
            Button_21=Button(root, text="O",padx=40,pady=40)
            Button_21.grid(row=1,column=0)
            board[1][0]="O"
            if won(p2s):
                myLabel=Label(root,text="O wins")
                myLabel.grid(row=3,column=0)
                
    if number==22:
        if turn%2==0:
            Button_22=Button(root, text="X",padx=40,pady=40)
            Button_22.grid(row=1,column=1)
            board[1][1]="X"
            if won(p1s):
                myLabel=Label(root,text="x wins")
                myLabel.grid(row=3,column=0)
                
        else:
            Button_22=Button(root, text="O",padx=40,pady=40)
            Button_22.grid(row=1,column=1)
            board[1][1]="O"
            if won(p2s):
                myLabel=Label(root,text="O wins")
                myLabel.grid(row=3,column=0)
                
    if number==23:
        if turn%2==0:
            Button_23=Button(root, text="X",padx=40,pady=40)
            Button_23.grid(row=1,column=2)
            board[1][2]="X"
            if won(p1s):
                myLabel=Label(root,text="x wins")
                myLabel.grid(row=3,column=0)
                
        else:
            Button_23=Button(root, text="O",padx=40,pady=40)
            Button_23.grid(row=1,column=2)
            board[1][2]="O"
            if won(p2s):
                myLabel=Label(root,text="O wins")
                myLabel.grid(row=3,column=0)
                
    if number==31:
        if turn%2==0:
            Button_31=Button(root, text="X",padx=40,pady=40)
            Button_31.grid(row=2,column=0)
            board[2][0]="X"
            if won(p1s):
                myLabel=Label(root,text="x wins")
                myLabel.grid(row=3,column=0)
                
        else:
            Button_31=Button(root, text="O",padx=40,pady=40)
            Button_31.grid(row=2,column=0)
            board[2][0]="O"
            if won(p2s):
                myLabel=Label(root,text="O wins")
                myLabel.grid(row=3,column=0)
                
    if number==32:
        if turn%2==0:
            Button_32=Button(root, text="X",padx=40,pady=40)
            Button_32.grid(row=2,column=1)
            board[2][1]="X"
            if won(p1s):
                myLabel=Label(root,text="X wins")
                myLabel.grid(row=3,column=0)
                
        else:
            Button_32=Button(root, text="O",padx=40,pady=40)
            Button_32.grid(row=2,column=1)
            board[2][1]="O"
            if won(p2s):
                myLabel=Label(root,text="O wins")
                myLabel.grid(row=3,column=0)
                
    if number==33:
        if turn%2==0:
            Button_33=Button(root, text="X",padx=40,pady=40)
            Button_33.grid(row=2,column=2)
            board[2][2]="X"
            if won(p1s):
                myLabel=Label(root,text="x wins")
                myLabel.grid(row=3,column=0)
                
        else:
            Button_33=Button(root, text="O",padx=40,pady=40)
            Button_33.grid(row=2,column=2)
            board[2][2]="O"
            if won(p2s):
                myLabel=Label(root,text="O wins")
                myLabel.grid(row=3,column=0)
                
            
    chance()


def check_rows(symbol):
    for r in range (3):
        count =0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            return True
    return False

def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range (3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            return True
    return False

def check_diagonals(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)
        

Button_11=Button(root, text="--",padx=40,pady=40,command=lambda: click(11))
Button_12=Button(root, text="--",padx=40,pady=40,command=lambda: click(12))
Button_13=Button(root, text="--",padx=40,pady=40,command=lambda: click(13))

Button_21=Button(root, text="--",padx=40,pady=40,command=lambda: click(21))
Button_22=Button(root, text="--",padx=40,pady=40,command=lambda: click(22))
Button_23=Button(root, text="--",padx=40,pady=40,command=lambda: click(23))

Button_31=Button(root, text="--",padx=40,pady=40,command=lambda: click(31))
Button_32=Button(root, text="--",padx=40,pady=40,command=lambda: click(32))
Button_33=Button(root, text="--",padx=40,pady=40,command=lambda: click(33))
myLabel=Label(root, text="   ")



Button_11.grid(row=0,column=0)
Button_12.grid(row=0,column=1)
Button_13.grid(row=0,column=2)
Button_21.grid(row=1,column=0)
Button_22.grid(row=1,column=1)
Button_23.grid(row=1,column=2)
Button_31.grid(row=2,column=0)
Button_32.grid(row=2,column=1)
Button_33.grid(row=2,column=2)
myLabel.grid(row=3,column=0)




root.mainloop()

