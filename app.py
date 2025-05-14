import time
from plyer import notification
from tkinter import *
import tkinter as tk

root = tk.Tk()

root.title("Notification App")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="lightblue")

minutes = Spinbox(root, from_=1, to=100, width=30, font=("Arial", 20))
minutes.place(x=300,y=100,anchor=CENTER)

minutes_label = Label(root, text="Minutes", font=("Arial", 20), bg="lightblue")
minutes_label.place(relx=0.5, rely=0.3, anchor=CENTER)

reason = Entry(root, width=31, font=("Arial", 20))
reason.place(x=300,y=200,anchor=CENTER)
reason_label = Label(root, text="Reason", font=("Arial", 20), bg="lightblue")
reason_label.place(relx=0.5, rely=0.5, anchor=CENTER)

submit = Button(root, text="Submit", font=("Arial", 20), bg="lightgreen", command=lambda: notify())
submit.place(relx=0.5, rely=0.7, anchor=CENTER)

def notify():
    time.sleep(int(minutes.get()) * 60)
    notification.notify(
        title="Reminder",
        message=reason.get(),
        app_icon=None,
        timeout=10,
    )

root.mainloop()


