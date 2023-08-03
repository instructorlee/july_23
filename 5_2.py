class Todo:

    def __init__(self, data):
        self.id = data['id'],
        self.text = data['text']

        self.tasks = []
    
    def __str__(self):
        return self.text

class Task:

    def __init__(self, data):
        self.id = data['id'],
        self.description = data['description']

    def __str__(self):
        return self.description
    
todo_data = {
        "id": 3,
        "text": "first todo"
    }

todo = Todo(todo_data)

todos_data = [
    {
        "id": 3,
        "text": "first todo",

        "tasks.id": 1,
        "description": "first task"
    },

    {
        "id": 3,
        "text": "first todo",       
        
        "tasks.id": 2,
        "description": "second task"
    }
]

todo = Todo(todos_data[0])

# iterate ALL ROWS to extract child data
for item in todos_data:
    todo.tasks.append(Task({
        "id": item['tasks.id'],
        "description": item['description']
    }))

print(todo.tasks[0].description)