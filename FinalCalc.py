from tkinter import *
root = Tk()
root.geometry('500x500+450+150')
root.title('Calculator')
root.config(bg='#223441')
root.resizable(width=False, height=False)

def button_click(number):
    enter.insert(END, number)

def button_clear():
    enter.delete(0, END)

def button_add():
    first_number = enter.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    enter.delete(0, END)

def button_equal():
    second_number = enter.get()
    enter.delete(0, END)

    if math == "addition":
        enter.insert(0, f_num + int(second_number))

    if math == "subtraction":
        enter.insert(0, f_num - int(second_number))

    if math == "multiplication":
        enter.insert(0, f_num * int(second_number))

    if math == "division":
        enter.insert(0, f_num / int(second_number))

def button_sub():
    first_number = enter.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    enter.delete(0, END)

def button_mul():
    first_number = enter.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    enter.delete(0, END)

def button_div():
    first_number = enter.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    enter.delete(0, END)

enter = Entry(root, width=60, font=('arial', 8, 'bold'), borderwidth=5)
enter.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = Button(root, text="1", font=14, padx=40, pady=30, command=lambda : button_click(1))
button_2 = Button(root, text="2", font=14, padx=40, pady=30, command=lambda : button_click(2))
button_3 = Button(root, text="3", font=14, padx=40, pady=30, command=lambda : button_click(3))
button_4 = Button(root, text="4", font=14, padx=40, pady=30, command=lambda : button_click(4))
button_5 = Button(root, text="5", font=14, padx=40, pady=30, command=lambda : button_click(5))
button_6 = Button(root, text="6", font=14, padx=40, pady=30, command=lambda : button_click(6))
button_7 = Button(root, text="7", font=14, padx=40, pady=30, command=lambda : button_click(7))
button_8 = Button(root, text="8", font=14, padx=40, pady=30, command=lambda : button_click(8))
button_9 = Button(root, text="9", font=14, padx=40, pady=30, command=lambda : button_click(9))
button_0 = Button(root, text="0", font=14, padx=40, pady=30, command=lambda : button_click(0))
button_add = Button(root, text="+", font=14, padx=40, pady=30, command=button_add)
button_subtract = Button(root, text="-", font=14, padx=40, pady=30, command=button_sub)
button_multiply = Button(root, text="*", font=14, padx=40, pady=30, command=button_mul)
button_division = Button(root, text="/", font=14, padx=40, pady=30, command=button_div)
button_equals = Button(root, text="=", font=14, padx=40, pady=30, command=button_equal)
button_clear = Button(root, text="C", font=14, padx=40, pady=30, command=button_clear)

# put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_division.grid(row=1, column=3)

button_equals.grid(row=4, column=2)
button_clear.grid(row=4, column=0)

root.mainloop()