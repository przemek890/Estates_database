import tkinter as tk

"""Okno tkintera"""
class Window:
    def __init__(self):
        # Ustawienia okna
        self.root = tk.Tk()
        self.root.title("Sprzedaz nieruchomosci - Przemysław Janiszewski")
        quarter_screen_width = 1000
        quarter_screen_height = 500
        self.root.geometry(
            f"{quarter_screen_width}x{quarter_screen_height}+{quarter_screen_width}+{quarter_screen_height}")