import tkinter as tk
class TrackParcel:

    def __init__(self, queue):
        self.queue = queue
        self.entry = None
        self.a = tk.Tk()
        self.gui()

    def search(self):
        tracking_code = self.entry.get( )
        print(self.queue.find_and_access_stack(tracking_code).get_stack())
        self.queue.display_specific_queue(tracking_code)
        self.a.destroy()


    def gui(self):
        self.a.geometry("300x200")
        self.a.config(background="blue")
        label = tk.Label(self.a,background="purple",text="Track Parcel",font=("Arial", 16))
        self.entry = tk.Entry(self.a,background="lightskyblue",font=("Arial", 16) )
        button = tk.Button(self.a,text="Search",font=("Arial", 16),background="green", command=self.search)
        label.pack( )
        self.entry.pack( )
        button.pack( )
        self.a.mainloop()

