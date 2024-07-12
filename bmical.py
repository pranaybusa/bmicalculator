import tkinter as tk
from tkinter import ttk

def find_body_mass_index():
    try:
        weight = float(weight_input.get())
        height = float(height_input.get())

        if weight <= 0 or height <= 0:
            output.configure(text='Please enter positive numbers for weight and height.')
            return

        body_mass_index = weight / (height**2)
        output.configure(text='Your BMI is ' + str("%.2f" % body_mass_index))
    except ValueError:
        output.configure(text='Please enter valid information.')

def clear_placeholder(event, placeholder):
    if event.widget.get() == placeholder:
        event.widget.delete(0, tk.END)
        event.widget.config(foreground='black')

 
window = tk.Tk()
window.title('Body Mass Index (BMI) Calculator')
window.minsize(width=500, height=500)
window.maxsize(width=1920, height=1080)
 
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))
 
welcome_label = ttk.Label(window, text='Welcome to the BMI Calculator')
welcome_label.pack(pady=10)

weight_label = ttk.Label(window, text='Enter your weight (kg)')
weight_label.pack(pady=10)

weight_input = ttk.Entry(window, foreground='grey')
weight_input.insert(0, 'e.g., 70')
weight_input.pack(pady=10)
weight_input.bind("<FocusIn>", lambda event: clear_placeholder(event, 'e.g., 70'))

height_label = ttk.Label(window, text='Enter your height (m)')
height_label.pack(pady=10)

height_input = ttk.Entry(window, foreground='grey')
height_input.insert(0, 'e.g., 1.75')
height_input.pack(pady=10)
height_input.bind("<FocusIn>", lambda event: clear_placeholder(event, 'e.g., 1.75'))

calculate_button = ttk.Button(window, text='Calculate', command=find_body_mass_index)
calculate_button.pack(pady=20)

output = ttk.Label(window)
output.pack(pady=10)
 
window.mainloop()
