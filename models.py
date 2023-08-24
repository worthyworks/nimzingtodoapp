import sqlite3

def create_table():
    connection = sqlite3.connect('todos.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)')
    connection.commit()
    connection.close()
    



def add_todo(todo):
    connection = sqlite3.connect('todos.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO todos (content) VALUES (?)', (todo,))
    connection.commit()
    connection.close()


def get_todos():
    connection = sqlite3.connect('todos.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    connection.close()
    return todos




def delete_todo(todo):
    connection = sqlite3.connect('todos.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM todos WHERE content = ?', (todo,))
    connection.commit()
    connection.close()

def update_todo(old_todo, new_todo):
    connection = sqlite3.connect('todos.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE todos SET content = ? WHERE content = ?', (new_todo, old_todo))
    connection.commit()
    connection.close()
