import tkinter as tk
from tkinter import ttk

import os
# This forces the app to recognize high-res displays
os.environ['TK_SILENT_DEPRECATION'] = '1' 

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Optilime")
        self.geometry("640x380")

        # Layout container
        self.main_frame = ttk.Frame(self, padding="20")
        self.main_frame.pack(expand=True)

        # label
        self.label = ttk.Label(self.main_frame, text="🍋‍🟩 Optilime 📸", font=("Departure Mono", 24, "bold"))
        self.label.pack(pady=5)

        # button
        self.button = ttk.Button(self.main_frame, text="Click Me", command= self.update_text)
        self.button.pack(pady=5)
        
        self.button2 = ttk.Button(self.main_frame, text="About", command=self.update_about)
        self.button2.pack(pady=5)
        print('tk version:',tk.TkVersion)

    def update_text(self):
        self.label.configure(text="You clicked the button!")
    
    def update_about(self):
        self.label.configure(text="This is a photo conversion app")

if __name__ == "__main__":
    app = GUI()
    app.mainloop()