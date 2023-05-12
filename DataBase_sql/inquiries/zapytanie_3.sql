-- Transakcje danego pośrednika
SELECT CONCAT(Klienci.Imie, ' ', Klienci.Nazwisko) AS Imię_i_nazwisko,
        CONCAT(Nieruchomosci.Ulica, ' ', Nieruchomosci.Miejscowosc, ' ', Nieruchomosci.Kraj) AS Adres_nieruchomosci,
        CONCAT(Posrednicy.Imie, ' ',Posrednicy.Nazwisko,' ', Posrednicy.Numer_telefonu) AS Dane_posrednika,
        Transakcje.Kwota_transakcji
    From Klienci
    LEFT JOIN Umowy ON Klienci.ID_Klienta = Umowy.ID_Klienta
    LEFT JOIN Transakcje ON Umowy.ID_Umowy = Transakcje.ID_Umowy
    LEFT JOIN Posrednicy ON Transakcje.ID_Posrednika = Posrednicy.ID_Posrednika
    LEFT JOIN Nieruchomosci ON Umowy.ID_Nieruchomosci = Nieruchomosci.ID_Nieruchomosci
    WHERE Posrednicy.Imie = '{}' AND Posrednicy.nazwisko = '{}';