from tkinter import ttk, LEFT
import tkinter.messagebox as messagebox
import tkinter as tk

"""Moduł dodawania rekordow"""
class Dodaj_rekord:
    def __init__(self,root,cursor,notebook,conn):
        self.root = root
        self.conn = conn
        self.cursor = cursor
        self.tree = None
        self.notebook = notebook
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Dodaj rekord")
        self.notebook.pack()
        self.tab2_subframe = None
        self.tab2_subnotebook = None
    def menu(self):
        # Menu:
        if self.tab2_subframe is None and self.tab2_subnotebook is None:
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
                                           "Nieruchomosci", "Oferty", "Posrednicy", "Transakcje", "Typy_nieruchomosci",
                                           "Umowy", command=self.Add_subtab)
            self.tab2_submenu.pack(side=LEFT,padx=10)

    def Add_Klienci(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Klienta")
        quarter_screen_width = 400
        quarter_screen_height = 280
        popup_window.transient(self.root)
        popup_window.grab_set()

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Imię:").grid(row=0, column=0, padx=5, pady=5)
        self.imie_entry = tk.Entry(frame)
        self.imie_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Nazwisko:").grid(row=1, column=0, padx=5, pady=5)
        self.nazwisko_entry = tk.Entry(frame)
        self.nazwisko_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Adres_zameldowania:").grid(row=2, column=0, padx=5, pady=5)
        self.Adres_zameldowania_entry = tk.Entry(frame)
        self.Adres_zameldowania_entry.grid(row=2, column=1, padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Numer telefonu: ").grid(row=3, column=0, padx=5, pady=5)
        self.numer_telefonu_entry = tk.Entry(frame)
        self.numer_telefonu_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="Adres email: ").grid(row=4, column=0, padx=5, pady=5)
        self.adres_email_entry = tk.Entry(frame)
        self.adres_email_entry.grid(row=4, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        def add_client():
            # pobierz wartości z pól tekstowych
            imie =  self.imie_entry.get()
            nazwisko =  self.nazwisko_entry.get()
            Adres_zameldowania = self.Adres_zameldowania_entry.get()
            numer_telefonu = self.numer_telefonu_entry.get()
            adres_email = self.adres_email_entry.get()
            # dodaj rekord do bazy danych
            try:
                self.add_client_to_database(imie, nazwisko, Adres_zameldowania, numer_telefonu, adres_email)
            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
            else:
                popup_window.destroy()

        tk.Button(button_frame, text="Dodaj klienta", command=add_client).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Anuluj", command=popup_window.destroy).grid(row=6, column=1, padx=5, pady=5)
        popup_window.protocol("WM_DELETE_WINDOW", popup_window.destroy)
    def add_client_to_database(self,imie, nazwisko, Adres_zameldowania, numer_telefonu,adres_email):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Klienci (Imie,Nazwisko,Adres_Zameldowania,Numer_telefonu,Adres_email) VALUES (%s, %s, %s,%s,%s)"
        val = (imie, nazwisko, Adres_zameldowania, numer_telefonu,adres_email)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()

    def Add_Nieruchomosci(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Nieruchomosci")
        quarter_screen_width = 400
        quarter_screen_height = 280
        popup_window.transient(self.root)
        popup_window.grab_set()

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Kraj:").grid(row=0, column=0, padx=5, pady=5)
        self.Kraj_entry = tk.Entry(frame)
        self.Kraj_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Miejscowosc:").grid(row=1, column=0, padx=5, pady=5)
        self.Miejscowosc_entry = tk.Entry(frame)
        self.Miejscowosc_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Ulica:").grid(row=2, column=0, padx=5, pady=5)
        self.Ulica_entry = tk.Entry(frame)
        self.Ulica_entry.grid(row=2, column=1, padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Powierzchnia: ").grid(row=3, column=0, padx=5, pady=5)
        self.Powierzchnia_entry = tk.Entry(frame)
        self.Powierzchnia_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="Liczba pokoi: ").grid(row=4, column=0, padx=5, pady=5)
        self.Liczba_pokoi_entry = tk.Entry(frame)
        self.Liczba_pokoi_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="ID Typu nieruchomosci").grid(row=5, column=0, padx=5, pady=5)
        self.ID_Typu_nieruchomosci_entry = tk.Entry(frame)
        self.ID_Typu_nieruchomosci_entry.grid(row=5, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        def add_nieruchomosc():
            # pobierz wartości z pól tekstowych
            Kraj =  self.Kraj_entry.get()
            Miejscowosc =  self.Miejscowosc_entry.get()
            Ulica = self.Ulica_entry.get()
            Powierzchnia = self.Powierzchnia_entry.get()
            Liczba_pokoi = self.Liczba_pokoi_entry.get()
            ID_Typu_nieruchomosci = self.ID_Typu_nieruchomosci_entry.get()
            # dodaj rekord do bazy danych
            try:
                self.add_nieruchomosc_to_database(Kraj,Miejscowosc,Ulica,Powierzchnia,Liczba_pokoi,ID_Typu_nieruchomosci)
            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
            else:
                popup_window.destroy()

        tk.Button(button_frame, text="Dodaj Nieruchomosc", command=add_nieruchomosc).grid(row=7, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Anuluj", command=popup_window.destroy).grid(row=7, column=1, padx=5, pady=5)
        popup_window.protocol("WM_DELETE_WINDOW", popup_window.destroy)
    def add_nieruchomosc_to_database(self,Kraj,Miejscowosc,Ulica,Powierzchnia,Liczba_pokoi,ID_Typu_nieruchomosci):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Nieruchomosci (Kraj,Miejscowosc,Ulica,Powierzchnia,Liczba_pokoi,ID_Typu_nieruchomosci) VALUES (%s, %s, %s,%s,%s,%s)"
        val = (Kraj,Miejscowosc,Ulica,Powierzchnia,Liczba_pokoi,ID_Typu_nieruchomosci)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()

    def Add_Oferty(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Oferty")
        quarter_screen_width = 400
        quarter_screen_height = 200
        popup_window.transient(self.root)
        popup_window.grab_set()

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Id Nieruchomosci:").grid(row=0, column=0, padx=5, pady=5)
        self.Id_Nieruchomosci_entry = tk.Entry(frame)
        self.Id_Nieruchomosci_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="ID Posrednika:").grid(row=1, column=0, padx=5, pady=5)
        self.ID_Posrednika_entry = tk.Entry(frame)
        self.ID_Posrednika_entry.grid(row=1, column=1, padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Data dodania:").grid(row=2, column=0, padx=5, pady=5)
        self.Data_dodania_entry = tk.Entry(frame)
        self.Data_dodania_entry.grid(row=2, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        def add_oferty():
            # pobierz wartości z pól tekstowych
            Id_Nieruchomosci = self.Id_Nieruchomosci_entry.get()
            ID_Posrednika = self.ID_Posrednika_entry.get()
            Data_dodania = self.Data_dodania_entry.get()
            # dodaj rekord do bazy danych
            try:
                self.add_oferty_to_database(Id_Nieruchomosci,ID_Posrednika,Data_dodania)
            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
            else:
                popup_window.destroy()

        tk.Button(button_frame, text="Dodaj Oferte", command=add_oferty).grid(row=7, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Anuluj", command=popup_window.destroy).grid(row=7, column=1, padx=5, pady=5)
        popup_window.protocol("WM_DELETE_WINDOW", popup_window.destroy)
    def add_oferty_to_database(self,Id_Nieruchomosci,ID_Posrednika,Data_dodania):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Oferty (Id_Nieruchomosci,ID_Posrednika,Data_dodania) VALUES (%s, %s, %s)"
        val = (Id_Nieruchomosci,ID_Posrednika,Data_dodania)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()

    def Add_Posrednicy(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Posrednika")
        quarter_screen_width = 400
        quarter_screen_height = 200
        popup_window.transient(self.root)
        popup_window.grab_set()

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Imię:").grid(row=0, column=0, padx=5, pady=5)
        self.imie_entry = tk.Entry(frame)
        self.imie_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Nazwisko:").grid(row=1, column=0, padx=5, pady=5)
        self.nazwisko_entry = tk.Entry(frame)
        self.nazwisko_entry.grid(row=1, column=1, padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Numer telefonu: ").grid(row=2, column=0, padx=5, pady=5)
        self.numer_telefonu_entry = tk.Entry(frame)
        self.numer_telefonu_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Adres email: ").grid(row=3, column=0, padx=5, pady=5)
        self.adres_email_entry = tk.Entry(frame)
        self.adres_email_entry.grid(row=3, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        def add_posrednik():
            # pobierz wartości z pól tekstowych
            imie =  self.imie_entry.get()
            nazwisko =  self.nazwisko_entry.get()
            numer_telefonu = self.numer_telefonu_entry.get()
            adres_email = self.adres_email_entry.get()
            # dodaj rekord do bazy danych
            try:
                self.add_posrednik_to_database(imie, nazwisko,numer_telefonu, adres_email)
            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
            else:
                popup_window.destroy()

        tk.Button(button_frame, text="Dodaj Posrednika", command=add_posrednik).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Anuluj", command=popup_window.destroy).grid(row=6, column=1, padx=5, pady=5)
        popup_window.protocol("WM_DELETE_WINDOW", popup_window.destroy)
    def add_posrednik_to_database(self,imie, nazwisko,numer_telefonu,adres_email):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Posrednicy(Imie,Nazwisko,Numer_telefonu,Adres_email) VALUES (%s, %s, %s,%s)"
        val = (imie, nazwisko,numer_telefonu,adres_email)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()

    def Add_Transakcje(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Transakcje")
        quarter_screen_width = 400
        quarter_screen_height = 200
        popup_window.transient(self.root)
        popup_window.grab_set()

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="ID Umowy:").grid(row=0, column=0, padx=5, pady=5)
        self.ID_Umowy_entry = tk.Entry(frame)
        self.ID_Umowy_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="ID Posrednika:").grid(row=1, column=0, padx=5, pady=5)
        self.ID_Posrednika_entry = tk.Entry(frame)
        self.ID_Posrednika_entry.grid(row=1, column=1, padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Kwota transakcji: ").grid(row=2, column=0, padx=5, pady=5)
        self.Kwota_transakcji_entry = tk.Entry(frame)
        self.Kwota_transakcji_entry.grid(row=2, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        def add_transakcja():
            # pobierz wartości z pól tekstowych
            ID_Umowy =  self.ID_Umowy_entry.get()
            ID_Posrednika = self.ID_Posrednika_entry.get()
            Kwota_transakcji = self.Kwota_transakcji_entry.get()
            # dodaj rekord do bazy danych
            try:
                self.add_transakcja_to_database(ID_Umowy,ID_Posrednika,Kwota_transakcji)
            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
            else:
                popup_window.destroy()

        tk.Button(button_frame, text="Dodaj Transakcje", command=add_transakcja).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Anuluj", command=popup_window.destroy).grid(row=6, column=1, padx=5, pady=5)
        popup_window.protocol("WM_DELETE_WINDOW", popup_window.destroy)
    def add_transakcja_to_database(self,ID_Umowy,ID_Posrednika,Kwota_transakcji):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Transakcje (ID_Umowy,ID_Posrednika,Kwota_transakcji) VALUES (%s, %s, %s)"
        val = (ID_Umowy,ID_Posrednika,Kwota_transakcji)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()

    def Add_Typy_nieruchomosci(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Typ nieruchomosci")
        quarter_screen_width = 400
        quarter_screen_height = 150
        popup_window.transient(self.root)
        popup_window.grab_set()

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Nazwa:").grid(row=0, column=0, padx=5, pady=5)
        self.nazwa_entry = tk.Entry(frame)
        self.nazwa_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Opis:").grid(row=1, column=0, padx=5, pady=5)
        self.opis_entry = tk.Entry(frame)
        self.opis_entry.grid(row=1, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        def add_typ_nieruchomosci():
            # pobierz wartości z pól tekstowych
            nazwa = self.nazwa_entry.get()
            opis = self.opis_entry.get()
            # dodaj rekord do bazy danych
            try:
                self.add_typy_nieruchomosci_to_database(nazwa,opis)
            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
            else:
                popup_window.destroy()

        tk.Button(button_frame, text="Dodaj Typ nieruchomosci", command=add_typ_nieruchomosci).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Anuluj", command=popup_window.destroy).grid(row=6, column=1, padx=5, pady=5)
        popup_window.protocol("WM_DELETE_WINDOW", popup_window.destroy)
    def add_typy_nieruchomosci_to_database(self,nazwa,opis):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Typy_nieruchomosci (nazwa,opis) VALUES (%s, %s)"
        val = (nazwa,opis)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()

    def Add_Umowy(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Umowe")
        quarter_screen_width = 400
        quarter_screen_height = 280
        popup_window.transient(self.root)
        popup_window.grab_set()

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height) / 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Data zawarcia:").grid(row=0, column=0, padx=5, pady=5)
        self.Data_zawarcia_entry = tk.Entry(frame)
        self.Data_zawarcia_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Data podpisania:").grid(row=1, column=0, padx=5, pady=5)
        self.Data_podpisania_entry = tk.Entry(frame)
        self.Data_podpisania_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="ID nieruchomosci:").grid(row=2, column=0, padx=5, pady=5)
        self.ID_nieruchomosci_entry = tk.Entry(frame)
        self.ID_nieruchomosci_entry.grid(row=2, column=1, padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="ID klienta: ").grid(row=3, column=0, padx=5, pady=5)
        self.ID_klienta_entry = tk.Entry(frame)
        self.ID_klienta_entry.grid(row=3, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        def add_umowa():
            # pobierz wartości z pól tekstowych
            Data_zawarcia =  self.Data_zawarcia_entry.get()
            Data_podpisania =  self.Data_podpisania_entry.get()
            ID_nieruchomosci = self.ID_nieruchomosci_entry .get()
            ID_klienta = self.ID_klienta_entry.get()
            # dodaj rekord do bazy danych
            try:
                self.add_umowa_to_database(Data_zawarcia,Data_podpisania,ID_nieruchomosci,ID_klienta)
            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
            else:
                popup_window.destroy()

        tk.Button(button_frame, text="Dodaj Umowe", command=add_umowa).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Anuluj", command=popup_window.destroy).grid(row=6, column=1, padx=5, pady=5)
        popup_window.protocol("WM_DELETE_WINDOW", popup_window.destroy)
    def add_umowa_to_database(self,Data_zawarcia,Data_podpisania,ID_nieruchomosci,ID_klienta):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Umowy (Data_zawarcia,Data_podpisania,ID_nieruchomosci,ID_klienta) VALUES (%s, %s, %s,%s)"
        val = (Data_zawarcia,Data_podpisania,ID_nieruchomosci,ID_klienta)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()

    def Add_subtab(self, option):
        if option == "Klienci":
            self.Add_Klienci()
        if option == "Nieruchomosci":
            self.Add_Nieruchomosci()
        if option == "Oferty":
            self.Add_Oferty()
        if option == "Posrednicy":
            self.Add_Posrednicy()
        if option == "Transakcje":
            self.Add_Transakcje()
        if option == "Typy_nieruchomosci":
            self.Add_Typy_nieruchomosci()
        if option == "Umowy":
            self.Add_Umowy()

