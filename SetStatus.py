import tkinter as tk


class SetStatus:

    def __init__(self, queue):
        self.queue = queue
        self.a = tk.Tk( )
        self.tracking_entry = tk.Entry(self.a,font=("Arial", 16), background="lightskyblue")
        self.status_entry = tk.Entry(self.a,font=("Arial", 16), background="lightskyblue")
        self.gui( )


    def set_status(self):
        tracking_code = self.tracking_entry.get( )
        new_status = self.status_entry.get( )
        self.queue.set(tracking_code,new_status)
        self.queue.display_specific_queue(tracking_code)
        self.a.destroy( )

    def gui(self):
        self.a.title("Set Parcel Status")
        self.a.config(background="blue",pady=50,padx=50)
        tk.Label(self.a,font=("Arial", 16),background="purple",padx=20, text="Tracking Code").grid(row=0)
        tk.Label(self.a,font=("Arial", 16),background="purple", text="New Status").grid(row=1)

        self.tracking_entry.grid(row=0, column=1)
        self.status_entry.grid(row=1, column=1)

        tk.Button(self.a,font=("Arial", 16),background="green", text="Submit",padx=12,
                  command=self.set_status).grid(row=3)

        self.a.mainloop( )
