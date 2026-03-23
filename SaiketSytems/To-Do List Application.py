# ============================ To-Do List Application ============================
print("........... [WELCOME] ......................................................")
print("📋 ===================== To-Do List Application ================== 📋")
print("..................................................... [WELCOME] ............")


class Task:
    def __init__(self, taskName, priority="medium"):
        self.taskName = taskName
        self.priority = priority
        self.completed = False
        
    def toggle(self):
        self.completed = not self.completed
        
    def __str__(self):
        status = "✅" if self.completed else "⭕"
        return f"[{status}] ({self.priority.upper()}) {self.taskName}"
    
class ToDoList:
    def __init__(self):
        self.tasks = []
        
    def _get_task(self, index):
        if 1 <= index <= len(self.tasks):
            return self.tasks[index - 1]
        print("⚠️ Invalid task index.")
        return None
    
    def displayAllTasks(self):
        if not self.tasks:
            print("📭 No Tasks Present In List !! Add Some...")
            return
        print("📋 Your To-Do List:")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")
        
        
    def addingTask(self, taskName, priority="Medium"):
        if priority not in ("Less", "Medium", "Top"):
            print("⚠️ Invalid priority. ===> Choose from: 🔻 Less,🔹 Medium, 🔺 Top. < ====")
            return
        task = Task(taskName, priority)
        self.tasks.append(task)
        print(f"✅ Task {taskName} Added Successfully")
        
    def StatusMarking(self, index):
        task = self._get_task(index)
        if task:
            task.toggle()
            state = "Done" if task.completed else "Pending"
            print(f"✅ Task marked as {state} Successfully.")
            
    def deletingTask(self, index):
        task = self._get_task(index)
        if task:
            self.tasks.pop(index - 1)
            print(f"🚮 Task {task.taskName} Deleted Successfully.")
            
    def clear_all_completed_tasks(self):
        selected_tasks = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        removed_tasks = selected_tasks - len(self.tasks)
        print(f"🧹 Cleared Successfully All Completed Tasks: {removed_tasks}.")
        
    def _filter(self, filter_by):
        if filter_by == "all":
            return self.tasks
        elif filter_by == "done":
            return [t for t in self.tasks if t.completed]
        elif filter_by == "pending":
            return [t for t in self.tasks if not t.completed]
        elif filter_by == "top":
            return [t for t in self.tasks if t.priority.lower() == "top"]
        elif filter_by == "medium":
            return [t for t in self.tasks if t.priority.lower() == "medium"]
        elif filter_by == "less":
            return [t for t in self.tasks if t.priority.lower() == "less"]
        else:
            return []
        
    def filteringTasks(self, filter_by):
        filtered = self._filter(filter_by)
        if filter_by == "all":
            return "\n📋 All Tasks: \n" + "\n".join(f"{idx}. {task}" for idx, task in enumerate(filtered, 1))
        elif filter_by in ("pending", "done"):
            return f"\n📋 Tasks: {filter_by.upper()} \n" + "\n".join(f"{idx}. {task}" for idx, task in enumerate(filtered, 1))
        elif filter_by in ("high", "medium", "low"):
            return f"\n📋 Tasks: {filter_by.upper()} \n" + "\n".join(f"{idx}. {task}" for idx, task in enumerate(filtered, 1))
        else:
            return "⚠️ Invalid filter. Choose from: all, pending, done, high, medium, low."
        
#! ============================================================= CLI MENU =============================================================
todo_list = ToDoList()
todo_list.addingTask("Buy groceries", priority="Top")

while True:
    print("""
+++++++++++++++++++++++++++++++++++++++++
++     MY TO-DO LIST APPLICATION       ++
+++++++++++++++++++++++++++++++++++++++++
++ 1. 👁️  View All Tasks               ++
++ 2. ➕ Add New Task                 ++
++ 3. ❓ Mark Task as Done/Pending    ++
++ 4. 🗑️  Delete Task                  ++
++ 5. 🧹 Clear All Completed Tasks    ++
++ 6. 🧲 Filter Tasks                 ++
++ 7. 🚀 Exit                         ++
+++++++++++++++++++++++++++++++++++++++++  
    """)
    choice = input("Enter your choice (1-7): ").strip()
   
    
    if choice == "1":
        todo_list.displayAllTasks()
    elif choice == "2":
        name = input("Enter task name: ").strip()
        priority = input("Enter priority (Less, Medium, Top): ").strip()
        todo_list.addingTask(name, priority)
    elif choice == "3":
        index = int(input("Enter task index to mark status: "))
        todo_list.StatusMarking(index)
    elif choice == "4":
        index = int(input("Enter task index to delete task: "))
        todo_list.deletingTask(index)
    elif choice == "5":
        todo_list.clear_all_completed_tasks()
    elif choice == "6":
        filter_by = input("Filter by (all, pending, done, high, medium, low): ").strip().lower()
        print(todo_list.filteringTasks(filter_by))
    elif choice == "7":
        print("🚀 Exiting To-Do List Application. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please enter a number between 1 and 7.")
        

