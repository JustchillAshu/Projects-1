from tkinter import *
import pyperclip
import random
# initialing tkinter using tk() method
root=Tk()
# setting the size of gui
root.geometry("400x350")
#declaring variable of string type to store password
strpass=StringVar()

lenpass=IntVar()
lenpass.set(0)
def passgenerate():
    keyss=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']
    password=""
    for i in range(lenpass.get()):
        password+=random.choice(keyss)
    #setting the password to entry widgets
    
    strpass.set(password)
#to copy password to clipboard
def copytoclip():
    ranpass=strpass.get()
    pyperclip.copy(ranpass)
    
#creating label
Label(root,text="Password GUI",font="calibri 20 bold").pack()
#creating a text label
Label(root,text="Enter password length").pack(pady=3)
#creating entry widget
Entry(root,textvariable=lenpass).pack(pady=3)
#creating label forwebsite name

Label(root,text="Enter website name").pack(pady=3)
#creating button to call generate
Button(root, text="Generate Password", command=passgenerate).pack(pady=7)

# entry widget to show the generated password
Entry(root, textvariable=strpass).pack(pady=3)

# button to call the copytoclipboard function
Button(root, text="Copy to clipboard", command=copytoclip).pack()

# mainloop() is an infinite loop used to run the application when 
# it's in ready state 
root.mainloop()


