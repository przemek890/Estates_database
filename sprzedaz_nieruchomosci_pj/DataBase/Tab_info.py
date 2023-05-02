import tkinter as tk
from tkinter import ttk, LEFT

"""Zakładka_1 - informacje o tabelach"""
class Informacje_o_tabelach:
    def __init__(self,root,cursor,notebook):
        self.root = root
        self.cursor = cursor
        self.tree = None
        self.notebook = notebook
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Informacje o tabelach")
        self.notebook.pack()

        # Menu:
        self.tab1_subframe = ttk.Frame(self.tab1)
        self.tab1_subnotebook = ttk.Notebook(self.tab1_subframe)
        self.tab1_subtab1 = ttk.Frame(self.tab1_subnotebook)
        self.tab1_subtab2 = ttk.Frame(self.tab1_subnotebook)
        self.tab1_subtab3 = ttk.Frame(self.tab1_subnotebook)
        self.tab1_subtab4 = ttk.Frame(self.tab1_subnotebook)
        self.tab1_subtab5 = ttk.Frame(self.tab1_subnotebook)
        self.tab1_subtab6 = ttk.Frame(self.tab1_subnotebook)
        self.tab1_subtab7 = ttk.Frame(self.tab1_subnotebook)

        self.tab1_subnotebook.add(self.tab1_subtab1, text="Klienci")
        self.tab1_subnotebook.add(self.tab1_subtab2, text="Nieruchomosci")
        self.tab1_subnotebook.add(self.tab1_subtab3, text="Oferty")
        self.tab1_subnotebook.add(self.tab1_subtab4, text="Posrednicy")
        self.tab1_subnotebook.add(self.tab1_subtab5, text="Transakcje")
        self.tab1_subnotebook.add(self.tab1_subtab6, text="Typy_nieruchomosci")
        self.tab1_subnotebook.add(self.tab1_subtab7, text="Umowy")
        self.tab1_subnotebook.pack()

        # Submenu:
        self.tab1_submenu_var = tk.StringVar()
        self.tab1_submenu = ttk.OptionMenu(self.tab1, self.tab1_submenu_var, "Tabele", "Klienci",
                                           "Nieruchomosci", "Oferty", "Posrednicy", "Transakcje", "Typy nieruchomosci",
                                           "Umowy", command=self.Show_subtab)
        self.tab1_submenu.pack(side=LEFT,padx=10)
    def Show_Klienci(self):
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(expand=True, fill=tk.BOTH)

        # Tabela::Klienci
        self.tree = ttk.Treeview(self.tab1)
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree["columns"] = ("1", "2", "3", "4", "5","6")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("1", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("2", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("3", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("4", width=250, minwidth=250, stretch=False,anchor=tk.CENTER)
        self.tree.column("5", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("6", width=200, minwidth=200, stretch=False,anchor=tk.CENTER)
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        self.tree.heading("1", text="ID Klienta", anchor=tk.CENTER)
        self.tree.heading("2", text="Imie", anchor=tk.CENTER)
        self.tree.heading("3", text="Nazwisko", anchor=tk.CENTER)
        self.tree.heading("4", text="Adres Zameldowania", anchor=tk.CENTER)
        self.tree.heading("5", text="Numer telefonu", anchor=tk.CENTER)
        self.tree.heading("6", text="Adres Email", anchor=tk.CENTER)

        self.cursor.execute("SELECT * FROM Klienci")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, text="", values=row,)
    def Show_Nieruchomosci(self):
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(expand=True, fill=tk.BOTH)

        # Tabela::Nieruchomosci
        self.tree = ttk.Treeview(self.tab1)
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree["columns"] = ("1", "2", "3", "4", "5","6","7")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("1", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("2", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("3", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("4", width=150, minwidth=150, stretch=False,anchor=tk.CENTER)
        self.tree.column("5", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("6", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("7", width=150, minwidth=150, stretch=False,anchor=tk.CENTER)
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        self.tree.heading("1", text="ID Nieruchomosci", anchor=tk.CENTER)
        self.tree.heading("2", text="Kraj", anchor=tk.CENTER)
        self.tree.heading("3", text="Miejscowosc", anchor=tk.CENTER)
        self.tree.heading("4", text="Ulica", anchor=tk.CENTER)
        self.tree.heading("5", text="Powierzchnia", anchor=tk.CENTER)
        self.tree.heading("6", text="Liczba pokoi", anchor=tk.CENTER)
        self.tree.heading("7", text="ID Typu nieruchomosci", anchor=tk.CENTER)

        self.cursor.execute("SELECT * FROM Nieruchomosci")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, text="", values=row)
    def Show_Oferty(self):
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(expand=True, fill=tk.BOTH)

        # Tabela::Nieruchomosci
        self.tree = ttk.Treeview(self.tab1)
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree["columns"] = ("1", "2", "3", "4", "5")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("1", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("2", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("3", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("4", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("5", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        self.tree.heading("1", text="ID Oferty", anchor=tk.CENTER)
        self.tree.heading("2", text="ID Nieruchomosci", anchor=tk.CENTER)
        self.tree.heading("3", text="ID Posrednika", anchor=tk.CENTER)
        self.tree.heading("4", text="Data dodania", anchor=tk.CENTER)
        self.tree.heading("5", text="Cena oferty", anchor=tk.CENTER)

        self.cursor.execute("SELECT * FROM Oferty")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, text="", values=row)
    def Show_Posrednicy(self):
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(expand=True, fill=tk.BOTH)

        # Tabela::Nieruchomosci
        self.tree = ttk.Treeview(self.tab1)
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree["columns"] = ("1", "2", "3", "4", "5")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("1", width=100, minwidth=100, stretch=False, anchor=tk.CENTER)
        self.tree.column("2", width=100, minwidth=100, stretch=False, anchor=tk.CENTER)
        self.tree.column("3", width=100, minwidth=100, stretch=False, anchor=tk.CENTER)
        self.tree.column("4", width=100, minwidth=100, stretch=False, anchor=tk.CENTER)
        self.tree.column("5", width=200, minwidth=200, stretch=False, anchor=tk.CENTER)
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        self.tree.heading("1", text="ID Posrednika", anchor=tk.CENTER)
        self.tree.heading("2", text="Imie", anchor=tk.CENTER)
        self.tree.heading("3", text="Nazwisko", anchor=tk.CENTER)
        self.tree.heading("4", text="Numer telefonu", anchor=tk.CENTER)
        self.tree.heading("5", text="Adres email", anchor=tk.CENTER)

        self.cursor.execute("SELECT * FROM Posrednicy")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, text="", values=row)
    def Show_Transakcje(self):
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(expand=True, fill=tk.BOTH)

        # Tabela::Nieruchomosci
        self.tree = ttk.Treeview(self.tab1)
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree["columns"] = ("1", "2", "3", "4")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("1", width=100, minwidth=100, stretch=False, anchor=tk.CENTER)
        self.tree.column("2", width=100, minwidth=100, stretch=False, anchor=tk.CENTER)
        self.tree.column("3", width=100, minwidth=100, stretch=False, anchor=tk.CENTER)
        self.tree.column("4", width=100, minwidth=100, stretch=False, anchor=tk.CENTER)
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        self.tree.heading("1", text="ID Transakcji", anchor=tk.CENTER)
        self.tree.heading("2", text="ID Umowy", anchor=tk.CENTER)
        self.tree.heading("3", text="ID Posrednika", anchor=tk.CENTER)
        self.tree.heading("4", text="Kwota Transakcji", anchor=tk.CENTER)

        self.cursor.execute("SELECT * FROM Transakcje")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, text="", values=row)
    def Show_Typ_nieruchomosci(self):
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(expand=True, fill=tk.BOTH)

        # Tabela::Nieruchomosci
        self.tree = ttk.Treeview(self.tab1)
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree["columns"] = ("1", "2", "3")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("1", width=200, minwidth=200, stretch=False, anchor=tk.CENTER)
        self.tree.column("2", width=150, minwidth=150, stretch=False, anchor=tk.CENTER)
        self.tree.column("3", width=300, minwidth=300, stretch=False, anchor=tk.CENTER)
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        self.tree.heading("1", text="ID Typu nieruchomosci", anchor=tk.CENTER)
        self.tree.heading("2", text="Nazwa", anchor=tk.CENTER)
        self.tree.heading("3", text="Opis", anchor=tk.CENTER)

        self.cursor.execute("SELECT * FROM Typy_nieruchomosci")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, text="", values=row)
    def Show_Umowy(self):
        self.table_frame = ttk.Frame(self.root)
        self.table_frame.pack(expand=True, fill=tk.BOTH)

        # Tabela::Nieruchomosci
        self.tree = ttk.Treeview(self.tab1)
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree["columns"] = ("1", "2", "3", "4", "5")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("1", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("2", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("3", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("4", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.column("5", width=100, minwidth=100, stretch=False,anchor=tk.CENTER)
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        self.tree.heading("1", text="ID Umowy", anchor=tk.CENTER)
        self.tree.heading("2", text="Data zawarcia", anchor=tk.CENTER)
        self.tree.heading("3", text="Data podpisania", anchor=tk.CENTER)
        self.tree.heading("4", text="ID Nieruchomosci", anchor=tk.CENTER)
        self.tree.heading("5", text="ID Klienta", anchor=tk.CENTER)

        self.cursor.execute("SELECT * FROM Umowy")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, text="", values=row)
    def Show_subtab(self, option):
        if option == "Klienci":
            if self.tree is not None:
                self.tree.destroy()
            self.tab1_subnotebook.select(self.tab1_subtab1)
            self.Show_Klienci()
        elif option == "Nieruchomosci":
            if self.tree is not None:
                self.tree.destroy()
            self.tab1_subnotebook.select(self.tab1_subtab2)
            self.Show_Nieruchomosci()
        elif option == "Oferty":
            if self.tree is not None:
                self.tree.destroy()
            self.tab1_subnotebook.select(self.tab1_subtab3)
            self.Show_Oferty()
        elif option == "Posrednicy":
            if self.tree is not None:
                self.tree.destroy()
            self.tab1_subnotebook.select(self.tab1_subtab4)
            self.Show_Posrednicy()
        elif option == "Transakcje":
            if self.tree is not None:
                self.tree.destroy()
            self.tab1_subnotebook.select(self.tab1_subtab5)
            self.Show_Transakcje()
        elif option == "Typy nieruchomosci":
            if self.tree is not None:
                self.tree.destroy()
            self.tab1_subnotebook.select(self.tab1_subtab5)
            self.Show_Typ_nieruchomosci()
        elif option == "Umowy":
            if self.tree is not None:
                self.tree.destroy()
            self.tab1_subnotebook.select(self.tab1_subtab5)
            self.Show_Umowy()