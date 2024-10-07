class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

# in memory db
tasks = []

@classmethod
def create(cls, title, description):
    task_id = len(cls.tasks) + 1
    new_task = cls(task_id, title, description)
    cls.tasks.append(new_task)
    return new_task

@classmethod
def find(cls, task_id):
    return next((task for task in cls.tasks if task.id == task_id), None)

@classmethod
def delete(cls, task_id):
    cls.tasks = [task for task in cls.tasks if task.id != task_id]

@classmethod
def all(cls):
    return cls.tasks

