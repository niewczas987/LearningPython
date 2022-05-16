import sqlite3

database = sqlite3.connect('tests_db.db')
cursor = database.cursor()
create_user_sql = "CREATE TABLE users (username TEXT, password TEXT)"
cursor.execute(create_user_sql)

database.commit()
database.close()