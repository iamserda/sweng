class TodoList:
    def __init__(self, title:str):
        self.title:str = title
        self.items:list[TodoItem] = []
    
    def __str__(self):
        return f"\nTodoList: {self.title}, Item Count: {len(self.items)}"

    def is_valid_task(self, task_number:int)->bool:
        if not self.items or task_number - 1 < 0 or task_number - 1 >= len(self.items):
            return False
        return True
    
    def create_task(self, description:str)->None:
        new_item = TodoItem(description)
        self.items.append(new_item)
        self.show_tasks_list()

    def show_tasks_list(self):
        print(f"\nList Title: {self.title}:")
        for i, item in enumerate(self.items):
            print(f"\t{i + 1}. {item}")

    def complete_task(self, task_number):
        if self.is_valid_task(task_number):
            task = self.items[task_number - 1]
            task.mark_complete()
            self.show_tasks_list()
    
    def delete_task(self, task_number):
        if self.is_valid_task(task_number):
            del self.item[task_number - 1]

    def update_task(self, task_number:int, new_description:str)->None:
        if self.is_valid_task(task_number):
            task:TodoItem = self.items[task_number - 1]
            task.update_description(new_description)
        self.show_tasks_list()


class TodoItem:
    def __init__(self, description):
        self.completed = False
        self.checkboxes = ["☑️", "✅"]
        self.description = description

    def __str__(self):
        return f"{self.checkboxes[1] if self.completed else self.checkboxes[0]} {self.description}"

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def undo_redo(self):
        self.completed = not self.completed

    def update_description(self, new_description):
        if new_description:
            self.description = new_description

todo1 = TodoList(title="Todo List 1")
print(todo1)
for i in range(9):
    todo1.create_task(f"Item {i+1}")

print(todo1)
todo1.show_tasks_list()
todo1.complete_task(0)
todo1.complete_task(1)
todo1.complete_task(2)
todo1.complete_task(3)
todo1.update_task(1, "Random acts of kindness.")
