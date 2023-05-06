from tkinter import ttk, LEFT
import tkinter.messagebox as messagebox
import tkinter as tk

"""Moduł usuwania rekordow"""
class Usun_rekord:
    def __init__(self,root,cursor,notebook,conn):
        self.root = root
        self.conn = conn
        self.cursor = cursor
        self.tree = None
        self.notebook = notebook
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Usun rekord")
        self.notebook.pack()
        self.tab3_subframe = None
        self.tab3_subnotebook = None
        self.tab3_submenu = None
        self.nazwa_entry = None
    def menu(self):
        # Menu:
            self.tab3_subframe = ttk.Frame(self.tab3)
            self.tab3_subnotebook = ttk.Notebook(self.tab3_subframe)
            self.tab3_subtab1 = ttk.Frame(self.tab3_subnotebook)
            self.tab3_subtab2 = ttk.Frame(self.tab3_subnotebook)
            self.tab3_subtab3 = ttk.Frame(self.tab3_subnotebook)
            self.tab3_subtab4 = ttk.Frame(self.tab3_subnotebook)
            self.tab3_subtab5 = ttk.Frame(self.tab3_subnotebook)
            self.tab3_subtab6 = ttk.Frame(self.tab3_subnotebook)
            self.tab3_subtab7 = ttk.Frame(self.tab3_subnotebook)

            self.tab3_subnotebook.add(self.tab3_subtab1, text="Klienci")
            self.tab3_subnotebook.add(self.tab3_subtab2, text="Nieruchomosci")
            self.tab3_subnotebook.add(self.tab3_subtab3, text="Oferty")
            self.tab3_subnotebook.add(self.tab3_subtab4, text="Posrednicy")
            self.tab3_subnotebook.add(self.tab3_subtab5, text="Transakcje")
            self.tab3_subnotebook.add(self.tab3_subtab6, text="Typy_nieruchomosci")
            self.tab3_subnotebook.add(self.tab3_subtab7, text="Umowy")
            self.tab3_subnotebook.pack()

            # Submenu:

            if not self.tab3_submenu:
                self.tab3_submenu_var = tk.StringVar()
                self.tab3_submenu = ttk.OptionMenu(self.tab3, self.tab3_submenu_var, "Tabele", "Klienci",
                                           "Nieruchomosci", "Oferty", "Posrednicy", "Transakcje", "Typy_nieruchomosci",
                                           "Umowy", command=self.Remove_subtab)
                self.tab3_submenu.configure(width=14)
                self.tab3_submenu.pack(side=LEFT, padx=10, pady=350)

    def Remove_Tab(self,tabela,rem_tab):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Usun {}".format(tabela))
        quarter_screen_width = 400
        quarter_screen_height = 125

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

        tk.Label(frame, text="USUN {}".format(tabela)).grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        tk.Label(frame, text="ID_{}:".format(tabela)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.ID_entry = tk.Entry(frame)
        self.ID_entry.grid(row=1, column=1, padx=5, pady=5,sticky="w")

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        def rem():
            try:
                id = self.ID_entry.get()

                rem_tab(id)
                messagebox.showinfo("Sukces", f"Usunieto rekord z bazy danych!\n")

                self.ID_entry.delete(0, tk.END)
                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne usuniecie rekordu do bazy danych!\n")
                print(e)
                popup_window.destroy()

        def delete():
            self.ID_entry.delete(0, tk.END)

        tk.Button(button_frame, text="Usun", command=rem, width=15).grid(row=7, column=0, padx=5,pady=5, sticky='w')
        tk.Button(button_frame, text="Reset", command=delete, width=15).grid(row=7, column=1, padx=5,pady=5, sticky='e')

    def Remove_subtab(self, option):
        if option == "Klienci":
            self.Remove_Tab("KLIENTA",self.rem_client_to_database)
        if option == "Nieruchomosci":
            self.Remove_Tab("NIERUCHOMOSC", self.rem_nieruchomosc_to_database)
        if option == "Oferty":
            self.Remove_Tab("OFERTY", self.rem_oferty_to_database)
        if option == "Posrednicy":
            self.Remove_Tab("POSREDNIKA", self.rem_posrednik_to_database)
        if option == "Transakcje":
            self.Remove_Tab("TRANSAKCJE", self.rem_transakcja_to_database)
        if option == "Typy_nieruchomosci":
            self.Remove_Tab("TYP NIERUCHOMOSCI", self.rem_typy_nieruchomosci_to_database)
        if option == "Umowy":
            self.Remove_Tab("UMOWY", self.rem_umowa_to_database)

    def rem_client_to_database(self,id):
        sql = "DELETE FROM Klienci WHERE ID_Klienta= {}".format(id)
        self.cursor.execute(sql)
        self.root.update()
        self.conn.commit()

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()
    def rem_nieruchomosc_to_database(self,id):
        sql = "DELETE FROM Nieruchomosci WHERE ID_Nieruchomosci = {}".format(id)
        self.cursor.execute(sql)
        self.root.update()
        self.conn.commit()

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()
    def rem_oferty_to_database(self,id):
        sql = "DELETE FROM Oferty WHERE ID_Oferty = {}".format(id)
        self.cursor.execute(sql)
        self.root.update()
        self.conn.commit()
    def rem_posrednik_to_database(self,id):
        sql = "DELETE FROM Posrednicy WHERE ID_Posrednika = {}".format(id)
        self.cursor.execute(sql)
        self.root.update()
        self.conn.commit()
    def rem_transakcja_to_database(self,id):
        sql = "DELETE FROM Transakcje WHERE ID_Transakcji = {}".format(id)
        self.cursor.execute(sql)
        self.root.update()
        self.conn.commit()
    def rem_typy_nieruchomosci_to_database(self,id):
        sql = "DELETE FROM Typy_nieruchomosci  WHERE ID_Typu_nieruchomosci = {}".format(id)
        self.cursor.execute(sql)
        self.root.update()
        self.conn.commit()
    def rem_umowa_to_database(self,id):
        sql = "DELETE FROM Umowy WHERE ID_Umowy = {}".format(id)
        self.cursor.execute(sql)
        self.root.update()
        self.conn.commit()


