"""Test for my functions.

Note: SOME REQUIRE MANUAL TESTING!
** IMPORTANT: Before testing, must read and edit line 4-8 of functions.py
"""

from functions import create_task, delete_num, print_tasks, print_tasks_as_list, read_file, write_file
from classes import Manager
import os
##
##

# Example Data For Testing
test_order = [1,2,3,4,5]
tasks = [Manager("Sleep", "Go to sleep", "2021/3/11 11:26",
				 			"10:00 pm", "Bob", "Daily"),
		 Manager("MATH 18 Homework", "Homework 6",
				 "2021/3/9 8:16", "2021/3/11", "n/a", "College"),
		 Manager("COGS 18 Project", "Final Project for the course",
					 "2021/3/11 11:26", "2021/3/19", "n/a", "College"),
		 Manager("COVID-19 Testing", "Get a COVID test",
				 "2021/3/3", "n/a", "n/a", "n/a"),
		 Manager("Buy RTX 3070", "For Gaming and ML", "2021/3/1", 
				 "ASAP", "David", "n/a")]
test_tasks = {}
for num, task in zip(test_order,tasks):
	test_tasks[num] = task

# Test Functions starts here
def test_create_task():
	"""
	Manual Testing REQUIRED!

	Because this function prompt for user interaction,
	it will require you to test manually by calling the
	function, and after done, compare with the printed
	result.
	"""
	# UNCOMMENT for manual testnig
	#print(create_task().return_info())

	# Automatic testing: 
	assert callable(create_task)

def test_delete_num():
	"""
	These two cases is sufficient to cover every edge case
	in my_script, any number not in order list or tasks dictionary
	will not be able to proceed to the delete_num function.
	"""
	assert callable(delete_num)
	a,b =  delete_num(test_order, test_tasks, 1)
	assert a == [1,2,3,4]
	a,b =  delete_num(test_order, test_tasks, 4)
	assert a == [1,2,3,4]
    
def test_print_tasks_as_list():
	"""
	Manual Testing REQUIRED!

	This function will not return anything but to print out
	the list and dictionary provided, thus check values
	above with the output from this function.
	"""
	assert callable(print_tasks_as_list)
    #print_tasks(test_order, test_tasks)

def test_print_tasks():
	"""
	Manual Testing REQUIRED!

	This function will not return anything but to print out
	the list and dictionary provided, thus check values
	above with the output from this function.
	"""
	assert callable(print_tasks)
    #print_tasks(test_order, test_tasks)

def test_read_file():
	assert callable(read_file)
	a,b = read_file("abcdefghijk") # Test for unexisted files
	assert a == []
	assert b == {}
	a,b = read_file("example_data.md")
	assert a == [1,2,3,4,5]
	assert type(b) == dict

def test_write_file():
	assert callable(write_file)
	write_file("should_not_exist",[],{}) # Test for empity list
	assert not os.path.exists("../should_not_exist")

	write_file("test_data.md",test_order, test_tasks)
	assert os.path.exists("../test_data.md")

# Alternative to Pytest
if __name__ == "__main__":
	test_create_task()
	test_delete_num()
	test_print_tasks_as_list()
	test_print_tasks()
	test_read_file()
	test_write_file()
	print("ALL TEST PASSED")