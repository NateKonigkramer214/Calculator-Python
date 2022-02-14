from tkinter import*

class Calculator():
    def __init__(self):
        self.total = 0 
        self.current = ""
        self.input_value = True
        self.check_result = False
        self.arthmetic_operater = ""
        self.result = False

    def display(self, value):
        txtEntry.delete(0,END)
        txtEntry.insert(0,value)

# clear entry box

    def clear_Entry(self):
        self.result = False
        self.current = 0
        self.display(0)
        self.input_value = True

# clear all

    def clear_all(self):
        self.clear_Entry()
        self.total = '0'

# Backspace

    def backspace(self):
        numlen = len(txtEntry.get())
        txtEntry.delete(numlen - 1, 'end')
        if numlen == 1:
            txtEntry.insert(0, '0')

# Number enter 

    def numberInput(self,num):
        self.result = False
        firstNum = txtEntry.get()
        secondnumber = str(num)
        if self.input_value:
            self.current = secondnumber
            self.input_value = False
        else:
            if secondnumber == '.':
                if secondnumber in firstNum:
                    return
            self.current = firstNum + secondnumber
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_result == True:
            self.valid_function()
        else:
            self.total = float(txtEntry.get())

    def valid_function(self):
        if self.arthmetic_operater == 'add':
            self.total += self.current

        if self.arthmetic_operater == 'sub':
            self.total -= self.current
        
        if self.arthmetic_operater == 'multi':
            self.total *= self.current
        
        if self.arthmetic_operater == 'divide':
            self.total /= self.current
        
        if self.arthmetic_operater == 'in2cm':
            self.total = self.current * 2.54

        if self.arthmetic_operater == 'cm2in':
            self.total = self.current / 2.54

        self.input_value = True 
        self.check_result = False
        self.display(self.total)

    def operation(self,arthmetic_operater):
        self.current = float(self.current)
        if self.check_result:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True

        self.check_result = True
        self.arthmetic_operater = arthmetic_operater
        self.result = False 

get_value = Calculator()

root = Tk()
root.title("Nathan's Calc")
root.config(bg="#fff")

# row - 0 entry box
#label
# entrylabel = Label(root, text='0', width=20, height=2)
# entrylabel.grid(row=0, column=0)

#Entry box
txtEntry = Entry(root, font=('arial', 20, 'bold'),fg='#000', bg='#fff', bd=4, width=22,justify=RIGHT)
txtEntry.grid(row=0, column=0, columnspan=4, pady=1)
txtEntry.insert(0,"0")

# row - 1: division, clear, back,multi 

btn_clear = Button(root, text='C', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#2c3e50',command=get_value.clear_all)
btn_clear.grid(row=1, column=0, padx=4, pady=4)


btn_back = Button(root, text='←', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#2c3e50', command=get_value.backspace)
btn_back.grid(row=1, column=1, padx=4)

btn_div = Button(root, text='/', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#2c3e50', command=lambda:get_value.operation("divide"))
btn_div.grid(row=1, column=2, padx=4)

btn_multi = Button(root, text='*', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#2c3e50',command=lambda:get_value.operation("multi"))
btn_multi.grid(row=1, column=3, padx=4)

# row - 2: 7,8,9, sub 

btn_7 = Button(root, text='7', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#ffdead',command=lambda:get_value.numberInput(7))
btn_7.grid(row=2, column=0, padx=4, pady=4)

btn_8 = Button(root, text='8', width=5, font=('Helvetica', 16, 'bold'),relief='flat',bg='#ffdead',command=lambda:get_value.numberInput(8))
btn_8.grid(row=2, column=1, padx=4)

btn_9 = Button(root, text='9', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#ffdead',command=lambda:get_value.numberInput(9))
btn_9.grid(row=2, column=2, padx=4)

btn_sub = Button(root, text='-', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#2c3e50',command=lambda:get_value.operation("sub"))
btn_sub.grid(row=2, column=3, padx=4)

# Row 3: 4, 5, 6, +

btn_4 = Button(root, text='4', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#ffdead',command=lambda:get_value.numberInput(4))
btn_4.grid(row=3, column=0, padx=4, pady=4)

btn_5 = Button(root, text='5', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#ffdead',command=lambda:get_value.numberInput(5))
btn_5.grid(row=3, column=1, padx=4)

btn_6 = Button(root, text='6', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#ffdead',command=lambda:get_value.numberInput(6))
btn_6.grid(row=3, column=2, padx=4)

btn_plus = Button(root, text='+', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#2c3e50',command=lambda:get_value.operation("add"))
btn_plus.grid(row=3, column=3, padx=4)

# Row 4: 1, 2, 3, =

btn_1 = Button(root, text='1', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#ffdead',command=lambda:get_value.numberInput(1))
btn_1.grid(row=4, column=0, padx=4, pady=4)

btn_2 = Button(root, text='2', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#ffdead',command=lambda:get_value.numberInput(2))
btn_2.grid(row=4, column=1, padx=4)

btn_3 = Button(root, text='3', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#ffdead',command=lambda:get_value.numberInput(3))
btn_3.grid(row=4, column=2, padx=4)

btn_equals = Button(root, text='=', width=5, height=3, font=('Helvetica', 16, 'bold'),relief='flat', bg='#34495e', command=get_value.sum_of_total)
btn_equals.grid(row=4, column=3, rowspan=2, padx=4)

# Row 5: 0, .

btn_0 = Button(root, text='0', width=12, font=('Helvetica', 16, 'bold'),relief='flat', bg='#ffdead',command=lambda:get_value.numberInput(0))
btn_0.grid(row=5, column=0,columnspan=2, padx=4, pady=4)

btn_dot = Button(root, text='.', width=5, font=('Helvetica', 16, 'bold'),relief='flat', bg='#ffdead',command=lambda:get_value.numberInput("."))
btn_dot.grid(row=5, column=2, padx=4)

# row : 6 cm to in, in to cm. 

btn_intocm = Button(root, text='In to CM', width=12, font=('Helvetica', 16, 'bold'), relief='flat', bg='#2c3e50',command=lambda:get_value.operation("in2cm"))
btn_intocm.grid(row=6, column=0,columnspan=2, padx=4, pady=4)

btn_cmtoin = Button(root, text='Cm to In', width=12, font=('Helvetica', 16, 'bold'), relief='flat', bg='#2c3e50',command=lambda:get_value.operation("cm2in"))
btn_cmtoin.grid(row=6, column=2,columnspan=2, padx=4, pady=4)


root.mainloop()

