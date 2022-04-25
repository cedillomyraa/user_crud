--Create a user database table
CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
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