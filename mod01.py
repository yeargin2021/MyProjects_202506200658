import json
import os

# 1. To-Do List App
# Build a simple app where you can add, mark as done, and delete to-do items.
# Try making it in your favorite language or framework

class Item:
	def __init__(self, description, done=False):
		self.description = description
		self.done = done

class ToDoList:
	def __init__(self, filename='todo_list.json'):
		self.filename = filename
		self.items = []
		self.load()

	def add_item(self, description):
		item = Item(description)
		self.items.append(item)
		self.save()

	def save(self):
		with open(self.filename, 'w') as f:
			json.dump([{'description': i.description, 'done': i.done} for i in self.items], f)

	def load(self):
		if os.path.exists(self.filename):
			with open(self.filename, 'r') as f:
				data = json.load(f)
				self.items = [Item(d['description'], d['done']) for d in data]

def display_list(todo_list):
	for idx, item in enumerate(todo_list.items, 1):
		status = "[x]" if item.done else "[ ]"
		print(f"{idx}. {status} {item.description}")

def main():
	todo_list = ToDoList()
	while True:
		print("\n1. Add item")
		print("2. Mark item as done/undone")
		print("3. Delete done items")
		print("4. Display list")
		print("5. Exit")
		choice = input("Choose an option: ")
		print("")
		if choice == "1":
			desc = input("Enter description: ")
			todo_list.add_item(desc)
		elif choice == "2":
			display_list(todo_list)
			idx = int(input("Enter item number to toggle: ")) - 1
			if 0 <= idx < len(todo_list.items):
				todo_list.items[idx].done = not todo_list.items[idx].done
				todo_list.save()
		elif choice == "3":
			todo_list.items = [item for item in todo_list.items if not item.done]
			todo_list.save()
		elif choice == "4":
			display_list(todo_list)
		elif choice == "5":
			break
		else:
			print("Invalid option.")

if __name__ == "__main__":
	main()
	# Add a line space after the item is selected for better readability
	print()