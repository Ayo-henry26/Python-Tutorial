from tkinter import *

#Create the main window
root = Tk()
root.title("Calculator")
root.geometry("400x400")

#Create display entry widget
display = Entry(root, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
display.pack(fill=BOTH, ipadx=8, ipady=15, padx=10, pady=10)

#Functions that handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(display.get())
            display.delete(0, END)
            display.insert(0, result)
        except:
            display.delete(0, END)
            display.insert(0, "Error")
    elif text == "C":
        display.delete(0, END)
    else:
        display.insert(END, text)

#Button Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

#Color Mapping 
colors = {
    "C" : "#ff4d4d",
    "+" : "#ffa500",
    "-" : "#ffa500",
    "*" : "#ffa500",
    "/" : "#ffa500"
}

#Create and place buttons
for row in buttons:
    frame = Frame(root)
    frame.pack(expand=True)
    for btn in row:
        bg_color = colors.get(btn, "#f0f0f0")
        b = Button(frame, text=btn, font=("Arial", 18), width=5, height=2, bg=bg_color)
        b.pack(side=LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)

#Run the program
root.mainloop()