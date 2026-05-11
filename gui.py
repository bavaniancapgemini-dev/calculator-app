import tkinter as tk


window = tk.Tk()

window.title("Calculator")

window.geometry("400x400")


entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()


window.mainloop()

def calculate():

    num1 = int(entry1.get())
    num2 = int(entry2.get())

    answer = num1 + num2

    result.config(text=str(answer))


button = tk.Button(
    window,
    text="Add",
    command=calculate
)

button.pack()


result = tk.Label(window, text="")
result.pack()