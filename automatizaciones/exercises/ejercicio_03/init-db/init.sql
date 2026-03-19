CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT
);

INSERT INTO users(name,email) VALUES
('Cristian','cristian@test.com'),
('Ana','ana@test.com'),
('Luis','luis@test.com');


CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name TEXT,
    price INT
);

INSERT INTO products(name,price) VALUES
('Laptop',3000),
('Mouse',40),
('Keyboard',120);