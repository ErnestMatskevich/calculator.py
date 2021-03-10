
from tkinter import *
from tkinter import messagebox

import math
import sys

root = Tk()
root.title("Calculator")
canvas = Canvas()


# Create support functions for Menu. New padge with information about author and instructions
def show_read():
    read = Tk()
    read.title("Справка")

    read.geometry("800x600")

    Label(read, text = 'Программа - калькулятор, для работы необходимо ввести в поле ввода выражение с клавиатуры \n или с помошью кнопок, рсположенных ниже.').grid(row=1,column=1)


def show_about():
    about = Tk()
    about.title("О программе")


def Exit():
    root.after(1, root.destroy)
    sys.exit

def vals():
    a = int(disp_a.get())
    b = int(disp_b.get())
    c = int(disp_c.get())

    if a == 0:
        X = -(b/c)
        Label(root, text="X: " + str(X)).grid(row=9, column=0)
    else:
        D = b**2 - 4*a*c
        X1 = (-b-D**0.5)/2*a
        X2 = (-b+D**0.5)/2*a

        if D == 0:
            Label(root, text="D: " + str(D)).grid(row=9, column=0)
            Label(root, text="X: " + str(X1)).grid(row=9, column=1)
        else:
            Label(root, text = "D: " + str(D)).grid(row=9,column=0)
            Label(root, text = "X1: " + str(X1)).grid(row=9,column=1)
            Label(root, text = "X2: " + str(X2)).grid(row=9, column=2)
# Create Menu
mainmenu = Menu(root) 
root.config(menu=mainmenu)


# Added comands to main Menu
filemenu = Menu(mainmenu, tearoff=0)


filemenu.add_command(label="Прочитать справку", command=show_read)
filemenu.add_separator()
filemenu.add_command(label="О программе", command=show_about)
mainmenu.add_cascade(label="Справка", menu=filemenu)
mainmenu.add_command(label="Выход", command=Exit)


but_list = [
"sin", "cos", "tan", "ctg",
"C", "√x", "xⁿ", "*",
"7", "8", "9", "/", 
"6", "5", "4",  "-", 
"3", "2", "1",  "+",
"±", "0", ",", "="]

r = 1
c = 0
for i in but_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    Button(root, text=i, command=cmd, overrelief="ridge",width=6, bg="#F8F8FF",  activebackground="#DCDCDC").grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1
    if r == 5 and c == 4:
        Button(root, text=i,command = cmd, width = 6).grid(row=5, column = 3)



disp = Entry(root, width = 33)
disp.grid(row=0, column=0, columnspan=5)

# Уравнения
text_a = Label(root, text="ax^2")
text_a.grid(row=7,column=0)

disp_a = Entry(root, width = 6)
disp_a.grid(row=8,column=0)

text_b = Label(root, text="bx")
text_b.grid(row=7,column=1)

disp_b = Entry(root, width = 6)
disp_b.grid(row=8,column=1)

text_c = Label(root, text="c")
text_c.grid(row=7,column=2)

disp_c = Entry(root, width = 6)
disp_c.grid(row=8,column=2)

Button(root, text="Enter",overrelief="ridge",width=6, bg="#F8F8FF",  activebackground="#DCDCDC", command = vals).grid(row=8,column=3)

#Label(root, text="X1=").grid(row=9, column=0)

def calc(key):
    global memory
    if key == "=":
#исключение написания слов
        str1 = "-+0123456789.*/)(" 
        if disp.get()[0] not in str1:
            #disp.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
#исчисления
        try:
            result = eval(disp.get())
            disp.insert(END, "=" + str(result))
        except:
            disp.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")


        #очищение поля ввода
    elif key == "C":
        disp.delete(0, END)
             
    
            

    elif key == "±":
        if "=" in disp.get():
            disp.delete(0, END)
        try:
            if disp.get()[0] == "-":
                disp.delete(0)
            else:
                disp.insert(0, "-")
        except IndexError:
            pass


  

    elif key == "sin":
        disp.insert(END, "=" + str(math.sin(int(disp.get()))))
        
    elif key == "cos":
        disp.insert(END, "=" + str(math.cos(int(disp.get()))))
        
    elif key == "tan":
        disp.insert(END, "=" + str(math.tan(int(disp.get()))))
        
    elif key == "ctg":
        disp.insert(END, "=" + str(1/(math.tan(int(disp.get())))))
        

        


  
    elif key == "√x":
        disp.insert(END, "=" + str(math.sqrt(int(disp.get()))))


    elif key == "xⁿ":
        disp.insert(END, "**")



    else:
        if "=" in disp.get():
            disp.delete(0, END)
        disp.insert(END, key)
    
    

root.resizable(False, False)
root.geometry("210x575")
root.mainloop()
