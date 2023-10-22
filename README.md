# PetShop Project

## Overview

The PetShop project is a Python application for managing information about pets, with two category cats and dogs. It also create the SQLite database to store information.

## File Structure

- **main.py**: Contains the `Cat`, `Dog`, and `Data` classes for working with pets and the database.
- **petShop.py**: Implements the `PetShop` class for managing pets, and logging current summary.
- **homework.sql**: SQL file with the database schema and sample insert statements.
- **test.py**: Unit tests for testing the classes.

## Getting Started

1. Make sure you have Python installed.
2. Install the `sqlite3` module for SQLite database interaction: `pip install pysqlite3`.
3. Clone or download this repository.
4. Navigate to the project directory.
5. Run the application:

To check proper implementation of requirements run:
```bash
python main.py
```
The testing.db file should be created in the working directory, which is testing database. The cat is inserted in it with data.insert() function. We can delete the database whenever we want to start from scrath. If the database is not deleted then information will be appended to it.

## PetShop Database
To check test the PetShop application and database run:
```bash
python petShop.py
```
### Save Pet
We can use saveTest() or savePetShop() functions to store the information for new pets in the office. New petShop.db file will be created which is the database for the petshop.
### Viewing Logs
The  basic logging functionality to provide insights into its operations is also included in logStats() function. You can view the logs in the terminal as the application runs. The logs will display information about connecting to the database, beginning and committing transactions, and inserting data.

## Testing Code

To run the tests:
```bash
python test.py
```
It will check the codes agains the testcases created. If we would like to test more casees, we can include them in this file.

## Why This Approach?
1. **Database Integration:** This project uses SQLite3 to showcase the integration of a database with Python. SQLite3 is a lightweight, serverless, and self-contained database engine, making it ideal for this demonstration.
2. **Unit Testing:** The implementation employs Python's built-in unittest framework, providing an efficient way to define and execute test cases for the Python application. This ensures code reliability and identifies potential issues early in development.
3. **Error Handling and Logging:** For the sake of simplicity, this project omits extensive error handling. Real-world applications would require more robust error handling and logging mechanisms.

## Future Improvements
1. **Unified Pet Class:** Instead of separate Cat and Dog classes, a single Pet class could be utilized with a type attribute to distinguish different animal types. This would simplify the codebase and enhance scalability when dealing with various animals.
2. **Inheritance for Default Sounds:** If the default sound is a key functionality, an inheritance-based approach could be adopted. A superclass Pet could define common attributes and methods, while subclasses like Cat and Dog could inherit from Pet and provide default sound implementations.
3. **Error Handling and Logging:** Real-world applications should incorporate thorough error handling and logging to ensure robustness and facilitate debugging and monitoring.
4. **Cloud Integration:** While the current project uses a local SQLite database, a future improvement could involve connecting the application to a cloud-based database service. This would enhance data accessibility, scalability, and collaboration.









