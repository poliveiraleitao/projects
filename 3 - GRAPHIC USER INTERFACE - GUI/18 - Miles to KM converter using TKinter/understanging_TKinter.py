import tkinter

def button_clicked():
    print('i got clicked')
    new_label_text = input.get() #get the input from the entry
    my_label.config(text = new_label_text)


#create a windown
window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) #adds a space between the windown and the widgets

#label
my_label = tkinter.Label(text = 'I am a Label', font=('Arial', 24, 'bold')) #create label
my_label.grid(row=0, column=1) #make it appear on the screen
my_label.config(padx=5, pady=5) #adds a space between the windown and the widgets

#buttom
button = tkinter.Button(text = 'click me', command=button_clicked)
button.grid(row=1, column=0) #make it appear on the screen
button.config(padx=5, pady=5)

# Entry
input = tkinter.Entry(width=20)
input.grid(row=1, column=1)












#keep window open
window.mainloop()

