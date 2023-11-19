# from Stack import *
from tkinter import *
import random

def generate_tracking_code():
   return random.randint(100000, 999999)


class ReceiveParcel:
    def __init__(self,queue):
        self.received = queue
        self.gui()

    def gui(self):
        a = Tk()
        a.title("Parcels Received")
        a.config(background="blue")
        screen_width = a.winfo_screenwidth( )
        screen_height = a.winfo_screenheight( )

        form_width = 300
        form_height = 280

        a.geometry(
            f"{form_width}x{form_height}+{screen_width // 2 - form_width // 2}+"
            f"{screen_height // 2 - form_height // 2}")


        name_label = Label(a, text="Name:",bg="purple")
        name_label.pack( )

        name_entry = Entry(a,background="lightskyblue")
        name_entry.pack( )

        sender_label = Label(a, text="Sender:",bg="purple")
        sender_label.pack( )

        sender_entry = Entry(a,background="lightskyblue")
        sender_entry.pack( )

        receiver_label = Label(a, text="Receiver:",bg="purple")
        receiver_label.pack( )

        receiver_entry = Entry(a,background="lightskyblue")
        receiver_entry.pack( )



        distance_label = Label(a, text="Distance:",bg="purple")
        distance_label.pack( )

        distance_entry = Entry(a,background="lightskyblue")
        distance_entry.pack( )

        submit_btn = Button(a,background="green", text="Submit",
                            command=lambda: self.add(name_entry,sender_entry,receiver_entry,distance_entry))
        submit_btn.pack( )

        for widget in [name_label, name_entry, sender_label, sender_entry,
                       receiver_label, receiver_entry, submit_btn, distance_label, distance_entry]:
            widget.config(font=("Arial", 14), width=20)


        a.mainloop()



    def add(self,name,sender,recipient,distance):
        tracking_code = generate_tracking_code()
        self.received.enqueue(name=name.get(),sender=sender.get(),recipient=recipient.get(),distance = distance.get()
                              ,tracking_code= tracking_code)
        self.received.set(tracking_code,"received")
        print("Submitted")

        self.received.display_queue()

    def get_queue(self):
        return self.received
