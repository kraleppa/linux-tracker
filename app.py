import tkinter as tk
from logic import *

repository = ProcessRepository()
active_process = ActiveProcess()


class ProcessRefresher:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="gray")
        self.frame.place(relwidth=1, relheight=1)
        self.frame.after(1000, self.refresh_process)

    def refresh_process(self):
        repository.add_process(active_process.update_process())
        for widget in self.frame.winfo_children():
            widget.destroy()

        for key in repository.process_map:
            process = tk.Label(self.frame, text=f"{key}: {str(repository.process_map[key])}")
            process.pack()

        self.frame.after(500, self.refresh_process)


if __name__ == "__main__":
    root = tk.Tk()
    timer = ProcessRefresher(root)
    root.mainloop()
