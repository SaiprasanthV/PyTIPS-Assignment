from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# e.insert(0, 'Enter the Value:')


def button_append(val):
    num = e.get()
    e.delete(0, END)
    e.insert(0, num + val)


def button_clr():
    e.delete(0, END)


def button_popping():
    num = e.get()
    e.delete(0, END)
    e.insert(0, num[:-1])


def button_eqaual():
    num = e.get()
    e.delete(0, END)
    e.insert(0, eval(num))


button1 = Button(root, text='1', padx=30, pady=20,
                 command=lambda: button_append('1'))
button2 = Button(root, text='2', padx=30, pady=20,
                 command=lambda: button_append('2'))
button3 = Button(root, text='3', padx=30, pady=20,
                 command=lambda: button_append('3'))
button4 = Button(root, text='4', padx=30, pady=20,
                 command=lambda: button_append('4'))
button5 = Button(root, text='5', padx=30, pady=20,
                 command=lambda: button_append('5'))
button6 = Button(root, text='6', padx=30, pady=20,
                 command=lambda: button_append('6'))
button7 = Button(root, text='7', padx=30, pady=20,
                 command=lambda: button_append('7'))
button8 = Button(root, text='8', padx=30, pady=20,
                 command=lambda: button_append('8'))
button9 = Button(root, text='9', padx=30, pady=20,
                 command=lambda: button_append('9'))
button0 = Button(root, text='0', padx=30, pady=20,
                 command=lambda: button_append('0'))
button_add = Button(root, text='+', padx=29, pady=20,
                    command=lambda: button_append('+'))
button_sub = Button(root, text='-', padx=30, pady=20,
                    command=lambda: button_append('-'))
button_mul = Button(root, text='*', padx=30, pady=20,
                    command=lambda: button_append('*'))
button_div = Button(root, text='/', padx=30, pady=20,
                    command=lambda: button_append('/'))
button_eql = Button(root, text='=', padx=28, pady=20, command=button_eqaual)
button_clear = Button(root, text='C', padx=68, pady=20, command=button_clr)
button_pop = Button(root, text='X', padx=68, pady=20,
                    command=button_popping)
button_perc = Button(root, text='%', padx=30, pady=20,
                     command=lambda: button_append('/100'))
button_sq = Button(root, text='x²', padx=29, pady=20,
                   command=lambda: button_append('**2'))
button_sqrt = Button(root, text='√', padx=30, pady=20,
                     command=lambda: button_append('**(1/2)'))
button_frac = Button(root, text='⅟x', padx=27, pady=20,
                     command=lambda: button_append('1/'))
button_dot = Button(root, text='.', padx=32, pady=20,
                    command=lambda: button_append('.'))


button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)
button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=6, column=0)
button_add.grid(row=6, column=3)
button_sub.grid(row=5, column=3)
button_mul.grid(row=4, column=3)
button_div.grid(row=3, column=3)
button_eql.grid(row=6, column=2)
button_clear.grid(row=2, column=0, columnspan=2)
button_pop.grid(row=2, column=2, columnspan=2)
button_perc.grid(row=1, column=0)
button_sq.grid(row=1, column=1)
button_sqrt.grid(row=1, column=2)
button_frac.grid(row=1, column=3)
button_dot.grid(row=6, column=1)


root.mainloop()
