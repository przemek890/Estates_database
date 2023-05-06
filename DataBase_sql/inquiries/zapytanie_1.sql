-- Umowy zawarte pomiedzy  rokiem rrrr-mm-dd -- rrrr-mm-dd:
SELECT Concat(Klienci.Imie, ' ', Klienci.Nazwisko) as "Imie i nazwisko" , Umowy.Data_zawarcia, Typy_nieruchomosci.Opis
FROM Klienci
LEFT JOIN Umowy ON Umowy.ID_Klienta = Klienci.ID_Klienta
LEFT JOIN Nieruchomosci ON Umowy.ID_Nieruchomosci = Nieruchomosci.ID_Nieruchomosci
LEFT JOIN Typy_nieruchomosci ON Nieruchomosci.ID_Typu_nieruchomosci = Typy_nieruchomosci.ID_Typu_nieruchomosci
WHERE Umowy.Data_zawarcia BETWEEN '{}' AND '{}';