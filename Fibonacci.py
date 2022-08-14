from tkinter import *
root = Tk()
root.title("Fibonacci")
root.geometry("400x200")

label_series = Label(root,text = "fibonacci series : ")
label_flower = Label(root)
label_spiral = Label(root)

def fibonacci():
    first_no  = 0 
    second_no = 1
    sum = 0 
    num = 10
    count = 1

    while(count <= num):
        label_series["text"] +=str(sum) + " "
        count = count + 1
        first_no = second_no
        second_no = sum
        sum = first_no  + second_no
    
    label_flower["text"] = "flower is still blooming."
    label_spiral["text"] = "Spirals in right direction are " + str(first_no) + " and spirals in left direction are " + str(second_no) + "\n. Total spiral are " + str(sum)    
    
btn = Button(root,text = "show fibonacci series", command = fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()
       
    