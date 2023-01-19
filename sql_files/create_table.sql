-- 1. создание структуры базы данных (таблицы):
CREATE TABLE IF NOT EXISTS Hogwarts_staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(80) UNIQUE NOT NULL
    );

CREATE TABLE IF NOT EXISTS Telephone_number (
    phone_number BIGINT UNIQUE NOT NULL,
    staff_id INTEGER REFERENCES Hogwarts_staff(staff_id)
    );
