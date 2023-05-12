import mysql.connector
from pymongo import MongoClient
"""Połączenie z baza danych SQL"""
class Database_Connect:
    def __init__(self):
        try:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("0. Upewnij się że serwer bazodanowy MariaDB jest włączony")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
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

class Database_Mongo_Connect:
    def __init__(self):
        try:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("1. Upewnij się że twój obecny adres IP dodany jest do listy adresów z których możesz połączyć sie do bazy MongoDB")
            print("W razie problemów z połączaniem - sprawdz swoje ustawienia na stronie: https://cloud.mongodb.com/ i/lub w MongoDB Compass")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
            self.client = MongoClient("mongodb+srv://przemekjan:ZVPlpLyCkQCo8Imw@sprzedaznieruchomoscipj.hfvvwe1.mongodb.net/")
            self.database = self.client["sprzedaz_nieruchomosci_pj"]
            self.collection = self.database["obsługa_systemu"]

        except Exception as e:
            print("Wystąpił nieznany błąd: {}".format(e))
            exit(0)