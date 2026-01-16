from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title("Sign Up")
window.geometry("925x500+300+200")
window.configure(bg="#fff")
window.resizable(False, False)


def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            file = open("datasheet.txt", "r+")
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username : password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open("datasheet.txt", "w")
            w = file.write(str(r))

            messagebox.showinfo("Signup", "Successfully sign up")

        except:
            file = open("datasheet.txt", "w")
            pp = str({username : password})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror("Invalid", "Both password should match")

def sign():
    window.destroy()



img = PhotoImage(file="signup_group.png")
Label(window, image=img, bd=0, bg="white").place(x=1, y=65)

frame = Frame(window, width=350, height=390, bg="#fff")
frame.place(x=490, y=50)

heading = Label(frame, text="Sign Up", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
heading.place(x=120, y= 20)

#########--------------------------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    if user.get() == '':
        user.insert(0, "Username")

user = Entry(frame, width=25, fg="black", bd=0, bg="white", font=("Microsoft Yahei UI Light", 11))
user.place(x=50, y=90)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=115)

#########--------------------------------------------------------------------------------------------------
def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    if code.get() == '':
        code.insert(0, "Password")

code = Entry(frame, width=25, fg="black", bd=0, bg="white", font=("Microsoft Yahei UI Light", 11))
code.place(x=50, y=170)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=195)

#########--------------------------------------------------------------------------------------------------
def on_enter(e):
    confirm_code.delete(0, "end")

def on_leave(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, "Confirm Password")

confirm_code = Entry(frame, width=25, fg="black", bd=0, bg="white", font=("Microsoft Yahei UI Light", 11))
confirm_code.place(x=50, y=250)
confirm_code.insert(0, "Confirm Password")
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=275)

#-----------------------------------------------------------------------
Button(frame, width=39, pady=7,text="Sign Up", bg="#57a1f8", fg="white", bd=0, command=signup).place(x=33, y=310)
label = Label(frame, text="I have an account", fg="black", bg="white", font=("Microsoft Yahei UI Light", 9))
label.place(x=85, y=370)

signin = Button(frame, width=6, text="Sign in", bd=0, bg="white", cursor="hand2", fg="#57a1f8", command=sign)
signin.place(x=200, y=370)


window.mainloop()