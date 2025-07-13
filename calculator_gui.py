import tkinter as tk

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "خطأ")

def press(x):
    if x == '=':
        equal()
    else:
        entry.insert(tk.END, x)

root = tk.Tk()
root.title("آلة حاسبة")

entry = tk.Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

row = 1
col = 0

for line in buttons:
    for char in line:
        btn = tk.Button(root, text=char, width=5, height=2, font=('Arial', 18),
                        command=lambda ch=char: press(ch))
        btn.grid(row=row, column=col)
        col += 1
    row += 1
    col = 0

clear_btn = tk.Button(root, text="مسح", width=20, height=2, font=('Arial', 14), command=clear)
clear
