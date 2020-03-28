CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights 
    (origin, destination, duration) 
    VALUES ('New York', 'London', 415);

INSERT INTO flights 
    (origin, destination, duration) 
    VALUES ('Rio de Janeiro', 'Porto', 532);

INSERT INTO flights 
    (origin, destination, duration) 
    VALUES ('Porto', 'Stockholm', 365);

INSERT INTO flights 
    (origin, destination, duration) 
    VALUES ('Rio de Janeiro', 'Uppsala', 001);

INSERT INTO flights 
    (origin, destination, duration) 
    VALUES ('New York', 'London', 321);
    
INSERT INTO flights 
    (origin, destination, duration) 
    VALUES ('Tokio', 'Canada', 965);

SELECT * FROM flights;

SELECT origin, destination FROM flights;

SELECT * FROM flights WHERE id = 3;

SELECT AVG(duration) FROM flights;

SELECT COUNT(*) FROM flights WHERE origin = 'Rio de Janeiro';

SELECT * FROM flights WHERE origin LIKE '%a%';

UPDATE flights SET duration = 684 WHERE origin = 'Rio de Janeiro' AND destination = 'Uppsala';

SELECT * FROM flights ORDER BY duration ASC;

SELECT origin, COUNT(*) FROM flights GROUP BY origin;

-- Another table to make id Foreign Keys

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    code VARCHAR NOT NULL,
    name VARCHAR NOT NULL
);

CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights 
);

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Dave', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Erin', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Frank', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Grace', 6);

SELECT origin, destination, name FROM flights JOIN passengers ON 
    passengers.flight_id = flights.id;

SELECT origin, destination, name FROM flights JOIN passengers ON 
    passengers.flight_id = flights.id WHERE name = 'Alice';

SELECT origin, destination, name FROM flights LEFT JOIN passengers ON 
    passengers.flight_id = flights.id;

SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1;

SELECT * FROM flights WHERE id IN 
(
    SELECT flight_id FROM passengers GROUP BY 
    flight_id HAVING COUNT(*) > 1
);

-- Create index = CREATE INDEX name table nameTable