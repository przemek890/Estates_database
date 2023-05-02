from tkinter import ttk, LEFT
import tkinter as tk

"""Moduł dodawania rekordow"""
class Dodaj_rekord:
    def __init__(self,root,cursor,notebook):
        self.root = root
        self.cursor = cursor
        self.tree = None
        self.notebook = notebook
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Dodaj rekord")
        self.notebook.pack()

        # Menu:
        self.tab2_subframe = ttk.Frame(self.tab2)
        self.tab2_subnotebook = ttk.Notebook(self.tab2_subframe)
        self.tab2_subtab1 = ttk.Frame(self.tab2_subnotebook)
        self.tab2_subtab2 = ttk.Frame(self.tab2_subnotebook)
        self.tab2_subtab3 = ttk.Frame(self.tab2_subnotebook)
        self.tab2_subtab4 = ttk.Frame(self.tab2_subnotebook)
        self.tab2_subtab5 = ttk.Frame(self.tab2_subnotebook)
        self.tab2_subtab6 = ttk.Frame(self.tab2_subnotebook)
        self.tab2_subtab7 = ttk.Frame(self.tab2_subnotebook)

        self.tab2_subnotebook.add(self.tab2_subtab1, text="Klienci")
        self.tab2_subnotebook.add(self.tab2_subtab2, text="Nieruchomosci")
        self.tab2_subnotebook.add(self.tab2_subtab3, text="Oferty")
        self.tab2_subnotebook.add(self.tab2_subtab4, text="Posrednicy")
        self.tab2_subnotebook.add(self.tab2_subtab5, text="Transakcje")
        self.tab2_subnotebook.add(self.tab2_subtab6, text="Typy_nieruchomosci")
        self.tab2_subnotebook.add(self.tab2_subtab7, text="Umowy")
        self.tab2_subnotebook.pack()

        # Submenu:
        self.tab2_submenu_var = tk.StringVar()
        self.tab2_submenu = ttk.OptionMenu(self.tab2, self.tab2_submenu_var, "Tabele", "Klienci",
                                           "Nieruchomosci", "Oferty", "Posrednicy", "Transakcje", "Typy nieruchomosci",
                                           "Umowy", command=self.Add_subtab)
        self.tab2_submenu.pack(side=LEFT,padx=10)

    def Add_subtab(self):
        pass