CREATE TABLE IF NOT EXISTS fiis (
    id SERIAL4 PRIMARY KEY,
    name TEXT
);
CREATE TABLE IF NOT EXISTS dividends (
    id SERIAL4 PRIMARY KEY,
    dividend DECIMAL(12, 5),
    net_worth DECIMAL(12, 5),
    reference_date DATE,
    document_id INT4,
    fii INT4,
    FOREIGN KEY (fii) REFERENCES fiis(id)
);
CREATE TABLE IF NOT EXISTS quotes (
    id SERIAL4 PRIMARY KEY,
    reference_date DATE,
    fii INT4,
    FOREIGN KEY (fii) REFERENCES fiis(id)
);