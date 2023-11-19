import tkinter as tk
class SendingParcels:
    def __init__(self, queue):
        self.queue = queue
        self.window = tk.Tk( )
        self.gui()


    def gui(self):
        self.window.title("Select Parcel Priority")
        self.window.config(background="blue")
        self.window.geometry("300x150")
        btn_oldest = tk.Button(self.window, text="Oldest Parcel",
                               font=("Arial", 14),background="purple", command=self.choose_oldest)
        btn_oldest.pack(pady=10)
        btn_nearest = tk.Button(self.window, text="Nearest Destination",
                                font=("Arial", 14),background="purple", command=self.choose_nearest)
        btn_nearest.pack(pady=10)

        self.window.mainloop( )


    def choose_oldest(self):
        print(f"name: {self.queue.first.name} "
                          f"sender: {self.queue.first.sender} "
                          f"recipient: {self.queue.first.recipient} "
                          f"distance: {self.queue.first.distance} "
                          f"tracking code: {self.queue.first.tracking_code} "
                          f"status: {self.queue.first.status_stack.peek()} ")
        agree = input("Do you want to send it?y/n\n")
        if agree == "y":
            self.queue.first.status_stack.push("sent")
        print("Done:)")
        self.window.destroy()


    def choose_nearest(self):
        self.search()
        self.window.destroy()
    def search(self):
        from PriorityQueue import PriorityQueue
        priority_queue = PriorityQueue(100)
        for i in range(self.queue.size):
            priority_queue.enqueue(self.queue.get_by_index(i).tracking_code,self.queue.get_by_index(i).distance)
            i+=1
        node_track = priority_queue.get_lowest_priority( ).val
        node=self.queue.find_node(node_track)
        print(f"name: {node.name} "
              f"sender: {node.sender} "
              f"recipient: {node.recipient} "
              f"distance: {node.distance} "
              f"tracking code: {node.tracking_code} "
              f"status: {node.status_stack.peek( )} ")
        self.queue.display_specific_queue(priority_queue.get_lowest_priority( ).val)
        agree = input("Do you want to send it?y/n")
        if agree == "y":
            self.queue.set(priority_queue.get_lowest_priority( ).val,"sent")
        self.queue.display_specific_queue(priority_queue.get_lowest_priority( ).val)
        print("Done:)")


