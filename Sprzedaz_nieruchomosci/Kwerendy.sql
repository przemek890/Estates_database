-- Klienci
SELECT * FROM Klienci;

-- Nieruchomosci
SELECT * FROM Nieruchomosci;

-- Klienci o nazwisku na literę D
SELECT * FROM Klienci WHERE Klienci.Nazwisko LIKE 'D%';

-- Nieruchomosci o powierzchni powyżej 100 m^2
SELECT * FROM Nieruchomosci WHERE Powierzchnia > 100;

-- Umowy zawarte pomiedzy  rokiem 2021-2022
SELECT  Klienci.Imie, Klienci.Nazwisko,Umowy.Data_zawarcia,Oferty.Opis_oferty
FROM Umowy
JOIN Klienci ON Umowy.ID_Klienta = Klienci.ID_Klienta
JOIN Oferty ON Umowy.ID_Umowy = Oferty.ID_Oferty
JOIN Nieruchomosci ON Oferty.ID_Nieruchomosci = Nieruchomosci.ID_Nieruchomosci
WHERE Umowy.Data_zawarcia BETWEEN '2021-01-01' AND '2021-12-31';


-- Łączny koszt zakupu dla każdego klienta
SELECT CONCAT(Klienci.Imie, ' ', Klienci.Nazwisko) AS `Imię i nazwisko`, SUM(Oferty.Cena_oferty) AS `Łączna cena nieruchomości`
FROM Klienci
INNER JOIN Umowy ON Klienci.ID_Klienta = Umowy.ID_Klienta
INNER JOIN Nieruchomosci ON Umowy.ID_Nieruchomosci = Nieruchomosci.ID_Nieruchomosci
INNER JOIN Oferty ON Nieruchomosci.ID_Nieruchomosci = Oferty.ID_Nieruchomosci
GROUP BY Klienci.ID_Klienta;

-- Podstawowe informacje o Sprzedazy
SELECT CONCAT(Klienci.Imie, ' ', Klienci.Nazwisko) AS Imię_i_nazwisko,
       CONCAT(Nieruchomosci.Ulica, ' ', Nieruchomosci.Miejscowosc, ' ', Nieruchomosci.Kraj) AS Adres_nieruchomosci,
       CONCAT(Posrednicy.Imie, ' ',Posrednicy.Nazwisko,' ', Posrednicy.Numer_telefonu) AS Dane_posrednika,
       Oferty.Cena_oferty
FROM Nieruchomosci
INNER JOIN Oferty ON Nieruchomosci.ID_Nieruchomosci = Oferty.ID_Nieruchomosci
INNER JOIN Posrednicy ON Oferty.ID_Posrednika = Posrednicy.ID_Posrednika
INNER JOIN Umowy ON Oferty.ID_Nieruchomosci = Umowy.ID_Nieruchomosci
INNER JOIN Klienci ON Umowy.ID_Klienta = Klienci.ID_Klienta;

-- Klienci których posrednikiem była Sarah Johnson
DELIMITER $
CREATE PROCEDURE posrednik(IN v_imie VARCHAR(255), IN v_nazwisko VARCHAR(255))
BEGIN
    SELECT CONCAT(Klienci.Imie, ' ', Klienci.Nazwisko) AS Imię_i_nazwisko,
           CONCAT(Nieruchomosci.Ulica, ' ', Nieruchomosci.Miejscowosc, ' ', Nieruchomosci.Kraj) AS Adres_nieruchomosci,
           CONCAT(Posrednicy.Imie, ' ',Posrednicy.Nazwisko,' ', Posrednicy.Numer_telefonu) AS Dane_posrednika,
           Oferty.Cena_oferty
    FROM Nieruchomosci
    INNER JOIN Oferty ON Nieruchomosci.ID_Nieruchomosci = Oferty.ID_Nieruchomosci
    INNER JOIN Posrednicy ON Oferty.ID_Posrednika = Posrednicy.ID_Posrednika
    INNER JOIN Umowy ON Oferty.ID_Nieruchomosci = Umowy.ID_Nieruchomosci
    INNER JOIN Klienci ON Umowy.ID_Klienta = Klienci.ID_Klienta
    WHERE Posrednicy.Imie = v_imie AND Posrednicy.nazwisko = v_nazwisko;
END $
DELIMITER ;

CALL posrednik('Sarah','Johnson');




