from tkinter import ttk, LEFT, BOTTOM, TOP
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
        self.tab2_submenu = None
    def menu(self):
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

            if not self.tab2_submenu:
                self.tab2_submenu_var = tk.StringVar()
                self.tab2_submenu = ttk.OptionMenu(self.tab2, self.tab2_submenu_var, "Tabele", "Klienci",
                                           "Nieruchomosci", "Oferty", "Posrednicy", "Transakcje", "Typy_nieruchomosci",
                                           "Umowy", command=self.Add_subtab)
                self.tab2_submenu.configure(width=74)
                self.tab2_submenu.pack(side=TOP, padx=100)

    def Add_Klienci(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Klienta")
        quarter_screen_width = 400
        quarter_screen_height = 285

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
        frame.pack(expand=False, fill="both", padx=5, pady=5)

        tk.Label(frame, text="DODAJ KLIENTA").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        tk.Label(frame, text="Imię:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.imie_entry = tk.Entry(frame)
        self.imie_entry.grid(row=1, column=1, padx=5, pady=5,sticky="w")

        tk.Label(frame, text="Nazwisko:").grid(row=2, column=0, padx=5, pady=5,sticky="e")
        self.nazwisko_entry = tk.Entry(frame)
        self.nazwisko_entry.grid(row=2, column=1, padx=5, pady=5,sticky="w")

        tk.Label(frame, text="Adres_zameldowania:").grid(row=3, column=0, padx=5, pady=5,sticky="e")
        self.Adres_zameldowania_entry = tk.Entry(frame)
        self.Adres_zameldowania_entry.grid(row=3, column=1, padx=5, pady=5,sticky="w")

        tk.Label(frame, text="Numer telefonu: ").grid(row=4, column=0, padx=5, pady=5,sticky="e")
        self.numer_telefonu_entry = tk.Entry(frame)
        self.numer_telefonu_entry.grid(row=4, column=1, padx=5, pady=5,sticky="w")

        tk.Label(frame, text="Adres email: ").grid(row=5, column=0, padx=5, pady=5,sticky="e")
        self.adres_email_entry = tk.Entry(frame)
        self.adres_email_entry.grid(row=5, column=1, padx=5, pady=5,sticky="w")

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        def add_client():
            try:
                imie = self.imie_entry.get()
                nazwisko = self.nazwisko_entry.get()
                Adres_zameldowania = self.adres_email_entry.get()
                numer_telefonu = self.numer_telefonu_entry.get()
                adres_email = self.adres_email_entry.get()

                self.add_client_to_database(imie, nazwisko, Adres_zameldowania, numer_telefonu, adres_email)

                messagebox.showinfo("Sukcess", f"Dodano rekord do bazy danych!\n")

                self.imie_entry.delete(0, tk.END)
                self.nazwisko_entry.delete(0, tk.END)
                self.Adres_zameldowania_entry.delete(0, tk.END)
                self.numer_telefonu_entry.delete(0, tk.END)
                self.adres_email_entry.delete(0, tk.END)

                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
                print(e)
                popup_window.destroy()

        def delete():
            info = messagebox.askyesnocancel("Sukcess",f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.imie_entry.delete(0, tk.END)
                self.nazwisko_entry.delete(0, tk.END)
                self.Adres_zameldowania_entry.delete(0, tk.END)
                self.numer_telefonu_entry.delete(0, tk.END)
                self.adres_email_entry.delete(0, tk.END)
                popup_window.destroy()
            else:
                self.empty_window()

        tk.Button(button_frame, text="Dodaj", command=add_client, width=15).grid(row=7, column=0, padx=5,pady=5, sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete, width=15).grid(row=7, column=1, padx=5,pady=5, sticky='e')
    def Add_Nieruchomosci(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Nieruchomosci")
        quarter_screen_width = 400
        quarter_screen_height = 325

        popup_window.transient(self.root)
        popup_window.overrideredirect(True)
        popup_window.attributes('-topmost', False)
        popup_window.grab_set()

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height)/ 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        tk.Label(frame, text="DODAJ NIERUCHOMOSC").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Kraj:").grid(row=1, column=0, padx=5, pady=5)
        self.Kraj_entry = tk.Entry(frame)
        self.Kraj_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Miejscowosc:").grid(row=2, column=0, padx=5, pady=5)
        self.Miejscowosc_entry = tk.Entry(frame)
        self.Miejscowosc_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Ulica:").grid(row=3, column=0, padx=5, pady=5)
        self.Ulica_entry = tk.Entry(frame)
        self.Ulica_entry.grid(row=3, column=1, padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Powierzchnia: ").grid(row=4, column=0, padx=5, pady=5)
        self.Powierzchnia_entry = tk.Entry(frame)
        self.Powierzchnia_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="Liczba pokoi: ").grid(row=5, column=0, padx=5, pady=5)
        self.Liczba_pokoi_entry = tk.Entry(frame)
        self.Liczba_pokoi_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(frame, text="ID Typu nieruchomosci").grid(row=6, column=0, padx=5, pady=5)
        self.ID_Typu_nieruchomosci_entry = tk.Entry(frame)
        self.ID_Typu_nieruchomosci_entry.grid(row=6, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        def add_nieruchomosc():
            try:
                Kraj = self.Kraj_entry.get()
                Miejscowosc = self.Miejscowosc_entry.get()
                Ulica = self.Ulica_entry.get()
                Powierzchnia = self.Powierzchnia_entry.get()
                Liczba_pokoi = self.Liczba_pokoi_entry.get()
                ID_Typu_nieruchomosci = self.ID_Typu_nieruchomosci_entry.get()

                self.add_nieruchomosc_to_database(Kraj,Miejscowosc,Ulica,Powierzchnia,Liczba_pokoi,ID_Typu_nieruchomosci)
                messagebox.showinfo("Sukcess", f"Dodano rekord do bazy danych!\n")

                self.Kraj_entry.delete(0, tk.END)
                self.Miejscowosc_entry.delete(0, tk.END)
                self.Ulica_entry.delete(0, tk.END)
                self.Powierzchnia_entry.delete(0, tk.END)
                self.Liczba_pokoi_entry.delete(0, tk.END)
                self.ID_Typu_nieruchomosci_entry.delete(0, tk.END)

                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
                print(e)
                popup_window.destroy()

        def delete():
            info = messagebox.askyesnocancel("Sukcess",f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.Kraj_entry.delete(0, tk.END)
                self.Miejscowosc_entry.delete(0, tk.END)
                self.Ulica_entry.delete(0, tk.END)
                self.Powierzchnia_entry.delete(0, tk.END)
                self.Liczba_pokoi_entry.delete(0, tk.END)
                self.ID_Typu_nieruchomosci_entry.delete(0, tk.END)
                popup_window.destroy()
            else:
                self.empty_window()

        tk.Button(button_frame, text="Dodaj", command=add_nieruchomosc,width=15).grid(row=8, column=0, padx=5, pady=10,sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete,width=15).grid(row=8, column=1, padx=5, pady=10,sticky='e')
    def Add_Oferty(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Oferty")
        quarter_screen_width = 400
        quarter_screen_height = 225
        popup_window.transient(self.root)

        popup_window.overrideredirect(True)
        popup_window.attributes('-topmost', False)
        popup_window.grab_set()

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height)/ 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        tk.Label(frame, text="DODAJ OFERTE").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Id Nieruchomosci:").grid(row=1, column=0, padx=5, pady=5)
        self.Id_Nieruchomosci_entry = tk.Entry(frame)
        self.Id_Nieruchomosci_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="ID Posrednika:").grid(row=2, column=0, padx=5, pady=5)
        self.ID_Posrednika_entry = tk.Entry(frame)
        self.ID_Posrednika_entry.grid(row=2, column=1, padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Data dodania:").grid(row=3, column=0, padx=5, pady=5)
        self.Data_dodania_entry = tk.Entry(frame)
        self.Data_dodania_entry.grid(row=3, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        def add_oferty():
            try:
                Id_Nieruchomosci = self.Id_Nieruchomosci_entry.get()
                ID_Posrednika = self.ID_Posrednika_entry.get()
                Data_dodania = self.Data_dodania_entry.get()

                self.add_oferty_to_database(Id_Nieruchomosci,ID_Posrednika,Data_dodania)
                messagebox.showinfo("Sukcess", f"Dodano rekord do bazy danych!\n")

                self.Id_Nieruchomosci_entry.delete(0, tk.END)
                self.ID_Posrednika_entry.delete(0, tk.END)
                self.Data_dodania_entry.delete(0, tk.END)

                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
                print(e)
                popup_window.destroy()

        def delete():
            info = messagebox.askyesnocancel("Sukcess",f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.Id_Nieruchomosci_entry.delete(0, tk.END)
                self.ID_Posrednika_entry.delete(0, tk.END)
                self.Data_dodania_entry.delete(0, tk.END)
                popup_window.destroy()
            else:
                self.empty_window()

        tk.Button(button_frame, text="Dodaj", command=add_oferty,width=15).grid(row=5, column=0, padx=5, pady=15,sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete,width=15).grid(row=5, column=1, padx=5, pady=15,sticky='e')
    def Add_Posrednicy(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Posrednika")
        quarter_screen_width = 400
        quarter_screen_height = 250
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

        tk.Label(frame, text="DODAJ POSREDNIKA").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Imię:").grid(row=1, column=0, padx=5, pady=5)
        self.imie_entry = tk.Entry(frame)
        self.imie_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Nazwisko:").grid(row=2, column=0, padx=5, pady=5)
        self.nazwisko_entry = tk.Entry(frame)
        self.nazwisko_entry.grid(row=2, column=1, padx=5, pady=5)

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

        def add_posrednik():
            try:
                imie = self.imie_entry.get()
                nazwisko = self.nazwisko_entry.get()
                numer_telefonu = self.numer_telefonu_entry.get()
                adres_email = self.adres_email_entry.get()

                self.add_posrednik_to_database(imie, nazwisko,numer_telefonu, adres_email)
                messagebox.showinfo("Sukcess", f"Dodano rekord do bazy danych!\n")

                self.imie_entry.delete(0, tk.END)
                self.nazwisko_entry.delete(0, tk.END)
                self.numer_telefonu_entry.delete(0, tk.END)
                self.adres_email_entry.delete(0, tk.END)

                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
                print(e)
                popup_window.destroy()

        def delete():
            info = messagebox.askyesnocancel("Sukcess",f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.imie_entry.delete(0, tk.END)
                self.nazwisko_entry.delete(0, tk.END)
                self.numer_telefonu_entry.delete(0, tk.END)
                self.adres_email_entry.delete(0, tk.END)
                popup_window.destroy()
            else:
                self.empty_window()

        tk.Button(button_frame, text="Dodaj", command=add_posrednik,width=15).grid(row=6, column=0, padx=5, pady=10,sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete,width=15).grid(row=6, column=1, padx=5, pady=10,sticky='e')
    def Add_Transakcje(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Transakcje")
        quarter_screen_width = 400
        quarter_screen_height = 225
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

        tk.Label(frame, text="DODAJ TRANSAKCJE").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="ID Umowy:").grid(row=1, column=0, padx=5, pady=5)
        self.ID_Umowy_entry = tk.Entry(frame)
        self.ID_Umowy_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="ID Posrednika:").grid(row=2, column=0, padx=5, pady=5)
        self.ID_Posrednika_entry = tk.Entry(frame)
        self.ID_Posrednika_entry.grid(row=2, column=1, padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Kwota transakcji: ").grid(row=3, column=0, padx=5, pady=5)
        self.Kwota_transakcji_entry = tk.Entry(frame)
        self.Kwota_transakcji_entry.grid(row=3, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        def add_transakcja():
            try:
                ID_Umowy = self.ID_Umowy_entry.get()
                ID_Posrednika = self.ID_Posrednika_entry.get()
                Kwota_transakcji = self.Kwota_transakcji_entry.get()

                self.add_transakcja_to_database(ID_Umowy,ID_Posrednika,Kwota_transakcji)
                messagebox.showinfo("Sukcess", f"Dodano rekord do bazy danych!\n")

                self.ID_Umowy_entry.delete(0, tk.END)
                self.ID_Posrednika_entry.delete(0, tk.END)
                self.Kwota_transakcji_entry.delete(0, tk.END)

                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
                print(e)
                popup_window.destroy()

        def delete():
            info = messagebox.askyesnocancel("Sukcess",f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.ID_Umowy_entry.delete(0, tk.END)
                self.ID_Posrednika_entry.delete(0, tk.END)
                self.Kwota_transakcji_entry.delete(0, tk.END)
                popup_window.destroy()
            else:
                self.empty_window()




        tk.Button(button_frame, text="Dodaj", command=add_transakcja,width=15).grid(row=4, column=0, padx=5, pady=10,sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete,width=15).grid(row=4, column=1, padx=5, pady=10,sticky='e')
    def Add_Typy_nieruchomosci(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Typ nieruchomosci")
        quarter_screen_width = 400
        quarter_screen_height = 175
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

        tk.Label(frame, text="DODAJ TYP NIERUCHOMOSCI").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Nazwa:").grid(row=1, column=0, padx=5, pady=5)
        self.nazwa_entry = tk.Entry(frame)
        self.nazwa_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Opis:").grid(row=2, column=0, padx=5, pady=5)
        self.opis_entry = tk.Entry(frame)
        self.opis_entry.grid(row=2, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        def add_typ_nieruchomosci():
            try:
                nazwa = self.nazwa_entry.get()
                opis = self.opis_entry.get()

                self.add_typy_nieruchomosci_to_database(nazwa, opis)
                messagebox.showinfo("Sukcess", f"Dodano rekord do bazy danych!\n")

                self.nazwa_entry.delete(0, tk.END)
                self.opis_entry.delete(0, tk.END)

                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
                print(e)
                popup_window.destroy()

        def delete():
            info = messagebox.askyesnocancel("Sukcess",f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.nazwa_entry.delete(0, tk.END)
                self.opis_entry.delete(0, tk.END)
                popup_window.destroy()
            else:
                self.empty_window()


        tk.Button(button_frame, text="Dodaj", command=add_typ_nieruchomosci,width=15).grid(row=4, column=0, padx=5, pady=10,sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete,width=15).grid(row=4, column=1, padx=5, pady=10,sticky='e')
    def Add_Umowy(self):
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Dodaj Umowe")
        quarter_screen_width = 400
        quarter_screen_height = 235
        popup_window.transient(self.root)

        popup_window.overrideredirect(True)
        popup_window.attributes('-topmost', False)
        popup_window.grab_set()

        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        x = int((screen_width - quarter_screen_width) / 2)
        y = int((screen_height - quarter_screen_height)/ 2)

        popup_window.geometry(f"{quarter_screen_width}x{quarter_screen_height}+{x}+{y}")
        popup_window.resizable(False, False)

        frame = ttk.Frame(popup_window)
        frame.pack(expand=True, fill="both", padx=5, pady=5)

        tk.Label(frame, text="DODAJ UMOWE").grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="Data zawarcia:").grid(row=1, column=0, padx=5, pady=5)
        self.Data_zawarcia_entry = tk.Entry(frame)
        self.Data_zawarcia_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Data podpisania:").grid(row=2, column=0, padx=5, pady=5)
        self.Data_podpisania_entry = tk.Entry(frame)
        self.Data_podpisania_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="ID nieruchomosci:").grid(row=3, column=0, padx=5, pady=5)
        self.ID_nieruchomosci_entry = tk.Entry(frame)
        self.ID_nieruchomosci_entry.grid(row=3, column=1, padx=5, pady=5)

        # stwórz etykiety i pola tekstowe
        tk.Label(frame, text="ID klienta: ").grid(row=4, column=0, padx=5, pady=5)
        self.ID_klienta_entry = tk.Entry(frame)
        self.ID_klienta_entry.grid(row=4, column=1, padx=5, pady=5)

        # stwórz przyciski
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        def add_umowa():
            try:
                Data_zawarcia = self.Data_zawarcia_entry.get()
                Data_podpisania = self.Data_podpisania_entry.get()
                ID_nieruchomosci = self.ID_nieruchomosci_entry.get()
                ID_klienta = self.ID_klienta_entry.get()

                self.add_umowa_to_database(Data_zawarcia, Data_podpisania, ID_nieruchomosci, ID_klienta)
                messagebox.showinfo("Sukcess", f"Dodano rekord do bazy danych!\n")

                self.Data_zawarcia_entry.delete(0, tk.END)
                self.Data_podpisania_entry.delete(0, tk.END)
                self.ID_nieruchomosci_entry.delete(0, tk.END)
                self.ID_klienta_entry.delete(0, tk.END)

                popup_window.destroy()

            except Exception as e:
                messagebox.showerror("Błąd", f"Niepoprawne dodanie rekordu do bazy danych!\n")
                print(e)
                popup_window.destroy()

        def delete():
            info = messagebox.askyesnocancel("Sukcess",f"Czy napewno chcesz zakończyć akcje?")
            if info is True:
                self.Data_zawarcia_entry.delete(0, tk.END)
                self.Data_podpisania_entry.delete(0, tk.END)
                self.ID_nieruchomosci_entry.delete(0, tk.END)
                self.ID_klienta_entry.delete(0, tk.END)
                popup_window.destroy()
            else:
                self.empty_window()

        tk.Button(button_frame, text="Dodaj", command=add_umowa,width=15).grid(row=6, column=0, padx=5, pady=5,sticky='w')
        tk.Button(button_frame, text="Zamknij", command=delete,width=15).grid(row=6, column=1, padx=5, pady=5,sticky='e')

    def Add_subtab(self, option):

        self.tab2_submenu.configure(width=74)
        self.tab2_submenu.pack(side=TOP, padx=100)

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


    def add_client_to_database(self, imie, nazwisko, Adres_zameldowania, numer_telefonu, adres_email):
        sql = "INSERT INTO Klienci (Imie,Nazwisko,Adres_Zameldowania,Numer_telefonu,Adres_email) VALUES (%s, %s, %s,%s,%s)"
        val = (imie, nazwisko, Adres_zameldowania, numer_telefonu, adres_email)
        self.cursor.execute(sql, val)
        self.root.update()

        self.conn.commit()
    def add_nieruchomosc_to_database(self, Kraj, Miejscowosc, Ulica, Powierzchnia, Liczba_pokoi, ID_Typu_nieruchomosci):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Nieruchomosci (Kraj,Miejscowosc,Ulica,Powierzchnia,Liczba_pokoi,ID_Typu_nieruchomosci) VALUES (%s, %s, %s,%s,%s,%s)"
        val = (Kraj, Miejscowosc, Ulica, Powierzchnia, Liczba_pokoi, ID_Typu_nieruchomosci)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()
    def add_oferty_to_database(self, Id_Nieruchomosci, ID_Posrednika, Data_dodania):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Oferty (Id_Nieruchomosci,ID_Posrednika,Data_dodania) VALUES (%s, %s, %s)"
        val = (Id_Nieruchomosci, ID_Posrednika, Data_dodania)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()
    def add_posrednik_to_database(self, imie, nazwisko, numer_telefonu, adres_email):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Posrednicy(Imie,Nazwisko,Numer_telefonu,Adres_email) VALUES (%s, %s, %s,%s)"
        val = (imie, nazwisko, numer_telefonu, adres_email)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()
    def add_transakcja_to_database(self, ID_Umowy, ID_Posrednika, Kwota_transakcji):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Transakcje (ID_Umowy,ID_Posrednika,Kwota_transakcji) VALUES (%s, %s, %s)"
        val = (ID_Umowy, ID_Posrednika, Kwota_transakcji)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()
    def add_typy_nieruchomosci_to_database(self, nazwa, opis):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Typy_nieruchomosci (nazwa,opis) VALUES (%s, %s)"
        val = (nazwa, opis)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()
    def add_umowa_to_database(self,Data_zawarcia,Data_podpisania,ID_nieruchomosci,ID_klienta):
        # pobranie danych od użytkownika

        # wykonanie zapytania dodającego rekord do tabeli "Klienci" w bazie danych
        sql = "INSERT INTO Umowy (Data_zawarcia,Data_podpisania,ID_nieruchomosci,ID_klienta) VALUES (%s, %s, %s,%s)"
        val = (Data_zawarcia,Data_podpisania,ID_nieruchomosci,ID_klienta)
        self.cursor.execute(sql, val)
        self.root.update()  # aktualizacja widoku

        # zatwierdzenie zmian w bazie danych
        self.conn.commit()

    def empty_window(self):
        pom = tk.Toplevel(self.root)
        pom.resizable(False, False)
        pom.destroy()