#create dictionary to hold connection info
dbConfig = {
    'user': 'admin',
    'password':'admin',
    'host':'127.0.0.1'
}

#create connection to sqllitedb
import sqlite3
def execute_query(query='*'):
    try:
        sqlite_connection = sqlite3.connect('tests_db.db')
        print('SQL connection succesfull')
        cursor = sqlite_connection.cursor()
        cursor.execute(query)
        output = cursor.fetchall()
        cursor.close()
        return output

    except sqlite3.Error as error:
        print('Error while connecting database:\n'+error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('The SQL connection closed.')

print(execute_query('SELECT * FROM users;'))
#create table books
# execute_query('''CREATE TABLE Books (
#                         Book_ID INTEGER PRIMARY KEY ASC AUTOINCREMENT NOT NULL,
#                         Book_Title VARCHAR(25) NOT NULL
#                         ,Book_Page INTEGER NOT NULL);''')
#create table quotations
# execute_query('''CREATE TABLE Quotations (
#                         Quote_ID INTEGER,
#                         Quotation VARCHAR(250),
#                         Books_Book_ID INTEGER,
#                         FOREIGN KEY (Books_Book_ID)
#                         REFERENCES Books(Book_ID)
#                         ON DELETE CASCADE);''')