import tkinter as tk
from PIL import ImageTk, Image
from RPS_functions import *
#from RPS_functions import how2play

window = tk.Tk()
window.title("RPS")
#window.geometry("150x150")

# Game title
lbl = tk.Label(window, text="Rock, Paper and Scissors", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

# Quick Game button
qgButton = tk.Button(window, text="Quick Game", fg="Yellow", bg="Black", command=quickGame)
qgButton.grid(column=0, row=1)

# Marathon button
mButton = tk.Button(window, text="Marathon", fg="Yellow", bg="Black", command=marathon)
mButton.grid(column=0, row=2)

# Tournament button
tButton = tk.Button(window, text="Tournament", fg="Yellow", bg="Black", command=tournament)
tButton.grid(column=0, row=3)

# How to play button
qButton = tk.Button(window, text="How To Play", fg="Blue", command=how2play)
qButton.grid(column=0, row=4)

# Exit button
eButton = tk.Button(window, text="Exit", fg="White", bg="Red", command=window.destroy)
eButton.grid(column=0, row=5)

window.mainloop()
