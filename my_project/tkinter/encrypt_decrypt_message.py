from tkinter import *
from tkinter import messagebox
import base64
import os
# Create the main window
def decrypt():
    password = code.get()
    if password == "2602":
        screen2 = Toplevel(screen)
        screen2.title("Decrypted Message")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decoded_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decoded_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="Decrypted Message", font="arial", fg="white", bg="#00bd56")
        text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("Encrypt Message", "Input Secret Key")
    elif password != "2602":
        messagebox.showerror("Encrypt Message", "Invalid Secret Key")

def encrypt():
    password = code.get()
    if password == "2602":
        screen1 = Toplevel(screen)
        screen1.title("Encrypted Message")
        screen1.geometry("400x200")
        screen1.configure(bg="#e53833")

        message = text1.get(1.0, END)
        encoded_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encoded_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="Encrypted Message", font="arial", fg="white", bg="#e53833")
        text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)
    elif password == "":
        messagebox.showerror("Encrypt Message", "Input Secret Key")
    elif password != "2602":
        messagebox.showerror("Encrypt Message", "Invalid Secret Key")


def main_screen():

    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    
    #Icon
    image_icon = PhotoImage(file = "key.png")
    screen.iconphoto(False, image_icon)
    screen.title("Encrypt & Decrypt Message")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(screen, text="Enter text for encryption/decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 12", bg="white",relief=GROOVE, wrap=WORD)
    text1.place(x=10, y=40, width=355,height=100)

    Label(screen, text="Enter secret key for encryption/decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(screen, text="ENCRYPT", height="2", width="23", bg="#e53833", fg="white", bd="0", command=encrypt).place(x=10, y=250)
    Button(screen, text="DECRYPT", height="2", width="23", bg="#00bd56", fg="white", bd="0", command=decrypt).place(x=200, y=250)
    Button(screen, text="RESET", height="2", width="50", bg="#1089ff", fg="white", bd="0", command=reset).place(x=10, y=300)


    screen.mainloop()
main_screen()