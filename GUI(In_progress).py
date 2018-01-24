import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage("C:/Users/admin/Desktop/ARTS/Sprites/Riven_sword.png")

w1 = tk.Label(root,image=logo).pack(side="right")

explanation = "This is a sword"

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=explanation).pack(side="left")


root.mainloop()
