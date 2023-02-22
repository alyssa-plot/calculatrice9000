import tkinter as tk

master = tk.Tk()
master.title("Calculatrice")

def reception(nombres):
    current = affichage.get()
    affichage.delete(0, tk.END)
    affichage.insert(0, str(current) + str(nombres))

def egal():
    current = affichage.get()
    affichage.delete(0, tk.END)
    try:
        affichage.insert(0, eval(current))
    except:
        affichage.insert(0, "Erreur")

def clear():
    affichage.delete(0, tk.END)

affichage = tk.Entry(master, width=35, borderwidth=5)
affichage.grid(columnspan=7)

btn1 = tk.Button(master, text="1",width=6,height=2, command=lambda: reception(1))
btn1.grid(column = 0, row = 3)

btn2 = tk.Button(master, text="2", width=6,height=2, command=lambda: reception(2))         
btn2.grid(column = 1, row = 3) 

btn3 = tk.Button(master, text="3", width=6,height=2, command=lambda: reception(3))        
btn3.grid(column = 2, row = 3) 

addition = tk.Button(master, text="+", width=6,height=2, command=lambda: reception("+"))
addition.grid(column = 3, row = 3) 

btn4 = tk.Button(master, text="4", width=6,height=2, command=lambda: reception(4))         
btn4.grid(column = 0, row = 4) 

btn5 = tk.Button(master, text="5", width=6,height=2, command=lambda: reception(5))       
btn5.grid(column = 1, row = 4)

btn6 = tk.Button(master, text="6", width=6,height=2, command=lambda: reception(6))         
btn6.grid(column = 2, row = 4) 

soustraire = tk.Button(master, text="-", width=6,height=2, command=lambda: reception("-"))
soustraire.grid(column = 3, row = 4) 

btn7 = tk.Button(master, text="7", width=6,height=2, command=lambda: reception(7))         
btn7.grid(column = 0, row = 5) 

btn2 = tk.Button(master, text="2",width=6,height=2, command=lambda: reception(2))         
btn2.grid(column = 1, row = 5) 

btn9 = tk.Button(master, text="9", width=6,height=2, command=lambda: reception(9))         
btn9.grid(column = 2, row = 5)

multiplication = tk.Button(master, text="*", width=6,height=2, command=lambda: reception("*"))
multiplication.grid(column = 3, row = 5) 

egalite = tk.Button(master, text="=", width=6,height=2, command=egal)
egalite.grid(row=6, column=1)

btnclear = tk.Button(master, text="Clear", width=6,height=2, command=clear)
btnclear.grid(row=6, column=2)

racine = tk.Button(master, text="√", command=lambda: reception('**0.5'),width=6,height=2)
racine.grid(column=4 , row=3)

btncube = tk.Button(master, text="²", command=lambda : reception('**2'),height=2,width=6)
btncube.grid(column=4 , row=4)

division = tk.Button(master, text="/", width=6,height=2, command=lambda: reception("/"))
division.grid(row=4, column=3)

master.mainloop()