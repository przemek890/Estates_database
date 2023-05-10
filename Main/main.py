import DataBase_file.Tab_info as info
import DataBase_file.Add_rec as add
import DataBase_file.Rem_rec as rem
import DataBase_file.Database_connect as db
import DataBase_file.Inquiries as  iq
import Window.window as wind
import DataBase_file.MongoDB as sb
from tkinter import ttk


if __name__ == "__main__":
    connect = db.Database_Connect()                                  # Połączenie z baza SQL
    connect_mn = db.Database_Mongo_Connect()                         # Połączene z baza Mongodb
    window = wind.Window()                                           # Tworzenie okna
    notebook = ttk.Notebook(window.root)                             # Notebook - zakładki

    # Tworzenie zakladek
    tuck1 = info.Informacje_o_tabelach(window.root,connect.cursor,notebook)
    tuck2 = add.Dodaj_rekord(window.root,connect.cursor,notebook,connect.conn)
    tuck3 = rem.Usun_rekord(window.root,connect.cursor,notebook,connect.conn)
    tuck4 = iq.Inquiries(window.root,connect.cursor,notebook,connect.conn)
    tuck5 = sb.Mongo_DB(window.root,notebook,connect_mn)

    def on_tab_selected(event):
        current_tab = event.widget.tab(event.widget.select(), "text")
        if current_tab == "Informacje o tabelach":
            tuck1.menu()
        elif current_tab == "Dodaj rekord":
            tuck2.menu()
        elif current_tab == "Usun rekord":
            tuck3.menu()
        elif current_tab == "Wybrane zapytania":
            tuck4.menu()
        elif current_tab == "MongoDB":
            tuck5.menu()

    notebook.bind("<<NotebookTabChanged>>", on_tab_selected)

    window.root.mainloop()  # Pętla główna

