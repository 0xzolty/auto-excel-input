CREATE TABLE produkty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nazwa VARCHAR(100),
    aktywny BOOL,
    cena DEC(10,2)
);
INSERT INTO produkty (nazwa, aktywny, cena) VALUES
('Produkt A', TRUE, 10.00),
('Produkt B', TRUE, 25.50),
('Produkt C', FALSE, 99.99),
('Produkt D', TRUE, 5.49),
('Produkt E', TRUE, 199.00);
