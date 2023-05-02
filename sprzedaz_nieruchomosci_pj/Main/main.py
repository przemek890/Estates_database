import DataBase.Tab_info as info
import DataBase.Add_rec as add
import DataBase.Database_connect as db
import Window.window as wind
from tkinter import ttk





if __name__ == "__main__":
    connect = db.Database_Connect()                                      # Połączenie z baza
    window = wind.Window()                                                 # Tworzenie okna

    notebook = ttk.Notebook(window.root)                              # Notebook - zakładki
    info.Informacje_o_tabelach(window.root,connect.cursor,notebook)        # Zakładka nr_1
    add.Dodaj_rekord(window.root,connect.cursor,notebook)
    window.root.mainloop()  # Pętla główna

