import tkinter as tk

"""Okno tkintera"""
class Window:
    def __init__(self):
        # Ustawienia okna
        self.root = tk.Tk()
        self.root.title("Sprzedaz nieruchomosci - Przemysław Janiszewski")
        quarter_screen_width = 1000
        quarter_screen_height = 800

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        self.root.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        self.root.resizable(False, False)


