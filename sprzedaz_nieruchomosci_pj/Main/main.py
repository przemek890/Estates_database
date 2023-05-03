import DataBase.Tab_info as info
import DataBase.Add_rec as add
import DataBase.Database_connect as db
import Window.window as wind
from tkinter import ttk





if __name__ == "__main__":
    connect = db.Database_Connect()                                      # Połączenie z baza
    window = wind.Window()                                                 # Tworzenie okna
    notebook = ttk.Notebook(window.root)                              # Notebook - zakładki


    # Tworzenie zakladek
    tuck1 = info.Informacje_o_tabelach(window.root,connect.cursor,notebook)
    tuck2 = add.Dodaj_rekord(window.root,connect.cursor,notebook,connect.conn)

    def on_tab_selected(event):
        current_tab = event.widget.tab(event.widget.select(), "text")
        if current_tab == "Informacje o tabelach":
            tuck1.menu()
        elif current_tab == "Dodaj rekord":
            tuck2.menu()


    notebook.bind("<<NotebookTabChanged>>", on_tab_selected)

    window.root.mainloop()  # Pętla główna

