import sqlite3

def add_user(username, real_name):
    sql = 'INSERT INTO users (username, real_name) VALUES (?,?)'
    query_params = (username, real_name)
    perform_insert(sql,query_params)