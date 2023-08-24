from flask import Flask, render_template, request, jsonify
from models import create_table,add_todo, get_todos,delete_todo,update_todo


create_table()

app = Flask(__name__)







'''@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)'''

'''@app.route('/add_todo', methods=['POST'])
def add_todo():
    new_todo = request.form.get('todo')
    todo_list.append(new_todo)
    return jsonify(message='Todo added successfully')'''
 
@app.route('/')
def index():
    todos = get_todos()  # Fetch the to-do items from the database
    return render_template('index.html', todos=todos) 
   


@app.route('/add_todo', methods=['POST'])
def add_todo_route():
    new_todo = request.form.get('todo')
    add_todo(new_todo)  # Pass the new_todo argument to the function
    return jsonify(message='Todo added successfully')




@app.route('/delete_todo', methods=['POST'])
def delete_todo_route():
    todo_to_delete = request.form.get('todo')
    delete_todo(todo_to_delete)  # Use the delete_todo function from models.py
    return jsonify(message='Todo deleted successfully')



@app.route('/update_todo', methods=['POST'])
def update_todo_route():
    old_todo = request.form.get('old_todo')
    new_todo = request.form.get('new_todo')
    update_todo(old_todo, new_todo)  # Use the update_todo function from models.py
    return jsonify(message='Todo updated successfully')


if __name__ == '__main__':
    app.run(debug=False)