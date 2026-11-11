from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

todo = [
    {'id': 1, 'task': 'learn flask'},
    {'id': 2, 'task': 'build a project'},
    {'id': 3, 'task': 'build the app'},
]
next_id = 4

@app.route('/')
def get_todos():
    return "from the API"

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

todo = [
    {'id': 1, 'task': 'learn flask', 'done': False},
    {'id': 2, 'task': 'build a project', 'done': False},
    {'id': 3, 'task': 'build the app', 'done': False},
]
next_id = 4


def find_todo(todo_id):
    for item in todo:
        if item['id'] == todo_id:
            return item
    abort(404)


@app.route('/')
def get_todos():
    return render_template('index.html', todos=todo)


@app.route('/add', methods=['POST'])
def add_todo():
    global next_id
    task = request.form.get('task', '').strip()
    if task:
        todo.append({'id': next_id, 'task': task, 'done': False})
        next_id += 1
    return redirect(url_for('get_todos'))


@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    item = find_todo(todo_id)
    if request.method == 'POST':
        task = request.form.get('task', '').strip()
        if task:
            item['task'] = task
        return redirect(url_for('get_todos'))
    return render_template('edit.html', todo=item)


@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle_todo(todo_id):
    item = find_todo(todo_id)
    item['done'] = not item['done']
    return redirect(url_for('get_todos'))


@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    item = find_todo(todo_id)
    todo.remove(item)
    return redirect(url_for('get_todos'))


if __name__ == '__main__':
    app.run(debug=True)
    
