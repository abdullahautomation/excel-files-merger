import tkinter as tk
from tkinter import messagebox
from script import start
window = tk.Tk()
window.title("GUI Version")
window.geometry("600x400")
label = tk.Label(window, text="Enter Output File name here: ")
label.pack()
entry = tk.Entry(window)
entry.pack()
def button_click():
    text = entry.get()
    if text.strip() == "":
        messagebox.showerror("Error", "Please Enter File name!")
        return
    result = start(text)
    messagebox.showinfo("Success" ,result)
button = tk.Button(window, text="Run", command=button_click)

button.pack()


window.mainloop()