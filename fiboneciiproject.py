from tkinter import*

root = Tk()
root.title("Fibonaccii Sum")
root.geometry("400x400")

input_var = Entry()
label_sum = Label(root)
label_fibonacci = Label(root)

def fibonacii_series():
    num= int(input_var.get())
    number1=0
    number2=1
    sum=0
    sum2=0
    repeat=1
    
    while repeat<=num:
        repeat=repeat+1
        number1=number2
        number2=sum
        sum=number1+number2
        sum2=sum+sum2
        
        label_fibonacci["text"]+=str(sum)+" "
        label_sum["text"]="Fibonacii Sum = " + str(sum2)
      
button1 = Button(root,text="Show Fibonacii Series",command=fibonacii_series,fg="blue",bg="red")

input_var.pack()
button1.pack()
label_fibonacci.pack()
label_sum.pack()
root.mainloop()