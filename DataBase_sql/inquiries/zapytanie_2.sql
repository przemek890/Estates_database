-- Łączny koszt zakupu dla każdego klienta
SELECT CONCAT(Klienci.Imie, ' ', Klienci.Nazwisko) AS `Imię i nazwisko`, SUM(Transakcje.Kwota_transakcji) AS `Łączna cena nieruchomości`
FROM Klienci
LEFT JOIN Umowy ON Klienci.ID_Klienta = Umowy.ID_Klienta
LEFT JOIN Transakcje ON Umowy.ID_Umowy = Transakcje.ID_Umowy
GROUP BY Klienci.ID_Klienta;