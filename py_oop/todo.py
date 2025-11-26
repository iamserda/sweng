class TodoList:
    def __init__(self, title):
        self.title = title
        self.items = []

    def add_item(self, description):
        new_item = TodoItem(description)
        self.items.append(new_item)
        self.display_list()

    def display_list(self):
        print(f"List Title: {self.title}:")
        for i, item in enumerate(self.items):
            print(f"\t{i + 1}. {item}")

    def complete_task(self, task_number):
        if not self.items or task_number - 1 < 0 or task_number - 1 >= len(self.items):
            return
        task = self.items[task_number - 1]
        task.mark_complete()
        self.display_list()


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


todo1 = TodoList(title="Todo List 1")
todo1.add_item("Item 1")
todo1.add_item("Item 2")
todo1.display_list()
todo1.complete_task(1)
todo1.complete_task(2)
