from datetime import datetime
from tkinter import ttk, LEFT, TOP
import tkinter.messagebox as messagebox
import tkinter as tk
from bson import ObjectId

class Mongo_DB:
    def __init__(self, root,notebook,connect_mn):
        self.root = root
        self.tree = None
        self.notebook = notebook
        self.tab5 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab5, text="MongoDB")
        self.notebook.pack()
        self.tab5_subframe = None
        self.tab5_subnotebook = None
        self.tab5_submenu = None
        self.connect_mn = connect_mn
        self.D1 = ""
        self.D2 = ""
    def menu(self):
        if self.tab5_subframe is None and self.tab5_subnotebook is None:
            self.tab5_subframe = ttk.Frame(self.tab5)
            self.tab5_subnotebook = ttk.Notebook(self.tab5_subframe)
            self.tab5_subtab1 = ttk.Frame(self.tab5_subnotebook)
            self.tab5_subtab2 = ttk.Frame(self.tab5_subnotebook)
            self.tab5_subtab3 = ttk.Frame(self.tab5_subnotebook)
            self.tab5_subtab4 = ttk.Frame(self.tab5_subnotebook)
            self.tab5_subtab5 = ttk.Frame(self.tab5_subnotebook)
            self.tab5_subtab6 = ttk.Frame(self.tab5_subnotebook)
            self.tab5_subtab7 = ttk.Frame(self.tab5_subnotebook)
            self.tab5_subtab8 = ttk.Frame(self.tab5_subnotebook)

            self.tab5_subnotebook.add(self.tab5_subtab1, text="Rekordy")
            self.tab5_subnotebook.add(self.tab5_subtab2, text="Klienci")
            self.tab5_subnotebook.add(self.tab5_subtab3, text="Usun Rekord")
            self.tab5_subnotebook.add(self.tab5_subtab1, text="Umowy zawarte w danym zakresie lat")
            self.tab5_subnotebook.add(self.tab5_subtab2, text="Łaczny koszt zakupu dla każdego klienta")
            self.tab5_subnotebook.add(self.tab5_subtab3, text="Transakcje danego pośrednika")
            self.tab5_subnotebook.add(self.tab5_subtab1, text="Klienci o nazwisku na daną literę")
            self.tab5_subnotebook.add(self.tab5_subtab2, text="Nieruchomosci o powierzchni większej od zadanej")

            self.tab5_subnotebook.pack()

            if not self.tab5_submenu:
                self.tab5_submenu_var = tk.StringVar()
                self.tab5_submenu = ttk.OptionMenu(self.tab5, self.tab5_submenu_var, "Tabele", "Rekordy","Dodaj Rekord",
                                                   "Usun Rekord","Umowy zawarte w danym zakresie lat",
                                                   "Łaczny koszt zakupu dla każdego klienta",
                                                   "Transakcje danego pośrednika",
                                                   "Klienci o nazwisku na daną literę",
                                                   "Nieruchomosci o powierzchni większej od zadanej",
                                                   command=self.Opcje_menu)

                self.tab5_submenu.configure(width=74)
                self.tab5_submenu.pack(side=TOP, padx=100, pady=350)

    def Show_records(self):
        records = self.connect_mn.collection.find()
        self.tree = ttk.Treeview(self.tab5)
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree["columns"] = ("1", "2")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("1", width=300, minwidth=300, stretch=True, anchor=tk.CENTER)
        self.tree.column("2", width=460, minwidth=460, stretch=True, anchor=tk.CENTER)
        self.tree.heading("#0", text="", anchor=tk.CENTER)
        self.tree.heading("1", text="Pole", anchor=tk.CENTER)
        self.tree.heading("2", text="Wartość", anchor=tk.CENTER)

        rows = []
        for record in records:
            row = [
                ("_id", record["_id"]),
                ("Kraj", record["Kraj"]),
                ("Miejscowosc", record["Miejscowosc"]),
                ("Ulica", record["Ulica"]),
                ("Powierzchnia", record["Powierzchnia"]),
                ("Liczba_pokoi", record["Liczba_pokoi"]),
                ("Nazwa_typu_nieruchomosci", record["Nazwa_typu_nieruchomosci"]),
                ("Opis_typu_nieruchomosci", record["Opis_typu_nieruchomosci"]),
                ("Imie_klienta", record["Imie_klienta"]),
                ("Nazwisko_klienta", record["Nazwisko_klienta"]),
                ("Adres_Zameldowania", record["Adres_Zameldowania"]),
                ("Numer_telefonu_klienta", record["Numer_telefonu_klienta"]),
                ("Adres_email_klienta", record["Adres_email_klienta"]),
                ("Imie_posrednika", record["Imie_posrednika"]),
                ("Nazwisko_posrednika", record["Nazwisko_posrednika"]),
                ("Numer_telefonu_posrednika", record["Numer_telefonu_posrednika"]),
                ("Adres_email_posrednika", record["Adres_email_posrednika"]),
                ("Data_dodania", record["Data_dodania"]),
                ("Kwota_transakcji", record["Kwota_transakcji"]),
                ("Data_zawarcia", record["Data_zawarcia"]),
                ("Data_podpisania", record["Data_podpisania"])
            ]
            rows.append(row)

        for row in rows:
            self.tree.insert("", tk.END, text=row[0][1], values=(row[0][0], row[0][1]))
            for field, value in row[1:]:
                self.tree.insert("", tk.END, text=field, values=(field, value))
            self.tree.insert("", tk.END, text="", values=("", ""))
            self.tree.insert("", tk.END, text="", values=("", ""))

        self.tree.column("1", anchor="w")
        self.tree.column("2", anchor="w")
    def Add_records(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj rekord")
        quarter_screen_width = 400
        quarter_screen_height = 870
        popup_window.transient(self.root)

        popup_window.overrideredirect(True)
        popup_window.attributes('-topmost', False)
        popup_window.grab_set()

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        tk.Label(frame, text="DODAJ REKORD").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Kraj:").grid(row=1, column=0, padx=5, pady=5)
        self.rec1_entry = tk.Entry(frame)
        self.rec1_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Miejscowosc:").grid(row=2, column=0, padx=5, pady=5)
        self.rec2_entry = tk.Entry(frame)
        self.rec2_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Ulica:").grid(row=3, column=0, padx=5, pady=5)
        self.rec3_entry = tk.Entry(frame)
        self.rec3_entry.grid(row=3, column=1, padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Powierzchnia: ").grid(row=4, column=0, padx=5, pady=5)
        self.rec4_entry = tk.Entry(frame)
        self.rec4_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="Liczba pokoi: ").grid(row=5, column=0, padx=5, pady=5)
        self.rec5_entry = tk.Entry(frame)
        self.rec5_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(frame, text="Nazwa typu nieruchomosci").grid(row=6, column=0, padx=5, pady=5)
        self.rec6_entry = tk.Entry(frame)
        self.rec6_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(frame, text="Opis typu nieruchomosci").grid(row=7, column=0, padx=5, pady=5)
        self.rec7_entry = tk.Entry(frame)
        self.rec7_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(frame, text="Imie klienta").grid(row=8, column=0, padx=5, pady=5)
        self.rec8_entry = tk.Entry(frame)
        self.rec8_entry.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(frame, text="Nazwisko klienta").grid(row=9, column=0, padx=5, pady=5)
        self.rec9_entry = tk.Entry(frame)
        self.rec9_entry.grid(row=9, column=1, padx=5, pady=5)

        tk.Label(frame, text="Adres Zameldowania").grid(row=10, column=0, padx=5, pady=5)
        self.rec10_entry = tk.Entry(frame)
        self.rec10_entry.grid(row=10, column=1, padx=5, pady=5)

        tk.Label(frame, text="Numer telefonu klienta").grid(row=11, column=0, padx=5, pady=5)
        self.rec11_entry = tk.Entry(frame)
        self.rec11_entry.grid(row=11, column=1, padx=5, pady=5)

        tk.Label(frame, text="Adres email klienta").grid(row=12, column=0, padx=5, pady=5)
        self.rec12_entry = tk.Entry(frame)
        self.rec12_entry.grid(row=12, column=1, padx=5, pady=5)

        tk.Label(frame, text="Imie posrednika").grid(row=13, column=0, padx=5, pady=5)
        self.rec13_entry = tk.Entry(frame)
        self.rec13_entry.grid(row=13, column=1, padx=5, pady=5)

        tk.Label(frame, text="Nazwisko posrednika").grid(row=14, column=0, padx=5, pady=5)
        self.rec14_entry = tk.Entry(frame)
        self.rec14_entry.grid(row=14, column=1, padx=5, pady=5)

        tk.Label(frame, text="Numer telefonu posrednika").grid(row=15, column=0, padx=5, pady=5)
        self.rec15_entry = tk.Entry(frame)
        self.rec15_entry.grid(row=15, column=1, padx=5, pady=5)

        tk.Label(frame, text="Adres email posrednika").grid(row=16, column=0, padx=5, pady=5)
        self.rec16_entry = tk.Entry(frame)
        self.rec16_entry.grid(row=16, column=1, padx=5, pady=5)

        tk.Label(frame, text="Data dodania").grid(row=17, column=0, padx=5, pady=5)
        self.rec17_entry = tk.Entry(frame)
        self.rec17_entry.grid(row=17, column=1, padx=5, pady=5)

        tk.Label(frame, text="Kwota transakcji").grid(row=18, column=0, padx=5, pady=5)
        self.rec18_entry = tk.Entry(frame)
        self.rec18_entry.grid(row=18, column=1, padx=5, pady=5)

        tk.Label(frame, text="Data zawarcia").grid(row=19, column=0, padx=5, pady=5)
        self.rec19_entry = tk.Entry(frame)
        self.rec19_entry.grid(row=19, column=1, padx=5, pady=5)

        tk.Label(frame, text="Data podpisania").grid(row=20, column=0, padx=5, pady=5)
        self.rec20_entry = tk.Entry(frame)
        self.rec20_entry.grid(row=20, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=21, column=0, columnspan=2, padx=5, pady=5)

        def add_record():
            try:
                id = ObjectId()

                rec1 = self.rec1_entry.get()
                rec2 = self.rec2_entry.get()
                rec3 = self.rec3_entry.get()
                rec4 = float(self.rec4_entry.get())
                rec5 = int(self.rec5_entry.get())
                rec6 = self.rec6_entry.get()
                rec7 = self.rec7_entry.get()
                rec8 = self.rec8_entry.get()
                rec9 = self.rec9_entry.get()
                rec10 = self.rec10_entry.get()
                rec11 = self.rec11_entry.get()
                rec12 = self.rec12_entry.get()
                rec13 = self.rec13_entry.get()
                rec14 = self.rec14_entry.get()
                rec15 = self.rec15_entry.get()
                rec16 = self.rec16_entry.get()
                rec17 = datetime.strptime(self.rec17_entry.get(), "%Y-%m-%d")
                rec18 = float(self.rec4_entry.get())
                rec19 = datetime.strptime(self.rec19_entry.get(), "%Y-%m-%d")
                rec20 = datetime.strptime(self.rec20_entry.get(), "%Y-%m-%d")

                data = {
                    "_id": id,
                    "Kraj": rec1,
                    "Miejscowosc": rec2,
                    "Ulica": rec3,
                    "Powierzchnia": rec4,
                    "Liczba_pokoi": rec5,
                    "Nazwa_typu_nieruchomosci": rec6,
                    "Opis_typu_nieruchomosci": rec7,
                    "Imie_klienta": rec8,
                    "Nazwisko_klienta": rec9,
                    "Adres_Zameldowania": rec10,
                    "Numer_telefonu_klienta": rec11,
                    "Adres_email_klienta": rec12,
                    "Imie_posrednika": rec13,
                    "Nazwisko_posrednika": rec14,
                    "Numer_telefonu_posrednika": rec15,
                    "Adres_email_posrednika": rec16,
                    "Data_dodania": rec17,
                    "Kwota_transakcji" : rec18,
                    "Data_zawarcia": rec19,
                    "Data_podpisania": rec20
                }

                result = self.connect_mn.collection.insert_one(data)
                if not result.acknowledged:
                    raise NameError("Nieznany błąd podczas dodawania rekordu.")
                messagebox.showinfo("Sukcess", f"Dodano rekord do bazy danych!\n")

                self.rec1_entry.delete(0, tk.END)
                self.rec2_entry.delete(0, tk.END)
                self.rec3_entry.delete(0, tk.END)
                self.rec4_entry.delete(0, tk.END)
                self.rec5_entry.delete(0, tk.END)
                self.rec6_entry.delete(0, tk.END)
                self.rec7_entry.delete(0, tk.END)
                self.rec8_entry.delete(0, tk.END)
                self.rec9_entry.delete(0, tk.END)
                self.rec10_entry.delete(0, tk.END)
                self.rec11_entry.delete(0, tk.END)
                self.rec12_entry.delete(0, tk.END)
                self.rec13_entry.delete(0, tk.END)
                self.rec14_entry.delete(0, tk.END)
                self.rec15_entry.delete(0, tk.END)
                self.rec16_entry.delete(0, tk.END)
                self.rec17_entry.delete(0, tk.END)
                self.rec18_entry.delete(0, tk.END)
                self.rec19_entry.delete(0, tk.END)
                self.rec20_entry.delete(0, tk.END)

                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
                print(e)
                popup_window.destroy()

        def delete():
            info = messagebox.askyesnocancel("Sukcess", f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.rec1_entry.delete(0, tk.END)
                self.rec2_entry.delete(0, tk.END)
                self.rec3_entry.delete(0, tk.END)
                self.rec4_entry.delete(0, tk.END)
                self.rec5_entry.delete(0, tk.END)
                self.rec6_entry.delete(0, tk.END)
                self.rec7_entry.delete(0, tk.END)
                self.rec8_entry.delete(0, tk.END)
                self.rec9_entry.delete(0, tk.END)
                self.rec10_entry.delete(0, tk.END)
                self.rec11_entry.delete(0, tk.END)
                self.rec12_entry.delete(0, tk.END)
                self.rec13_entry.delete(0, tk.END)
                self.rec14_entry.delete(0, tk.END)
                self.rec15_entry.delete(0, tk.END)
                self.rec16_entry.delete(0, tk.END)
                self.rec17_entry.delete(0, tk.END)
                self.rec18_entry.delete(0, tk.END)
                self.rec19_entry.delete(0, tk.END)
                self.rec20_entry.delete(0, tk.END)
                popup_window.destroy()
                self.tab5_submenu.configure(width=74)
                self.tab5_submenu.pack(side=TOP, padx=100)
            else:
                self.empty_window()

        tk.Button(button_frame, text="Dodaj", command=add_record, width=15).grid(row=8, column=0, padx=5, pady=10,
                                                                                       sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete, width=15).grid(row=8, column=1, padx=5, pady=10,
                                                                             sticky='e')
    def Remove_records(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("USUN REKORD")
        quarter_screen_width = 400
        quarter_screen_height = 125

        popup_window.transient(self.root)
        popup_window.overrideredirect(True)
        popup_window.attributes('-topmost', False)

        popup_window.grab_set()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        tk.Label(frame, text="USUN REKORD").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        tk.Label(frame, text="_ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.ID_entry = tk.Entry(frame)
        self.ID_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        def rem():
            try:
                id = self.ID_entry.get()
                object_id = ObjectId(id)
                result = self.connect_mn.collection.delete_one({"_id": object_id})
                if result.deleted_count != 1:
                    raise NameError("Nieznany blad")

                messagebox.showinfo("Sukces", f"Usunieto rekord z bazy danych!\n")

                self.ID_entry.delete(0, tk.END)
                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne usuniecie rekordu do bazy danych!\n")
                print(e)
                popup_window.destroy()

        def delete():
            info = messagebox.askyesnocancel("Sukcess", f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.ID_entry.delete(0, tk.END)
                popup_window.destroy()
                self.tab5_submenu.configure(width=74)
                self.tab5_submenu.pack(side=TOP, padx=100)
            else:
                self.empty_window()

        tk.Button(button_frame, text="Usun", command=rem, width=15).grid(row=7, column=0, padx=5, pady=5, sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete, width=15).grid(row=7, column=1, padx=5, pady=5,
                                                                             sticky='e')

    def kwerenda_1(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Podaj daty")
        quarter_screen_width = 400
        quarter_screen_height = 175

        popup_window.transient(self.root)
        popup_window.overrideredirect(True)
        popup_window.attributes('-topmost', False)
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
            self.tree = ttk.Treeview(self.tab5)
            self.tree.pack(expand=True, fill=tk.BOTH)
            self.tree["columns"] = ("1", "2", "3", "4")
            self.tree.column("#0", width=0, stretch=False)
            self.tree.column("1", width=250, minwidth=250, stretch=True, anchor=tk.CENTER)
            self.tree.column("2", width=150, minwidth=150, stretch=True, anchor=tk.CENTER)
            self.tree.column("3", width=150, minwidth=150, stretch=True, anchor=tk.CENTER)
            self.tree.column("4", width=210, minwidth=210, stretch=True, anchor=tk.CENTER)
            self.tree.heading("#0", text="", anchor=tk.CENTER)
            self.tree.heading("1", text="Opis", anchor=tk.CENTER)
            self.tree.heading("2", text="Data zawarcia", anchor=tk.CENTER)
            self.tree.heading("3", text="Imie i nazwisko", anchor=tk.CENTER)
            self.tree.heading("4", text="", anchor=tk.CENTER)

            d1 = datetime.strptime(self.D1, "%Y-%m-%d")
            d2 = datetime.strptime(self.D2, "%Y-%m-%d")

            # Tworzenie zapytania z warunkiem dotyczącym daty transakcji
            query = {
                "Data_dodania": {
                    "$gte": d1,
                    "$lte": d2
                }
            }

            results = self.connect_mn.collection.aggregate([
                {
                    "$match": query  # Dodaj to, jeśli chcesz zachować istniejące warunki zapytania
                },
                {
                    "$project": {
                        "_id": 0,  # Wyklucz pole 'id_'
                        "Klient": {
                            "$concat": ["$Imie_klienta", " ", "$Nazwisko_klienta"]
                        },
                        "Data_zawarcia": 1,
                        "Opis_typu_nieruchomosci": 1
                    }
                }
            ])

            for result in results:
                values = list(result.values())
                self.tree.insert("", tk.END, text="", values=values)

        def get_values():
            try:
                self.D1 = self.D1_entry.get()
                self.D2 = self.D2_entry.get()

                kw_1()

                messagebox.showinfo("Sukces", f"Poprawnie podano dane!\n")

                self.D1_entry.delete(0, tk.END)
                self.D2_entry.delete(0, tk.END)
                popup_window.destroy()


            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne podano dane!\n")
                print(e)
                popup_window.destroy()
                self.D1_entry.delete(0, tk.END)
                self.D2_entry.delete(0, tk.END)

        def delete():
            info = messagebox.askyesnocancel("Sukcess",f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.D1_entry.delete(0, tk.END)
                self.D2_entry.delete(0, tk.END)
                popup_window.destroy()
                self.tab5_submenu.configure(width=74)
                self.tab5_submenu.pack(side=TOP, padx=100)
            else:
                self.empty_window()


        tk.Button(button_frame, text="Zatwierdz", command=get_values, width=15).grid(row=7, column=0, padx=5,pady=5, sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete, width=15).grid(row=7, column=1, padx=5,pady=5, sticky='e')
    def kwerenda_2(self):
        def kw_2():
            self.tree = ttk.Treeview(self.tab5)
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

            pipeline = [
                {
                    "$group": {
                        "_id": {
                            "Imie_klienta": "$Imie_klienta",
                            "Nazwisko_klienta": "$Nazwisko_klienta"
                        },
                        "Laczna_cena_nieruchomosci": {"$sum": "$Kwota_transakcji"}
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                        "Imię i nazwisko": {"$concat": ["$_id.Imie_klienta", " ", "$_id.Nazwisko_klienta"]},
                        "Łączna cena nieruchomości": "$Laczna_cena_nieruchomosci"
                    }
                }
            ]

            results = self.connect_mn.collection.aggregate(pipeline)

            for result in results:
                values = [result["Imię i nazwisko"], result["Łączna cena nieruchomości"], ""]
                self.tree.insert("", tk.END, text="", values=values)

        kw_2()
    def kwerenda_3(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Podaj Imie i nazwisko pośrednika")
        quarter_screen_width = 400
        quarter_screen_height = 175


        popup_window.transient(self.root)
        popup_window.overrideredirect(True)
        popup_window.attributes('-topmost', False)
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
            self.tree = ttk.Treeview(self.tab5)
            self.tree.pack(expand=True, fill=tk.BOTH)
            self.tree["columns"] = ("1", "2", "3","4")
            self.tree.column("#0", width=0, stretch=False)
            self.tree.column("1", width=150, minwidth=150, stretch=True, anchor=tk.CENTER)
            self.tree.column("2", width=250, minwidth=250, stretch=True, anchor=tk.CENTER)
            self.tree.column("3", width=250, minwidth=250, stretch=True, anchor=tk.CENTER)
            self.tree.column("4", width=110, minwidth=110, stretch=True, anchor=tk.CENTER)
            self.tree.heading("#0", text="", anchor=tk.CENTER)
            self.tree.heading("1", text="Imie i nazwisko", anchor=tk.CENTER)
            self.tree.heading("2", text="Adres nieruchomości", anchor=tk.CENTER)
            self.tree.heading("3", text="Dane pośrednika", anchor=tk.CENTER)
            self.tree.heading("4", text="Kwota transakcji", anchor=tk.CENTER)

            query = {
                "Imie_posrednika": self.D1,
                "Nazwisko_posrednika": self.D2
            }

            pipeline = [
                {
                    "$match": query
                },
                {
                    "$project": {
                        "_id": 0,
                        "Imię i nazwisko": {"$concat": ["$Imie_klienta", " ", "$Nazwisko_klienta"]},
                        "Adres nieruchomości": {"$concat": ["$Kraj", ", ", "$Miejscowosc", ", ", "$Ulica"]},
                        "Dane pośrednika": {"$concat": ["$Imie_posrednika", ", ", "$Nazwisko_posrednika", ", ", "$Numer_telefonu_posrednika"]},
                        "Kwota_transakcji": 1,
                    }
                }
            ]

            results = self.connect_mn.collection.aggregate(pipeline)

            for result in results:
                values = [result["Imię i nazwisko"], result["Adres nieruchomości"],result["Dane pośrednika"],result["Kwota_transakcji"]]
                self.tree.insert("", tk.END, text="", values=values)

        def get_values():
            try:
                self.D1 = self.D1_entry.get()
                self.D2 = self.D2_entry.get()

                kw_3()
                messagebox.showinfo("Sukces", f"Poprawnie podano dane!\n")

                self.D1_entry.delete(0, tk.END)
                self.D2_entry.delete(0, tk.END)
                popup_window.destroy()



            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne podano dane!\n")
                print(e)
                popup_window.destroy()
                self.D1_entry.delete(0, tk.END)
                self.D2_entry.delete(0, tk.END)

        def delete():
            info = messagebox.askyesnocancel("Sukcess",f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.D1_entry.delete(0, tk.END)
                self.D2_entry.delete(0, tk.END)
                popup_window.destroy()
                self.tab5_submenu.configure(width=74)
                self.tab5_submenu.pack(side=TOP, padx=100)
            else:
                self.empty_window()


        tk.Button(button_frame, text="Zatwierdz", command=get_values, width=15).grid(row=7, column=0, padx=5,pady=5, sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete, width=15).grid(row=7, column=1, padx=5,pady=5, sticky='e')
    def kwerenda_4(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("PODAJ PIERWSZA LITERE NAZWISKA")
        quarter_screen_width = 425
        quarter_screen_height = 150


        popup_window.transient(self.root)
        popup_window.overrideredirect(True)
        popup_window.attributes('-topmost', False)
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
            self.tree = ttk.Treeview(self.tab5)
            self.tree.pack(expand=True, fill=tk.BOTH)
            self.tree["columns"] = ("1", "2", "3","4","5","6")
            self.tree.column("#0", width=0, stretch=False)
            self.tree.column("1", width=60, minwidth=60, stretch=True, anchor=tk.CENTER)
            self.tree.column("2", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.column("3", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.column("4", width=200, minwidth=200, stretch=True, anchor=tk.CENTER)
            self.tree.column("5", width=150, minwidth=150, stretch=True, anchor=tk.CENTER)
            self.tree.heading("#0", text="", anchor=tk.CENTER)
            self.tree.heading("1", text="Imie", anchor=tk.CENTER)
            self.tree.heading("2", text="Nazwisko", anchor=tk.CENTER)
            self.tree.heading("3", text="Adres Zameldowania", anchor=tk.CENTER)
            self.tree.heading("4", text="Numer telefonu", anchor=tk.CENTER)
            self.tree.heading("5", text="Adres email", anchor=tk.CENTER)

            query = {
                "Nazwisko_klienta": {"$regex": "^" + self.D1, "$options": "i"}
            }

            projection = {
                "_id": 0,
                "Imie_klienta": 1,
                "Nazwisko_klienta": 1,
                "Adres_Zameldowania": 1,
                "Numer_telefonu_klienta": 1,
                "Adres_email_klienta": 1
            }

            results = self.connect_mn.collection.find(query, projection)

            for result in results:
                imie = result["Imie_klienta"]
                nazwisko = result["Nazwisko_klienta"]
                adres_zameldowania = result["Adres_Zameldowania"]
                numer_telefonu = result["Numer_telefonu_klienta"]
                adres_email = result["Adres_email_klienta"]

                values = [imie, nazwisko, adres_zameldowania, numer_telefonu, adres_email]
                self.tree.insert("", tk.END, text="", values=values)

        def get_values():
            try:
                self.D1 = self.D1_entry.get()

                kw_4()

                messagebox.showinfo("Sukces", f"Poprawnie podano dane!\n")

                self.D1_entry.delete(0, tk.END)

                popup_window.destroy()


            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne podano dane!\n")
                print(e)
                popup_window.destroy()
                self.D1_entry.delete(0, tk.END)

        def delete():
            info = messagebox.askyesnocancel("Sukcess",f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.D1_entry.delete(0, tk.END)
                popup_window.destroy()
                self.tab5_submenu.configure(width=74)
                self.tab5_submenu.pack(side=TOP, padx=100)
            else:
                self.empty_window()


        tk.Button(button_frame, text="Zatwierdz", command=get_values, width=15).grid(row=7, column=0, padx=5,pady=5, sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete, width=15).grid(row=7, column=1, padx=5,pady=5, sticky='e')
    def kwerenda_5(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("PODAJ ROZMIAR POWIERZCHNI UŻYTKOWEJ")
        quarter_screen_width = 425
        quarter_screen_height = 150


        popup_window.transient(self.root)
        popup_window.overrideredirect(True)
        popup_window.attributes('-topmost', False)
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
            self.tree = ttk.Treeview(self.tab5)
            self.tree.pack(expand=True, fill=tk.BOTH)
            self.tree["columns"] = ("1", "2", "3", "4", "5")
            self.tree.column("#0", width=0, stretch=False)
            self.tree.column("1", width=70, minwidth=70, stretch=True, anchor=tk.CENTER)
            self.tree.column("2", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.column("3", width=140, minwidth=140, stretch=True, anchor=tk.CENTER)
            self.tree.column("4", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.column("5", width=100, minwidth=100, stretch=True, anchor=tk.CENTER)
            self.tree.heading("#0", text="", anchor=tk.CENTER)
            self.tree.heading("1", text="Kraj", anchor=tk.CENTER)
            self.tree.heading("2", text="Miejscowosc", anchor=tk.CENTER)
            self.tree.heading("3", text="Ulica", anchor=tk.CENTER)
            self.tree.heading("4", text="Powierzchnia", anchor=tk.CENTER)
            self.tree.heading("5", text="Liczba pokoi", anchor=tk.CENTER)

            query = {
                "Powierzchnia": {"$gt": float(self.D1)}
            }

            projection = {
                "_id": 0,
                "Kraj": 1,
                "Miejscowosc": 1,
                "Ulica": 1,
                "Powierzchnia": 1,
                "Liczba_pokoi": 1
            }

            results = self.connect_mn.collection.find(query, projection)

            for result in results:
                kraj = result["Kraj"]
                miejscowosc = result["Miejscowosc"]
                ulica = result["Ulica"]
                powierzchnia = result["Powierzchnia"]
                liczba_pokoi = result["Liczba_pokoi"]

                values = [kraj, miejscowosc, ulica, powierzchnia, liczba_pokoi]
                self.tree.insert("", tk.END, text="", values=values)

        def get_values():
            try:
                self.D1 = self.D1_entry.get()

                kw_5()

                messagebox.showinfo("Sukces", f"Poprawnie podano dane!\n")

                self.D1_entry.delete(0, tk.END)

                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne podano dane!\n")
                print(e)
                popup_window.destroy()
                self.D1_entry.delete(0, tk.END)

        def delete():
            info = messagebox.askyesnocancel("Sukcess",f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.D1_entry.delete(0, tk.END)
                popup_window.destroy()
                self.tab5_submenu.configure(width=74)
                self.tab5_submenu.pack(side=TOP, padx=100)
            else:
                self.empty_window()

        tk.Button(button_frame, text="Zatwierdz", command=get_values, width=15).grid(row=7, column=0, padx=5, pady=5,
                                                                                     sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete, width=15).grid(row=7, column=1, padx=5, pady=5,
                                                                             sticky='e')

    def Opcje_menu(self, option):

        self.tab5_submenu.configure(width=10)
        self.tab5_submenu.pack(side=LEFT, padx=10, pady=350)

        if option == "Rekordy":
            if self.tree is not None:
                self.tree.destroy()
            self.Show_records()
        if option == "Dodaj Rekord":
            if self.tree is not None:
                self.tree.destroy()
            self.Add_records()
        if option == "Usun Rekord":
            if self.tree is not None:
                self.tree.destroy()
            self.Remove_records()
        if option == "Umowy zawarte w danym zakresie lat":
            if self.tree is not None:
                self.tree.destroy()
            self.kwerenda_1()
        if option == "Łaczny koszt zakupu dla każdego klienta":
            if self.tree is not None:
                self.tree.destroy()
            self.kwerenda_2()
        if option == "Transakcje danego pośrednika":
            if self.tree is not None:
                self.tree.destroy()
            self.kwerenda_3()
        if option == "Klienci o nazwisku na daną literę":
            if self.tree is not None:
                self.tree.destroy()
            self.kwerenda_4()
        if option == "Nieruchomosci o powierzchni większej od zadanej":
            if self.tree is not None:
                self.tree.destroy()
            self.kwerenda_5()

    def empty_window(self):
        pom = tk.Toplevel(self.root)
        pom.resizable(False, False)
        pom.destroy()