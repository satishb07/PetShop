-- Create a table to store animals
CREATE TABLE petData (
    PetID SERIAL PRIMARY KEY,
    type VARCHAR(255),
    name VARCHAR(255),
    age VARCHAR(255),
    favoriteFood VARCHAR(255),
    oldNames VARCHAR(255),
    speakCount VARCHAR(255)
);

-- Sample insert statements for cats and dogs
INSERT INTO petData (type, name, age, favoriteFood, oldNames, speakCount) VALUES ('Cat', 'Whiskers', '6', 'milk', '["A","B"]', '8');
INSERT INTO petData (type, name, age, favoriteFood, oldNames, speakCount) VALUES ('Dog', 'Bruno', '8', 'biscuit', '["C","D"]', '5');
