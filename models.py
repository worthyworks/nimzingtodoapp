import os
import sqlite3

def get_db_path(app):
    return os.path.join(app.root_path, 'todos.db')

def create_table(app):
    db_path = get_db_path(app)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)')
    connection.commit()
    connection.close()

def add_todo(app, todo):
    db_path = get_db_path(app)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO todos (content) VALUES (?)', (todo,))
    connection.commit()
    connection.close()
    






def get_todos(app):
    db_path = get_db_path(app)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    connection.close()
    return todos

def delete_todo(app, todo):
    db_path = get_db_path(app)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('DELETE FROM todos WHERE content = ?', (todo,))
    connection.commit()
    connection.close()

def update_todo(app, old_todo, new_todo):
    db_path = get_db_path(app)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('UPDATE todos SET content = ? WHERE content = ?', (new_todo, old_todo))
    connection.commit()
    connection.close()
