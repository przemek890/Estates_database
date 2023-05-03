CREATE DATABASE IF NOT EXISTS sprzedaz_nieruchomosci_pj;
USE sprzedaz_nieruchomosci_pj;
#-------------------------

-- Nieruchomości
CREATE TABLE IF NOT EXISTS Nieruchomosci (
  ID_Nieruchomosci INT AUTO_INCREMENT PRIMARY KEY,
  Kraj VARCHAR(255),
  Miejscowosc VARCHAR(255),
  Ulica VARCHAR(255),
  Powierzchnia DECIMAL(10,2),
  Liczba_pokoi INT,
  ID_Typu_nieruchomosci INT
) engine = InnoDB;

-- Klienci
CREATE TABLE IF NOT EXISTS Klienci (
  ID_Klienta INT AUTO_INCREMENT PRIMARY KEY,
  Imie VARCHAR(255),
  Nazwisko VARCHAR(255),
  Adres_Zameldowania VARCHAR(255),
  Numer_telefonu VARCHAR(20),
  Adres_email VARCHAR(255)
) engine = InnoDB;

-- Umowy
CREATE TABLE IF NOT EXISTS Umowy (
  ID_Umowy INT AUTO_INCREMENT PRIMARY KEY,
  Data_zawarcia DATE,
  Data_podpisania DATE,
  ID_Nieruchomosci INT,
  ID_Klienta INT
) engine = InnoDB;
ALTER TABLE Umowy ADD FOREIGN KEY (ID_Nieruchomosci)
    REFERENCES Nieruchomosci(ID_Nieruchomosci)
    ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE Umowy ADD FOREIGN KEY (ID_Klienta)
    REFERENCES Klienci(ID_Klienta)
    ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Posrednicy
CREATE TABLE IF NOT EXISTS Posrednicy (
  ID_Posrednika INT AUTO_INCREMENT PRIMARY KEY,
  Imie VARCHAR(255),
  Nazwisko VARCHAR(255),
  Numer_telefonu VARCHAR(20),
  Adres_email VARCHAR(255)
) engine = InnoDB;

-- Oferty
CREATE TABLE IF NOT EXISTS Oferty (
  ID_Oferty INT AUTO_INCREMENT PRIMARY KEY,
  ID_Nieruchomosci INT,
  ID_Posrednika INT,
  Data_dodania DATE
) engine = InnoDB;
ALTER TABLE Oferty ADD FOREIGN KEY (ID_Nieruchomosci)
    REFERENCES Nieruchomosci(ID_Nieruchomosci)
    ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE Oferty ADD FOREIGN KEY (ID_Posrednika)
    REFERENCES Posrednicy(ID_Posrednika)
    ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Transakcje
CREATE TABLE IF NOT EXISTS Transakcje (
ID_Transakcji INT AUTO_INCREMENT PRIMARY KEY,
ID_Umowy INT,
ID_Posrednika INT,
Kwota_transakcji DECIMAL(10,2)
) engine = InnoDB;
ALTER TABLE Transakcje ADD FOREIGN KEY (ID_Umowy)
REFERENCES Umowy(ID_Umowy)
ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE Transakcje ADD FOREIGN KEY (ID_Posrednika)
REFERENCES Posrednicy(ID_Posrednika)
ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Typy nieruchomości
CREATE TABLE IF NOT EXISTS Typy_nieruchomosci (
ID_Typu_nieruchomosci INT AUTO_INCREMENT PRIMARY KEY,
Nazwa VARCHAR(255),
Opis TEXT
) engine = InnoDB;
ALTER TABLE Nieruchomosci ADD FOREIGN KEY (ID_Typu_nieruchomosci)
REFERENCES Typy_nieruchomosci(ID_Typu_nieruchomosci)
ON DELETE RESTRICT ON UPDATE RESTRICT;




