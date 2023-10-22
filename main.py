import os
import random
import sqlite3

class Cat:
    def __init__(self, name=""):
        self.type = "Cat"
        self.name = name
        self.age = random.randint(5, 10)
        self.favoriteFood = None
        self.oldNames = [] #Excluded the current name, if we need to include it we can modify.
        self.speakCount = 0
    
    def getName(self):
        return self.name
    
    def getNames(self):
        return self.oldNames
    
    def getAge(self):
        return self.age
    
    def getFavoriteFood(self):
        return self.favoriteFood
    
    def setName(self, name):
        if self.name: self.oldNames.append(self.name)
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    def setFavoriteFood(self, favoriteFood):
        self.favoriteFood = favoriteFood

    def speak(self, sound="meow"):
        print(sound)
        
        self.speakCount += 1
        if self.speakCount % 5 == 0:
            self.age += 1
    
    def getAverageNameLength(self):
        if not self.oldNames: return 0
        nameLengths = [len(i) for i in self.oldNames]
        return sum(nameLengths)/len(nameLengths)

class Dog:
    def __init__(self, name=""):
        self.type = "Dog"
        self.name = name
        self.age = random.randint(5, 10)
        self.favoriteFood = None
        self.oldNames = [] #Excluded the current name, if we need to include it we can modify.
        self.speakCount = 0
    
    def getName(self):
        return self.name
    
    def getNames(self):
        return self.oldNames
    
    def getAge(self):
        return self.age
    
    def getFavoriteFood(self):
        return self.favoriteFood
    
    def setName(self, name):
        if self.name: self.oldNames.append(self.name)
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    def setFavoriteFood(self, favoriteFood):
        self.favoriteFood = favoriteFood

    def speak(self, sound="bark"):
        print(sound)
        
        self.speakCount += 1
        if self.speakCount % 5 == 0:
            self.age += 1
    
    def getAverageNameLength(self):
        if not self.oldNames: return 0
        nameLengths = [len(i) for i in self.oldNames]
        return sum(nameLengths)/len(nameLengths)

class Data:
    def __init__(self, name):
        print ("Connecting to database")
        self.dataBase = name + ".db"

        # Create SQLite database if not present
        if not os.path.exists(self.dataBase): os.system("sqlite3 " + self.dataBase + " < homework.sql")

        # Connect to the SQLite database
        self.conn = sqlite3.connect(self.dataBase)
        self.cursor = self.conn.cursor()
    
    def insert(self, pet):
        print ("Inserting " + pet.getName() + " into table " + self.dataBase)
        self.cursor.execute("INSERT INTO petData (type, name, age, favoriteFood, oldNames, speakCount) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(pet.type, pet.name, pet.age, pet.favoriteFood, pet.oldNames, pet.speakCount))
        self.conn.commit()

    def beginTran(self, object):
        print ("Beginning a transaction")
    
    def commit(self, object):
        print ("Committing transaction")
    
    def rollback(self, object):
        print ("Rolling back transaction")
        
if __name__ == "__main__":
    cat = Cat()
    print("Name is currently " + str(cat.getName()))

    cat.setName("Garfield")
    print("Name has been changed to " + str(cat.getName()))

    data = Data("testing")

    data.insert(cat)