from tkinter import *

root = Tk()

def button_add():
    return

button_1 = Button(root, text="1", padx=40, pady=20, command = button_add)
button_2 = Button(root, text="2", padx=40, pady=20, command = button_add)
button_3 = Button(root, text="3", padx=40, pady=20, command = button_add)
button_4 = Button(root, text="4", padx=40, pady=20, command = button_add)
button_5 = Button(root, text="5", padx=40, pady=20, command = button_add)
button_6 = Button(root, text="6", padx=40, pady=20, command = button_add)
button_7 = Button(root, text="7", padx=40, pady=20, command = button_add)
button_8 = Button(root, text="8", padx=40, pady=20, command = button_add)
button_9 = Button(root, text="9", padx=40, pady=20, command = button_add)
button_0 = Button(root, text="0", padx=40, pady=20, command = button_add)
button_add = Button(root, text="+", padx=40, pady=20, command = button_add)
button_equal = Button(root, text="=", padx=40, pady=20, command = button_add)
button_clear = Button(root, text="Clear", padx=40, pady=20, command = button_add)

# Put buttons on the screen

button_1.grid(row =3, cloumn =0)
button_2.grid(row =3, cloumn =1)
button_3.grid(row =3, cloumn =2)
button_4.grid(row =2, cloumn =3)
button_5.grid(row =2, cloumn =0)
button_6.grid(row =2, cloumn =1)
button_7.grid(row =1, cloumn =2)
button_8.grid(row =1, cloumn =3)
button_9.grid(row =1, cloumn =1)
button_0.grid(row =4, cloumn =0)
button_add.grid(row =3, cloumn =3)
root.mainloop()