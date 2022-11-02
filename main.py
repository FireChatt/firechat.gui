from tkinter import *
from requests import get, post

tk = Tk("Firechat")
tk.geometry("700x300")

text_variable = StringVar()

mainurl = "https://firechat-prototype.herokuapp.com"

class Sendinput(Frame):
    def __init__(self, master) -> None:
        super().__init__(master, width=700, height=30, bg="grey")

def get_all_messages():
    all_messages = get(f"{mainurl}/messages").json()
    
    for i in all_messages:
        content = i['content']
        Label(tk, text=content).pack()

def on_enter(*args, **kwargs):
    for i in tk.winfo_children():
        if text_variable.get():
            post(f"{mainurl}/messages", json={"content": text_variable.get()})
            text_variable.set("")
        else:
            pass

e = Entry(tk, textvariable=text_variable, width=700)
e.pack(side="bottom")
e.bind("<Return>", on_enter)

while True:
    get_all_messages()
    
    tk.update()
    
    from time import sleep
    sleep(1)
    
    for i in tk.winfo_children():
        if not isinstance(i, Entry):
            i.destroy()
