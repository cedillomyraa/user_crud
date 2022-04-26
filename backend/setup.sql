--Create a user database table
CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);
--Create a vehicle_type table
CREATE TABLE vehicle_type(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(64)
);
--Vehicle table
CREATE TABLE vehicle(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(45) NOT NULL,
    license_plate VARCHAR(45) NOT NULL,
    v_type INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (v_type) REFERENCES vehicle_type(id),
    FOREIGN KEY (owner_id) REFERENCES user(id)
);
--insert some dummy data

INSERT INTO user(
    first_name,
    last_name,
    hobbies
)VALUES (
    "Maira",
    "Quinones",
    "Eating"
);

INSERT INTO user(
    first_name,
    last_name,
    hobbies
)VALUES (
    "Anna",
    "Cedillo",
    "Painting"
);

INSERT INTO user(
    first_name,
    last_name,
    hobbies
)VALUES (
    "Yessy",
    "Rod",
    "Hiking"
);

INSERT INTO vehicle_type (description) VALUES ('Car');
INSERT INTO vehicle_type (description) VALUES ('Truck');
INSERT INTO vehicle_type (description) VALUES ('SUV');
INSERT INTO vehicle_type (description) VALUES ('Van');
INSERT INTO vehicle_type (description) VALUES ('Bicycle');

--dummy data for vehicles

INSERT INTO vehicle(
    color,
    license_plate,
    v_type,
    owner_id
)VALUES(
    "red",
    "HELLO",
    1,
    1
);

INSERT INTO vehicle(
    color,
    license_plate,
    v_type,
    owner_id
)VALUES(
    "blue",
    "HELLO2",
    2,
    2
);

INSERT INTO vehicle(
    color,
    license_plate,
    v_type,
    owner_id
)VALUES(
    "green",
    "HELLO3",
    3,
    3
);

--Joining two tables
SELECT user.last_name,
        user.first_name,
        user.hobbies,
        user.active,
        vehicle.license_plate,
        vehicle.color,
        vehicle.v_type AS vehicle_type
FROM user INNER JOIN vehicle
ON user.id = vehicle.owner_id;

--Join three tables user, vehicle and vehicle type
SELECT user.last_name,
        user.first_name,
        user.hobbies,
        user.active,
        vehicle.license_plate,
        vehicle.color,
        vehicle_type.discription
FROM user
INNER JOIN vehicle ON user.id = vehicle.user_id
INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id;

