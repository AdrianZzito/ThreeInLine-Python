import tkinter as tk
import Logic, Methods


window = tk.Tk()
window.title("Three in Line")
window.config(width=400, height=400)
a1 = tk.Button(window, text=Logic.a1, command=Methods.movement(where="a1", who="player 1"))
window.mainloop()