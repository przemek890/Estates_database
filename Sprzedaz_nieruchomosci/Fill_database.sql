-- Nieruchmosci
INSERT INTO Nieruchomosci (Kraj, Miejscowosc, Ulica, Powierzchnia, Liczba_pokoi,ID_Nieruchomosci)
VALUES ('Polska', 'Kraków', 'Floriańska 21', 75.50, 3,1);

INSERT INTO Nieruchomosci (Kraj, Miejscowosc, Ulica, Powierzchnia, Liczba_pokoi,ID_Nieruchomosci)
VALUES ('USA', 'Los Angeles', 'Rodeo Drive 44', 250.00, 5,2);

INSERT INTO Nieruchomosci (Kraj, Miejscowosc, Ulica, Powierzchnia, Liczba_pokoi,ID_Nieruchomosci)
VALUES ('Francja', 'Paryż', 'Champs-Élysées 34', 100.00, 4,4);

INSERT INTO Nieruchomosci (Kraj, Miejscowosc, Ulica, Powierzchnia, Liczba_pokoi,ID_Nieruchomosci)
VALUES ('Polska', 'Kraków', 'Karmelicka 56', 72.5, 2,3);

INSERT INTO Nieruchomosci (Kraj, Miejscowosc, Ulica, Powierzchnia, Liczba_pokoi,ID_Nieruchomosci)
VALUES ('Polska', 'Warszawa', 'Nowy Świat 22', 120.0, 4,5);


-- Klienci
INSERT INTO Klienci (Imie, Nazwisko, Adres_Zameldowania, Numer_telefonu, Adres_email)
VALUES ('Anna', 'Kowalska', 'Nowa 1, 31-500 Kraków', '123 456 789', 'anna.kowalska@example.com');

INSERT INTO Klienci (Imie, Nazwisko, Adres_Zameldowania, Numer_telefonu, Adres_email)
VALUES ('John', 'Doe', 'Main St. 123, 90-012 Los Angeles', '555 555 555', 'john.doe@example.com');

INSERT INTO Klienci (Imie, Nazwisko,Adres_Zameldowania, Numer_telefonu, Adres_email)
VALUES ('Marie', 'Dubois', 'Rue de Rivoli 5, 75-001 Paris', '123 456 789', 'marie.dubois@example.com');

INSERT INTO Klienci (Imie, Nazwisko, Adres_Zameldowania, Numer_telefonu, Adres_email)
VALUES ('Jan', 'Kowalski', 'Wiejska 1, 00-001 Warszawa', '555 123 456', 'jan.kowalski@example.com');

-- Posrednicy
INSERT INTO Posrednicy (Imie, Nazwisko, Numer_telefonu, Adres_email)
VALUES ('Jan', 'Kowalski', '123 456 789', 'jan.kowalski@example.com');

INSERT INTO Posrednicy (Imie, Nazwisko, Numer_telefonu, Adres_email)
VALUES ('Sarah', 'Johnson', '555 555 555', 'sarah.johnson@example.com');

INSERT INTO Posrednicy (Imie, Nazwisko, Numer_telefonu, Adres_email)
VALUES ('Jean', 'Dupont', '123 456 789', 'jean.dupont@example.com');

-- Umowy
INSERT INTO Umowy (Data_zawarcia, Data_podpisania, ID_Nieruchomosci, ID_Klienta)
VALUES ('2021-02-01', '2021-02-03', 2, 2);

INSERT INTO Umowy (Data_zawarcia, Data_podpisania, ID_Nieruchomosci, ID_Klienta)
VALUES ('2022-03-15', '2022-03-16', 3, 1);

INSERT INTO Umowy (Data_zawarcia, Data_podpisania, ID_Nieruchomosci, ID_Klienta)
VALUES ('2023-04-21', '2023-04-23', 1, 3);

INSERT INTO Umowy (Data_zawarcia, Data_podpisania, ID_Nieruchomosci, ID_Klienta)
VALUES ('2021-05-10', '2021-05-11', 4, 4);

INSERT INTO Umowy (Data_zawarcia, Data_podpisania, ID_Nieruchomosci, ID_Klienta)
VALUES ('2002-06-05', '2002-06-06', 5, 3);

-- Oferty
INSERT INTO Oferty (ID_Nieruchomosci, ID_Posrednika, Data_dodania)
VALUES (1, 1, '2022-03-01');

INSERT INTO Oferty (ID_Nieruchomosci, ID_Posrednika, Data_dodania)
VALUES (2, 1, '2022-03-02');

INSERT INTO Oferty (ID_Nieruchomosci, ID_Posrednika, Data_dodania)
VALUES (3, 2, '2022-03-03');

INSERT INTO Oferty (ID_Nieruchomosci, ID_Posrednika, Data_dodania)
VALUES (4, 2, '2022-03-04');

INSERT INTO Oferty (ID_Nieruchomosci, ID_Posrednika, Data_dodania)
VALUES (5, 3, '2022-03-05');

INSERT INTO Transakcje (ID_Umowy, ID_Posrednika, Kwota_transakcji) VALUES (1, 1, 500000.00);
INSERT INTO Transakcje (ID_Umowy, ID_Posrednika, Kwota_transakcji) VALUES (2, 2, 750000.00);
INSERT INTO Transakcje (ID_Umowy, ID_Posrednika, Kwota_transakcji) VALUES (3, 1, 400000.00);
INSERT INTO Transakcje (ID_Umowy, ID_Posrednika, Kwota_transakcji) VALUES (4, 3, 1000000.00);
INSERT INTO Transakcje (ID_Umowy, ID_Posrednika, Kwota_transakcji) VALUES (5, 2, 600000.00);


INSERT INTO Typy_nieruchomosci (Nazwa, Opis) VALUES ('Mieszkanie', 'Mieszkanie w bloku');
INSERT INTO Typy_nieruchomosci (Nazwa, Opis) VALUES ('Dom', 'Dom jednorodzinny z ogrodem');
INSERT INTO Typy_nieruchomosci (Nazwa, Opis) VALUES ('Apartament', 'Apartament w apartamentowcu');
INSERT INTO Typy_nieruchomosci (Nazwa, Opis) VALUES ('Działka budowlana', 'Działka budowlana z widokiem na jezioro');
INSERT INTO Typy_nieruchomosci (Nazwa, Opis) VALUES ('Biuro', 'Lokal biurowy w centrum miasta');

