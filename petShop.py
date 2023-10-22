from main import *

def saveTest(data):
    # Create a cat with a name and insert it into the database
    cat = Cat("Whiskers")
    data.insert(cat)

    # Create a dog with a name and insert it into the database
    dog = Dog("Bruno")
    data.insert(dog)

def savePetShop(data):
    # Create three nameless cats
    cats = [Cat() for _ in range(3)]

    # Create three nameless dogs
    dogs = [Dog() for _ in range(3)]

    # Insert all six pets into the database
    for cat in cats: data.insert(cat)
    for dog in dogs: data.insert(dog)

def logStats(data):
    print("Logging statistics:")

    # Execute a SQL query to retrieve summary data from the database
    query = "SELECT COUNT(*) AS totalPets, AVG(age) AS avgAge FROM petData"
    data.cursor.execute(query)
    result = data.cursor.fetchone()  # Fetch the result
    
    if result:
        totalPets, avgAge = result
        print(f"Total pets in the database: {totalPets}")
        print(f"Average age of pets: {round(avgAge)}")
    else:
        print("No data found in the database.")

if __name__ == "__main__":
    data = Data("petShop")
    saveTest(data)
    savePetShop(data)
    logStats(data)