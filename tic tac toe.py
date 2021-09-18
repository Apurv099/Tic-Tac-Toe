from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("TIC TAC TOE")
#to rename the title of the window

#window.geometry("300x300")
#window ka intial size set karne ke 





#widgets:
'''A element in the GUI that displays information or provides
   a specific way for a user to interact with the operating system or application'''

#Label - is a single line widget used to display text or image
#Label can also be used to manipulate font size and style
#l1=Label(window,text="MY NAME IS AKSHAY",font=("Arial Bold",15))
#l1.grid(column=1,row=0)

#pack is used to show the object in the window
#label=Label(window,text="Hello World").pack()
#upar vala  use kiya to ye vale mai errir aayega
#cannot use geometry manager pack inside .
#which already has slaves managed by grid

#X goes first
clicked=True
count=0

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    

def wincheck(btn):
    global winner
    winner=False
    row    = btn.grid_info()['row']      # Row of the button
    col = btn.grid_info()['column']  #column of the button

    #row check 
    if(row==0):
        if(b1["text"]==b2["text"] and b2["text"]==b3["text"]):
            winner=True
            if(b1["text"]=="X"):
                
                b1.config(bg="green")
                b2.config(bg="green")
                b3.config(bg="green")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 1 WINS")
            else:
                
                b1.config(bg="red")
                b2.config(bg="red")
                b3.config(bg="red")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 2 WINS")
            disable_all_buttons()
    elif(row==1):
        
        if(b4["text"]==b5["text"] and b5["text"]==b6["text"]):
            winner=True
            if(b4["text"]=="X"):
                
                b4.config(bg="green")
                b5.config(bg="green")
                b6.config(bg="green")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 1 WINS")
            else:
                b4.config(bg="red")
                b5.config(bg="red")
                b6.config(bg="red")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 2 WINS")
            disable_all_buttons()
    elif(row==2):
        if(b7["text"]==b8["text"] and b8["text"]==b9["text"]):
            winner=True
            if(b7["text"]=="X"):
                b7.config(bg="green")
                b8.config(bg="green")
                b9.config(bg="green")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 1 WINS")
            else:
                
                b7.config(bg="red")
                b8.config(bg="red")
                b9.config(bg="red")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 2 WINS")
            disable_all_buttons()

    #column check
    if(col==0):
        if(b1["text"]==b4["text"] and b4["text"]==b7["text"]):
            winner=True
            if(b1["text"]=="X"):
                b1.config(bg="green")
                b4.config(bg="green")
                b7.config(bg="green")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 1 WINS")
            else:
                
                b1.config(bg="red")
                b4.config(bg="red")
                b7.config(bg="red")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 2 WINS")
            disable_all_buttons()
    elif(col==1):
        if(b2["text"]==b5["text"] and b5["text"]==b8["text"]):
            winner=True
            if(b2["text"]=="X"):
                
                b2.config(bg="green")
                b5.config(bg="green")
                b8.config(bg="green")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 1 WINS")
            else:
                
                b2.config(bg="red")
                b5.config(bg="red")
                b8.config(bg="red")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 2 WINS")
            disable_all_buttons()
    elif(col==2):
        if(b3["text"]==b6["text"] and b6["text"]==b9["text"]):
            winner=True
            if(b3["text"]=="X"):
                
                b3.config(bg="green")
                b6.config(bg="green")
                b9.config(bg="green")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 1 WINS")
            else:
                
                b3.config(bg="red")
                b6.config(bg="red")
                b9.config(bg="red")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 2 WINS")
            disable_all_buttons()

    #diagonal
    if(row==col):
        if(b1["text"]==b5["text"] and b5["text"]==b9["text"]):
            winner=True
            if(b1["text"]=="X"):
                b1.config(bg="green")
                b5.config(bg="green")
                b9.config(bg="green")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 1 WINS")
            else:
                b1.config(bg="red")
                b5.config(bg="red")
                b9.config(bg="red")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 2 WINS")
            disable_all_buttons()
    if(row== col-2):
       if(b3["text"]==b5["text"] and b5["text"]==b7["text"]):
            winner=True
            if(b1["text"]=="X"):
                b3.config(bg="green")
                b5.config(bg="green")
                b7.config(bg="green")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 1 WINS")
            else:
                b3.config(bg="red")
                b5.config(bg="red")
                b7.config(bg="red")
                messagebox.showinfo("Tic Tac Toe Game","PLAYER 2 WINS")
            disable_all_buttons()
    if(count==9 and winner == False):
        b1.config(bg="black")
        b2.config(bg="black")
        b3.config(bg="black")
        b4.config(bg="black")
        b5.config(bg="black")
        b6.config(bg="black")
        b7.config(bg="black")
        b8.config(bg="black")
        b9.config(bg="black")
        messagebox.showinfo("Tic Tac Toe Game","GAME TIED!!!!")
        disable_all_buttons()


def b_click(b):
    global clicked ,count
    if(b["text"]==" " and  clicked==True):
        b["text"]="X"
        clicked=False
        count+=1
        wincheck(b)
    elif(b["text"]==" " and  clicked==False):
        b["text"]="O"
        clicked=True
        count+=1
        wincheck(b)
    else:
        messagebox.showerror("Tice Tac Toe", "place is already full please enter correclty!!!")

def reset():
#creating the buttons
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked=True
    count=0
    b1=Button(window,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b1))
    b2=Button(window,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b2))
    b3=Button(window,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b3))

    b4=Button(window,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b4))
    b5=Button(window,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b5))
    b6=Button(window,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b6))

    b7=Button(window,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b7))
    b8=Button(window,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b8))
    b9=Button(window,text=" ",font=("Helvetica",20),height=3,width=6,bg="SystemButtonFace",command=lambda: b_click(b9))

#creating the grid for buttons

    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

my_menu=Menu(window)
window.config(menu=my_menu)


reset()
options_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Reset Game",command=lambda : reset())


window.mainloop()
