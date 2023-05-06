import mysql.connector
"""Połączenie z baza danych"""
class Database_Connect:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                port="3306",
                user="root",
                database="sprzedaz_nieruchomosci_pj"
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as error:
            print("Błąd połączenia z bazą danych: {}".format(error))
            exit(0)
        except Exception as e:
            print("Wystąpił nieznany błąd: {}".format(e))
            exit(0)