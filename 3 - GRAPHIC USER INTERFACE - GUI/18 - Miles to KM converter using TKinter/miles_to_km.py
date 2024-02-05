import tkinter

def calculate():
    miles = float(input.get())  # Get the input from the entry and convert it to float
    new_miles_converted = miles * 1.609344  # Convert miles to kilometers
    miles_converted.config(text=new_miles_converted)

    # Update the label for 'Km' or 'Kms' based on the calculated value
    label_kms.config(text='Kms' if new_miles_converted > 2 else 'Km')

#--------------------------------------------------------------------------------------------------

#create a windown
window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=400, height=200)
window.config(padx=20, pady=20) #adds a space between the windown and the widgets

#--------------------------------------------------------------------------------------------------

# Input field for miles
input = tkinter.Entry(width=10, font=('Arial', 18))
input.grid(row=0, column=1, padx=5, pady=5)

# label miles
label_miles = tkinter.Label(text='miles', font=('Arial', 18, 'bold'))
label_miles.grid(row=0, column=2, padx=5, pady=5) #make it apper on the screen

# Label for 'is equal to'
label_equal_to = tkinter.Label(text='is equal to', font=('Arial', 18, 'bold'))
label_equal_to.grid(row=1, column=0, padx=5, pady=5)

# Miles to kilometers conversion result label
miles_converted = tkinter.Label(text ='0.00', font=('Arial', 18, 'bold')) #create label
miles_converted.grid(row=1, column=1, padx=5, pady=5) #make it appear on the screen

# Label for 'Kms' or 'Km'
label_kms = tkinter.Label(text='', font=('Arial', 18, 'bold'))
label_kms.grid(row=1, column=2, padx=5, pady=5)

# Button to calculate
button = tkinter.Button(text='Calculate', command=calculate, font=('Arial', 18))
button.grid(row=0, column=3, padx=5, pady=5)

#--------------------------------------------------------------------------------------------------
# Start the GUI event loop
window.mainloop()