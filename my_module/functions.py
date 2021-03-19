"""A collection of function for doing my project."""
from datetime import datetime as dt

# For my_script.py, MUST comment/hide when running test_function.py
from my_module.classes import Manager

# For test_function.py, MUST comment/hide when running my_script.py
#from classes import Manager

import os

def create_task():
	"""
	Function create_task():

	Description: Prompt the user simple print and input questions,
	containing task name, detail, due date(optional), user (optional)
	, and catagory (optional). The info recorded will be processed to
	form a Manager type data.

	In-take Variables: n/a
	Returned Variable: new_task (in the format of Manager class)
	"""
	print("Please enter the task info")

	input_name = input('|ENTER Task Name|: ')
	while not input_name:
		input_name = input('|ENTER Task Name|: ')

	input_detail = input('|ENTER Detail of Task|: ')
	while not input_detail:
		input_detail = input('|ENTER Detail of Task|: ')

	input_due = input('|(Optional)ENTER Due Date or press ENTER to skip|: ')
	if not input_due:
		input_due = 'n/a'

	input_user = input('|(Optional)ENTER User Name or press ENTER to skip|: ')
	if not input_user:
		input_user= 'n/a'

	input_catagory = input('|(Optional)ENTER Catagory or press ENTER to skip|: ')
	if not input_catagory:
		input_catagory = 'n/a'
	
	new_task = Manager(input_name, input_detail, dt.now(), input_due, input_user, input_catagory)
	return new_task

def delete_num(order, tasks, num_to_delete):
	"""
	Function delete_num(order, tasks, num_to_delete):

	Description: Delete the given number in order list, and remove the key
	and value in dictionary tasks, where the key = number given. Since the
	order list is in order (i.e. 1,2,3,4,5), whichever number removed will
	cause the number list and dictionary to shift and adjust so the new
	edited list will remain in order without skipping.

	In-take Variable: order (list), tasks (dictionary), num_to_delete (int)
	Returned Variable: order, tasks
	"""

	order = order[:-1]
	del tasks[num_to_delete]
	
	#proceeds to shift all tasks' keys by n-1 if num_to delete is not at the end
	shift_num = num_to_delete
	while shift_num + 1 in tasks.keys():
		tasks[shift_num] = tasks[shift_num + 1]
		shift_num += 1

	return order , tasks

# Print all tasks as a list (without detail)
def print_tasks_as_list(order,tasks):
	"""
	Function print_tasks_as_list(order, tasks):

	Description: Takes in order and tasks, date created and task name will be
	printed out as a list.

	In-take Variables: order (list), tasks (dictionary)
	Returned Variable: n/a
	"""
	for num in order:
		print(str(num) + tasks[num].return_min_info())

# Print all the tasks info provided
def print_tasks(order, tasks):
	"""
	Function print_tasks(order, tasks):

	Description: Takes in order and tasks, all tasks will be printed
	out in the order of the order list.

	In-take Variables: order (list), tasks (dictionary)
	Returned Variable: n/a
	"""
	for num in order:
		info_list = tasks[num].return_info()
		print("-----[Task No. " + str(num) + "]-----")
		for content in info_list:
			print(content)

# Used when program starts to re-open files saved from previous session
def read_file(file_name):
	"""
	Function read_file(file_name):

	Description: Process the file of given file_name to read the saved data
	, the data will be processed and form "order" list and "tasks" dictionary
	these two variables will be returned.

	In-take Variable: file_name (str)
	Returned Variable: order (list), tasks (dictionary)
	"""
	order = []
	tasks = {}

	# If no previous data found, return a empity list and dictionary
	if not os.path.exists("../"+file_name):
		return order, tasks

	# For counting where the start of each dataset is located
	order_increment = lambda num: num+8 # The start of each dataset is 8 lines apart
	order_num = 2 						# The start of first dataset is at line 2
	process_task = False 				# True when the start of a new dataset is found

	# Start of processing data file
	with open("../"+file_name, "rt") as file:
		for num, line in enumerate(file,1):

			line = line.strip("\n")

			# After the line locating # for "order" list is found,
			# This will be used to create a new task for "tasks" dict.
			if process_task:

				if line == "---":

					new_task = Manager(temp[0], temp[1], temp[2],
									   temp[3],temp[4], temp[5])
					tasks.setdefault(order[-1], new_task)
					process_task = False

				else:

					temp.append(line)

			# Test 1: make sure first line is in right format
			elif num == 1 and not "FILE DATA" in line:

				print("Inocorrect Data Format")
				break

			# Append data for "order" list
			elif num == order_num:

				order.append(int(line))
				order_num = order_increment(num)
				process_task = True
				temp = []

	# For Manual Testing:
	#print(order)
	#print(tasks)

	print("*Previous saved data found and opened* \n")
	return order, tasks

# Used before program closes to keep the tasks created
def write_file(file_name, order, tasks):
	"""
	Function write_file(file_name, order, tasks):

	Description: Record the given order/tasks data to a .md file with given name.
	If old file exists, and order is now empty, old file will be removed, if old
	file does not exist, and old file is empty, nothing will be saved.

	In-take Variable: file (str), order (list), tasks (dictionary)
	Returned Variable: n/a
	"""

	# If there aren't things to be saved:
	if not order:

		if not os.path.exists("../"+file_name):

			return

		os.remove("../"+file_name) # Old file removed if order list is empty
		return

	# If there are things to be saved:
	file = open("../"+file_name, "w")
	file.write("FILE DATA | Warning: manually editing may result in file error\n")
	
	for num in order:

		file.write(str(num)+"\n")
		info_list = tasks[num].return_raw_info()

		for content in info_list:

			file.write(content+"\n")

		file.write("---\n")

	file.close