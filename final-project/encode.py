import tkinter as tk

# setup a root element
root = tk.Tk()

# add a label and an entry box
tk.Label(root, text='Message To Send').grid(row=9, column=5)
message = tk.Entry(root)
message.grid(row=10, column=5)

root.mainloop()

print(message)
