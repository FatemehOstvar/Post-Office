import tkinter as tk

from Parcel import Parcel
from ReceiveParcel import ReceiveParcel
from TrackParcel import TrackParcel
from SendingParcels import SendingParcels
from SetStatus import SetStatus

class MainMenu :

    def __init__(self) :
        self.queue = Parcel()
        self.window = tk.Tk()
        self.menu_frame = tk.Frame(self.window)
        self.gui()


    def gui(self):
        self.menu_frame.pack(side="top", fill="both", expand=True)
        self.menu_frame.config(bg="blue")
        self.create_buttons()
    def receive_posts(self) :
        ReceiveParcel(self.queue)
    def post(self) :
        SendingParcels(self.queue)

    def set_status(self) :
        SetStatus(self.queue)

    def track_status(self) :
        TrackParcel(self.queue)
    def create_buttons(self) :
        button1 = tk.Button(self.menu_frame,bg="purple", text="Receiving Posts",command=self.receive_posts,font=("Arial", 16))
        button2 = tk.Button(self.menu_frame,bg="purple", text="Posting",command=self.post,font=("Arial", 16))
        button3 = tk.Button(self.menu_frame,bg="purple", text="Set Status",command=self.set_status,font=("Arial", 16))
        button4 = tk.Button(self.menu_frame,bg="purple", text="Tracking Status",command=self.track_status,font=("Arial", 16))

        button1.pack(side="top", fill="x", padx=20, pady=10)
        button2.pack(side="top", fill="x", padx=20, pady=10)
        button3.pack(side="top", fill="x", padx=20, pady=10)
        button4.pack(side="top", fill="x", padx=20, pady=10)

        self.window.geometry("800x600+400+100")
        self.window.mainloop( )




MainMenu( )
