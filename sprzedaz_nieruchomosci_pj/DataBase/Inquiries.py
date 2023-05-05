import tkinter as tk
from tkinter import ttk, LEFT
import tkinter.messagebox as messagebox
import asyncio


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
    def menu(self):
        # Menu:
        if self.tab4_subframe is None and self.tab4_subnotebook is None:

            self.tab4_subframe = ttk.Frame(self.tab4)
            self.tab4_subnotebook = ttk.Notebook(self.tab4_subframe)

            self.tab4_subtab1 = ttk.Frame(self.tab4_subnotebook)
            self.tab4_subnotebook.add(self.tab4_subtab1, text="Umowy zawarte w danym zakresie lat")

            self.tab4_subnotebook.pack()

            # Submenu:
            self.tab4_submenu_var = tk.StringVar()
            self.tab4_submenu = ttk.OptionMenu(self.tab4, self.tab4_submenu_var, "Tabele",
                                               "Umowy zawarte w danym zakresie lat",
                                               command=self.zapytania_subtab)

            self.tab4_submenu.configure(width=14)
            self.tab4_submenu.pack(side=LEFT, padx=10, pady=350)

    def podaj_daty(self):
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

        self.D1 = ""
        self.D2 = ""

        def get_values():
            try:
                self.D1 = self.D1_entry.get()
                self.D2 = self.D2_entry.get()

                messagebox.showinfo("Sukces", f"Poprawnie pobrano dane!\n")

                self.D1_entry.delete(0, tk.END)
                self.D2_entry.delete(0, tk.END)
                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
                print(e)
                popup_window.destroy()

        def delete():
            self.D1_entry.delete(0, tk.END)
            self.D2_entry.delete(0, tk.END)

        tk.Button(button_frame, text="Zatwierdz", command=get_values, width=15).grid(row=7, column=0, padx=5,pady=5, sticky='w')
        tk.Button(button_frame, text="Reset", command=delete, width=15).grid(row=7, column=1, padx=5,pady=5, sticky='e')

    def kwerenda_1(self):


        self.tree = ttk.Treeview(self.tab4)
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree["columns"] = ("1", "2", "3","4")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("1", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
        self.tree.column("2", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
        self.tree.column("3", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
        self.tree.column("4", width=460, minwidth=460, stretch=True, anchor=tk.CENTER)
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        self.tree.heading("1", text="Imie i nazwisko", anchor=tk.CENTER)
        self.tree.heading("2", text="Data zawarcia", anchor=tk.CENTER)
        self.tree.heading("3", text="Opis", anchor=tk.CENTER)
        self.tree.heading("4", text="", anchor=tk.CENTER)



        query = "SELECT Concat(Klienci.Imie, ' ', Klienci.Nazwisko) as \"Imie i nazwisko\", Umowy.Data_zawarcia, Typy_nieruchomosci.Opis " \
                "FROM Klienci " \
                "INNER JOIN Umowy ON Umowy.ID_Klienta = Klienci.ID_Klienta " \
                "INNER JOIN Nieruchomosci ON Umowy.ID_Nieruchomosci = Nieruchomosci.ID_Nieruchomosci " \
                "INNER JOIN Typy_nieruchomosci ON Nieruchomosci.ID_Typu_nieruchomosci = Typy_nieruchomosci.ID_Typu_nieruchomosci " \
                "WHERE Umowy.Data_zawarcia BETWEEN '{}' AND '{}';".format(self.D1,self.D2)

        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, text="", values=row, )


    def zapytania_subtab(self,option):
        if option == "Umowy zawarte w danym zakresie lat":
            if self.tree is not None:
                self.tree.destroy()
            self.tab4_subnotebook.select(self.tab4_subtab1)
            self.podaj_daty()
            self.kwerenda_1()
