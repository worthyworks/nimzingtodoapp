from flask import Flask, render_template, request, jsonify
from models import create_table,add_todo, get_todos,delete_todo,update_todo




app = Flask(__name__)
create_table(app)



@app.route('/')
def index():
    todos = get_todos(app)  # Fetch the to-do items from the database
    return render_template('index.html', todos=todos) 

@app.route('/add_todo', methods=['POST'])
def add_todo_route():
    new_todo = request.form.get('todo')
    add_todo(app, new_todo)  # Pass the 'app' argument to the function
    return jsonify(message='Todo added successfully')

@app.route('/delete_todo', methods=['POST'])
def delete_todo_route():
    todo_to_delete = request.form.get('todo')
    delete_todo(app, todo_to_delete)  # Use the delete_todo function from models.py
    return jsonify(message='Todo deleted successfully')

@app.route('/update_todo', methods=['POST'])
def update_todo_route():
    old_todo = request.form.get('old_todo')
    new_todo = request.form.get('new_todo')
    update_todo(app, old_todo, new_todo)  # Use the update_todo function from models.py
    return jsonify(message='Todo updated successfully')



if __name__ == '__main__':
    app.run(debug=False)