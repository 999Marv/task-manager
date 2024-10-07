class Task:
   # in memory db
    tasks = []
    next_id = 1
    
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

    @classmethod
    def create(cls, title, description):
        task_id = cls.next_id
        cls.next_id += 1
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
