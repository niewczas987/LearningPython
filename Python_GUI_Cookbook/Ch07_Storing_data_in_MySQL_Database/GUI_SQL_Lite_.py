import os
import sqlite3
#database name constant
databaseName = 'tests_db.db'
class SQLite():
    def connect(self):
        # connect by unpacking dictionary credentials
        conn = sqlite3.connect(databaseName)
        # create cursor
        cursor = conn.cursor()
        return conn, cursor

    def close(self, conn, cursor):
        # close cursor and connection
        cursor.close()
        conn.close()

    def showDBs(self):
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for file in files:
            if file.endswith('.db'):
                print(file)

    def createGuiDB(self, dbName):
        try:
            sqlite_connection = sqlite3.connect(dbName)
        except sqlite3.Error as error:
            print('Error while connecting database:\n' + error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print('The SQL connection closed.')

    def dropGuiDB(self, dbName):
        if os.path.exists(dbName):
            os.remove(dbName)
        else:
            print("The file does not exist")
    def createTable(self, tableName):
        conn, cursor = self.connect()
        try:
            cursor.execute('CREATE TABLE %s(Id INTEGER);'%(tableName))
        except Exception as ex:
            print('Table not created. Exception: '+ str(ex))
        self.close(conn,cursor)

    def dropTable(self, tableName):
        conn, cursor = self.connect()
        try:
            cursor.execute('DROP TABLE %s;' % (tableName))
        except Exception as ex:
            print('Table not created. Exception: ' + str(ex))
        self.close(conn, cursor)

    def alterTable(self, oldName, newName):
        conn, cursor = self.connect()
        try:
            cursor.execute('ALTER TABLE %s RENAME TO %s;'%(oldName, newName))
        except Exception as ex:
            print('Table not altered. Exception: ' + str(ex))
        self.close(conn,cursor)

    def showTables(self):
        conn, cursor = self.connect()
        cursor.execute('''SELECT name FROM sqlite_schema
                        WHERE type='table'
                        ORDER BY name;''')
        print(cursor.fetchall())
        self.close(conn,cursor)
    def insertBooks(self, title, page, bookQuote):
        conn, cursor = self.connect()
        if title:
            cursor.execute('INSERT INTO Books(\'Book_Title\', \'Book_Page\') VALUES (\'%s\', \'%s\');'% (title, page))
            conn.commit()
        if bookQuote:
            cursor.execute('SELECT Book_ID From Books WHERE Book_Title = \'%s\';'%(title))
            book_containing = cursor.fetchall()[0][0]
            cursor.execute('INSERT INTO Quotations(\'Quotation\', \'Books_Book_Id\') VALUES (\'%s\', \'%s\');' % (bookQuote, book_containing))
            conn.commit()
        print(cursor.fetchall())
        self.showBooks()
        self.close(conn, cursor)
    def insertBooksExample(self):
        conn, cursor = self.connect()
        cursor.execute('INSERT INTO Books(\'Book_Title\', \'Book_Page\') VALUES (\'test1\', \'2137\');')
        conn.commit()
        self.showBooks()
        self.close(conn, cursor)

    def showBooks(self):
        conn, cursor = self.connect()
        cursor.execute('''SELECT * FROM Books;''')
        print(cursor.fetchall())
        self.close(conn, cursor)

    def showColumns(self,tableName):
        # connect to sqlite
        conn, cursor = self.connect()
        cursor.execute('PRAGMA table_info(%s);'%(tableName))
        print(cursor.fetchall())
        self.close(conn, cursor)

    def showData(self):
        # connect to sqlite
        conn, cursor = self.connect()
        print('Data from table BOOKS:')
        cursor.execute('SELECT * FROM Books;')
        print(cursor.fetchall())
        print('Data from table QUOTATIONS:')
        print(cursor.fetchall())
        self.close(conn,cursor)

if __name__ == '__main__':
    # Create class instance
    sqlite = SQLite()
    #sqlite.showData()
    #sqlite.createGuiDB('dupa.db')
    #sqlite.dropGuiDB('dupa.db')
    sqlite.createTable('qqq')
    sqlite.showDBs()
    sqlite.alterTable('qqq','xD')
    print('TABLES:')
    sqlite.showTables()
    print('BOOKS:')
    sqlite.showBooks()
    sqlite.dropTable('qqq')
    print('TABLES:')
    sqlite.showTables()
    print('COLUMNS')
    sqlite.showColumns('Books')
    print('INSERT BOOKS EXEMPLARY')
    sqlite.insertBooksExample()
    print('INSERT DEFINED BOOK')
    sqlite.insertBooks('dupa','123','dupadupadupa')


