from PIL import Image,ImageTk
import tkinter as tk
import os
from tkinter import ttk,messagebox

class c2w_TkinterLibraryApp:
    def __init__(self):
        self.c2w_root=tk.Tk()
        self.c2w_screen_width=self.c2w_root.winfo_screenwidth()
        self.c2w_screen_height=self.c2w_root.winfo_screenheight()
        self.c2w_root.title("tkinter Library")
        self.c2w_root.geometry(f"{self.c2w_screen_width}x{self.c2w_screen_height}")
        self.c2w_root.configure(bg="#192f44")

        #set up the ui component
        self.setup_ui()
    def setup_ui(self):
        #create the main background frame
        self.c2w_background_frame = tk.Frame(self.c2w_root)

