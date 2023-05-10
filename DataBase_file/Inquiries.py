import tkinter as tk
from tkinter import ttk, LEFT
import tkinter.messagebox as messagebox

"""Zakładka wybrane zapytania"""
class Inquiries:
    def __init__(self,root,cursor,notebook,conn):
        self.root = root
        self.cursor = cursor
        self.conn = conn
        self.tree = None
        self.notebook = notebook
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab4, text="Wybrane zapytania")
        self.notebook.pack()
        self.tab4_subframe = None
        self.tab4_subnotebook = None
        self.tab4_submenu = None
        self.D1 = ""
        self.D2 = ""
    def menu(self):
        # Menu:
        if self.tab4_subframe is None and self.tab4_subnotebook is None:

            self.tab4_subframe = ttk.Frame(self.tab4)
            self.tab4_subnotebook = ttk.Notebook(self.tab4_subframe)

            self.tab4_subtab1 = ttk.Frame(self.tab4_subnotebook)
            self.tab4_subtab2 = ttk.Frame(self.tab4_subnotebook)
            self.tab4_subtab3 = ttk.Frame(self.tab4_subnotebook)
            self.tab4_subtab4 = ttk.Frame(self.tab4_subnotebook)
            self.tab4_subtab5 = ttk.Frame(self.tab4_subnotebook)

            self.tab4_subnotebook.add(self.tab4_subtab1, text="Umowy zawarte w danym zakresie lat")
            self.tab4_subnotebook.add(self.tab4_subtab2, text="Łaczny koszt zakupu dla każdego klienta")
            self.tab4_subnotebook.add(self.tab4_subtab3, text="Transakcje danego pośrednika")
            self.tab4_subnotebook.add(self.tab4_subtab4, text="Klienci o nazwisku na daną literę")
            self.tab4_subnotebook.add(self.tab4_subtab5, text="Nieruchomosci o powierzchni większej od zadanej")

            self.tab4_subnotebook.pack()

            # Submenu:
            self.tab4_submenu_var = tk.StringVar()
            self.tab4_submenu = ttk.OptionMenu(self.tab4, self.tab4_submenu_var, "Tabele",
                                               "Umowy zawarte w danym zakresie lat",
                                               "Łaczny koszt zakupu dla każdego klienta",
                                               "Transakcje danego pośrednika",
                                               "Klienci o nazwisku na daną literę",
                                               "Nieruchomosci o powierzchni większej od zadanej",
                                               command=self.zapytania_subtab)

            self.tab4_submenu.configure(width=14)
            self.tab4_submenu.pack(side=LEFT, padx=10, pady=350)

    def kwerenda_1(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Podaj daty")
        quarter_screen_width = 400
        quarter_screen_height = 175

        popup_window.transient(self.root)
        popup_window.overrideredirect(True)

        popup_window.grab_set()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        tk.Label(frame, text="PODAJ DATY").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        tk.Label(frame, text="DATA POCZATKOWA:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.D1_entry = tk.Entry(frame)
        self.D1_entry.grid(row=1, column=1, padx=5, pady=5,sticky="w")

        tk.Label(frame, text="DATA KONCOWA:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.D2_entry = tk.Entry(frame)
        self.D2_entry.grid(row=2, column=1, padx=5, pady=5,sticky="w")

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


        def kw_1():
            self.tree = ttk.Treeview(self.tab4)
            self.tree.pack(expand=True, fill=tk.BOTH)
            self.tree["columns"] = ("1", "2", "3", "4")
            self.tree.column("#0", width=0, stretch=False)
            self.tree.column("1", width=150, minwidth=150, stretch=True, anchor=tk.CENTER)
            self.tree.column("2", width=150, minwidth=150, stretch=True, anchor=tk.CENTER)
            self.tree.column("3", width=250, minwidth=250, stretch=True, anchor=tk.CENTER)
            self.tree.column("4", width=160, minwidth=160, stretch=True, anchor=tk.CENTER)
            self.tree.heading("#0", text="", anchor=tk.CENTER)
            self.tree.heading("1", text="Imie i nazwisko", anchor=tk.CENTER)
            self.tree.heading("2", text="Data zawarcia", anchor=tk.CENTER)
            self.tree.heading("3", text="Opis", anchor=tk.CENTER)
            self.tree.heading("4", text="", anchor=tk.CENTER)

            with open('DataBase_sql/inquiries/zapytanie_1.sql', 'r') as file:
                query = file.read()
                query.format(self.D1,self.D2)

            formatted_query = query.format(self.D1, self.D2)

            self.cursor.execute(formatted_query)
            print(formatted_query)
            rows = self.cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, text="", values=row, )

        def get_values():
            try:
                self.D1 = self.D1_entry.get()
                self.D2 = self.D2_entry.get()

                messagebox.showinfo("Sukces", f"Poprawnie podano dane!\n")

                self.D1_entry.delete(0, tk.END)
                self.D2_entry.delete(0, tk.END)
                popup_window.destroy()

                kw_1()


            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne podano dane!\n")
                print(e)
                popup_window.destroy()
                self.D1_entry.delete(0, tk.END)
                self.D2_entry.delete(0, tk.END)

        def delete():
            self.D1_entry.delete(0, tk.END)
            self.D2_entry.delete(0, tk.END)


        tk.Button(button_frame, text="Zatwierdz", command=get_values, width=15).grid(row=7, column=0, padx=5,pady=5, sticky='w')
        tk.Button(button_frame, text="Reset", command=delete, width=15).grid(row=7, column=1, padx=5,pady=5, sticky='e')
    def kwerenda_2(self):
        def kw_1():
            self.tree = ttk.Treeview(self.tab4)
            self.tree.pack(expand=True, fill=tk.BOTH)
            self.tree["columns"] = ("1", "2", "3")
            self.tree.column("#0", width=0, stretch=False)
            self.tree.column("1", width=200, minwidth=200, stretch=True, anchor=tk.CENTER)
            self.tree.column("2", width=160, minwidth=160, stretch=True, anchor=tk.CENTER)
            self.tree.column("3", width=400, minwidth=400, stretch=True, anchor=tk.CENTER)
            self.tree.heading("#0", text="", anchor=tk.CENTER)
            self.tree.heading("1", text="Imie i nazwisko", anchor=tk.CENTER)
            self.tree.heading("2", text="Łączna cena nieruchomości", anchor=tk.CENTER)
            self.tree.heading("3", text="", anchor=tk.CENTER)

            with open('DataBase_sql/inquiries/zapytanie_2.sql', 'r') as file:
                query = file.read()
                query.format(self.D1,self.D2)

            self.cursor.execute(query)
            print(query)
            rows = self.cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, text="", values=row, )
        kw_1()
    def kwerenda_3(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Podaj Imie i nazwisko pośrednika")
        quarter_screen_width = 400
        quarter_screen_height = 175

        popup_window.transient(self.root)
        popup_window.overrideredirect(True)

        popup_window.grab_set()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        tk.Label(frame, text="PODAJ IMIE I NAZWISKO POSREDNIKA").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        tk.Label(frame, text="IMIE:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.D1_entry = tk.Entry(frame)
        self.D1_entry.grid(row=1, column=1, padx=5, pady=5,sticky="w")

        tk.Label(frame, text="NAZWISKO:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.D2_entry = tk.Entry(frame)
        self.D2_entry.grid(row=2, column=1, padx=5, pady=5,sticky="w")

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


        def kw_3():
            self.tree = ttk.Treeview(self.tab4)
            self.tree.pack(expand=True, fill=tk.BOTH)
            self.tree["columns"] = ("1", "2", "3","4","5")
            self.tree.column("#0", width=0, stretch=False)
            self.tree.column("1", width=150, minwidth=150, stretch=True, anchor=tk.CENTER)
            self.tree.column("2", width=250, minwidth=250, stretch=True, anchor=tk.CENTER)
            self.tree.column("3", width=200, minwidth=200, stretch=True, anchor=tk.CENTER)
            self.tree.column("4", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.column("5", width=60, minwidth=60, stretch=True, anchor=tk.CENTER)
            self.tree.heading("#0", text="", anchor=tk.CENTER)
            self.tree.heading("1", text="Imie i nazwisko", anchor=tk.CENTER)
            self.tree.heading("2", text="Adres nieruchomości", anchor=tk.CENTER)
            self.tree.heading("3", text="Dane pośrednika", anchor=tk.CENTER)
            self.tree.heading("4", text="Kwota transakcji", anchor=tk.CENTER)
            self.tree.heading("5", text="", anchor=tk.CENTER)

            with open('DataBase_sql/inquiries/zapytanie_3.sql', 'r') as file:
                query = file.read()
                query.format(self.D1,self.D2)

            formatted_query = query.format(self.D1, self.D2)

            self.cursor.execute(formatted_query)
            print(formatted_query)
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
                self.tree.insert("", tk.END, text="", values=row, )

        def get_values():
            try:
                self.D1 = self.D1_entry.get()
                self.D2 = self.D2_entry.get()

                messagebox.showinfo("Sukces", f"Poprawnie podano dane!\n")

                self.D1_entry.delete(0, tk.END)
                self.D2_entry.delete(0, tk.END)
                popup_window.destroy()

                kw_3()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne podano dane!\n")
                print(e)
                popup_window.destroy()
                self.D1_entry.delete(0, tk.END)
                self.D2_entry.delete(0, tk.END)


        def delete():
            self.D1_entry.delete(0, tk.END)
            self.D2_entry.delete(0, tk.END)


        tk.Button(button_frame, text="Zatwierdz", command=get_values, width=15).grid(row=7, column=0, padx=5,pady=5, sticky='w')
        tk.Button(button_frame, text="Reset", command=delete, width=15).grid(row=7, column=1, padx=5,pady=5, sticky='e')
    def kwerenda_4(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("PODAJ PIERWSZA LITERE NAZWISKA")
        quarter_screen_width = 425
        quarter_screen_height = 150

        popup_window.transient(self.root)
        popup_window.overrideredirect(True)

        popup_window.grab_set()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        tk.Label(frame, text="PODAJ LITERE ").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        tk.Label(frame, text="PIERWSZA LITERA NAZWISKA:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.D1_entry = tk.Entry(frame)
        self.D1_entry.grid(row=1, column=1, padx=5, pady=5,sticky="w")

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


        def kw_4():
            self.tree = ttk.Treeview(self.tab4)
            self.tree.pack(expand=True, fill=tk.BOTH)
            self.tree["columns"] = ("1", "2", "3","4","5","6")
            self.tree.column("#0", width=0, stretch=False)
            self.tree.column("1", width=60, minwidth=60, stretch=True, anchor=tk.CENTER)
            self.tree.column("2", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.column("3", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.column("4", width=200, minwidth=200, stretch=True, anchor=tk.CENTER)
            self.tree.column("5", width=150, minwidth=150, stretch=True, anchor=tk.CENTER)
            self.tree.column("6", width=150, minwidth=150, stretch=True, anchor=tk.CENTER)
            self.tree.heading("#0", text="", anchor=tk.CENTER)
            self.tree.heading("1", text="ID klienta", anchor=tk.CENTER)
            self.tree.heading("2", text="Imie", anchor=tk.CENTER)
            self.tree.heading("3", text="Nazwisko", anchor=tk.CENTER)
            self.tree.heading("4", text="Adres Zameldowania", anchor=tk.CENTER)
            self.tree.heading("5", text="Numer telefonu", anchor=tk.CENTER)
            self.tree.heading("6", text="Adres email", anchor=tk.CENTER)

            with open('DataBase_sql/inquiries/zapytanie_4.sql', 'r') as file:
                query = file.read()
                query.format(self.D1)

            formatted_query = query.format(self.D1)

            self.cursor.execute(formatted_query)
            print(formatted_query)
            rows = self.cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, text="", values=row, )

        def get_values():
            try:
                self.D1 = self.D1_entry.get()

                messagebox.showinfo("Sukces", f"Poprawnie podano dane!\n")

                self.D1_entry.delete(0, tk.END)

                popup_window.destroy()

                kw_4()


            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne podano dane!\n")
                print(e)
                popup_window.destroy()
                self.D1_entry.delete(0, tk.END)


        def delete():
            self.D1_entry.delete(0, tk.END)


        tk.Button(button_frame, text="Zatwierdz", command=get_values, width=15).grid(row=7, column=0, padx=5,pady=5, sticky='w')
        tk.Button(button_frame, text="Reset", command=delete, width=15).grid(row=7, column=1, padx=5,pady=5, sticky='e')
    def kwerenda_5(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("PODAJ ROZMIAR POWIERZCHNI UŻYTKOWEJ")
        quarter_screen_width = 425
        quarter_screen_height = 150

        popup_window.transient(self.root)
        popup_window.overrideredirect(True)

        popup_window.grab_set()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        tk.Label(frame, text="PODAJ ROZMIAR POWIERZCHNI UŻYTKOWEJ").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        tk.Label(frame, text="POWIERZCHNIA UŻYTKOWA:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.D1_entry = tk.Entry(frame)
        self.D1_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        def kw_5():
            self.tree = ttk.Treeview(self.tab4)
            self.tree.pack(expand=True, fill=tk.BOTH)
            self.tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")
            self.tree.column("#0", width=0, stretch=False)
            self.tree.column("1", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.column("2", width=70, minwidth=70, stretch=True, anchor=tk.CENTER)
            self.tree.column("3", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.column("4", width=140, minwidth=140, stretch=True, anchor=tk.CENTER)
            self.tree.column("5", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.column("6", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.column("7", width=150, minwidth=150, stretch=True, anchor=tk.CENTER)
            self.tree.heading("#0", text="", anchor=tk.CENTER)
            self.tree.heading("1", text="ID Nieruchomosci", anchor=tk.CENTER)
            self.tree.heading("2", text="Kraj", anchor=tk.CENTER)
            self.tree.heading("3", text="Miejscowosc", anchor=tk.CENTER)
            self.tree.heading("4", text="Ulica", anchor=tk.CENTER)
            self.tree.heading("5", text="Powierzchnia", anchor=tk.CENTER)
            self.tree.heading("6", text="Liczba pokoi", anchor=tk.CENTER)
            self.tree.heading("7", text="ID Typu nieruchomosci", anchor=tk.CENTER)

            with open('DataBase_sql/inquiries/zapytanie_5.sql', 'r') as file:
                query = file.read()
                query.format(self.D1)

            formatted_query = query.format(self.D1)

            self.cursor.execute(formatted_query)
            print(formatted_query)
            rows = self.cursor.fetchall()
            for row in rows:
                self.tree.insert("", tk.END, text="", values=row, )

        def get_values():
            try:
                self.D1 = self.D1_entry.get()

                messagebox.showinfo("Sukces", f"Poprawnie podano dane!\n")

                self.D1_entry.delete(0, tk.END)

                popup_window.destroy()

                kw_5()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne podano dane!\n")
                print(e)
                popup_window.destroy()
                self.D1_entry.delete(0, tk.END)

        def delete():
            self.D1_entry.delete(0, tk.END)

        tk.Button(button_frame, text="Zatwierdz", command=get_values, width=15).grid(row=7, column=0, padx=5, pady=5,
                                                                                     sticky='w')
        tk.Button(button_frame, text="Reset", command=delete, width=15).grid(row=7, column=1, padx=5, pady=5,
                                                                             sticky='e')

    def zapytania_subtab(self,option):
        if option == "Umowy zawarte w danym zakresie lat":
            if self.tree is not None:
                self.tree.destroy()
            self.tab4_subnotebook.select(self.tab4_subtab1)
            self.kwerenda_1()

        if option == "Łaczny koszt zakupu dla każdego klienta":
            if self.tree is not None:
                self.tree.destroy()
            self.tab4_subnotebook.select(self.tab4_subtab2)
            self.kwerenda_2()

        if option == "Transakcje danego pośrednika":
            if self.tree is not None:
                self.tree.destroy()
            self.tab4_subnotebook.select(self.tab4_subtab3)
            self.kwerenda_3()

        if option == "Klienci o nazwisku na daną literę":
            if self.tree is not None:
                self.tree.destroy()
            self.tab4_subnotebook.select(self.tab4_subtab4)
            self.kwerenda_4()

        if option == "Nieruchomosci o powierzchni większej od zadanej":
            if self.tree is not None:
                self.tree.destroy()
            self.tab4_subnotebook.select(self.tab4_subtab5)
            self.kwerenda_5()








