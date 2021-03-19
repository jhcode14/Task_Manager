"""Classes used throughout project"""
class Manager():
	"""
	In a single task:
    - Task Name
    - Task Detail(optional)
    - Date Created(self prompt)
    - Due Date(optional/required for icn)
    -- User(optional)
	"""
	def __init__(self, name, detail, date_created, due, user, catagory):
		self.name = str(name)
		self.detail = str(detail)
		self.due = str(due)
		self.user = str(user)
		self.date = str(date_created)
		self.catagory = str(catagory)

	def return_raw_info(self):
		return self.name, self.detail, self.date, self.due, self.user, self.catagory

	def return_min_info(self):
		return " | Date Created: " + self.date + " | Task Name: " + self.name

	def return_info(self):
		return "Task Name: " + self.name, "Detail: " + self.detail,\
				"Date Created: " + self.date, "Due Date: " + self.due, \
				"User: "+ self.user, "Catagory: " + self.catagory
