"""Script to run my project"""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
import my_module.functions as fx

###
###

def demo(file_name = "data.md"):
    
	print("\n Welcome to Task Manager 1.0 \n")
	
	# tasks store all the tasks user stored
	# order store all the tasks in order of how they are saved
	order, tasks = fx.read_file(file_name)


	# Loop until user decides to quit.
	stay = True

	while stay:

		print(
			"		Menu: \n \
			q = quit \n \
			list = quick view tasks \n \
			see = view tasks in detail \n \
			add = add task \n \
			del = delete task")

		user_input = input('\n |INPUT|: ')

		if user_input == 'q':

			stay = False
			continue

		elif user_input == 'list':
			
			if not order:

				print("No task recorded")

			else:

				fx.print_tasks_as_list(order, tasks)

		elif user_input == 'add':

			# Decides the location of dictionary/order to store the new task
			if not order:
				
				storing_location = 1
				
			else:
				
				storing_location = order[-1]+ 1

			new_task = fx.create_task()
			order.append(storing_location)
			tasks.setdefault(storing_location,new_task)

		elif user_input == 'del':

			if not order:

				print("There are no tasks, nothing avliable to delete")
				continue

			print("Which task would you like to delete")
			print("Avliable to delete: " + str(order))

			while True:

				try: 

					num_to_del = input("ENTER Task Number or 'x' to cancel: ")

					if num_to_del == 'x':

						break

					elif int(num_to_del) in order:

						order, tasks = fx.delete_num(order, tasks, int(num_to_del))
						break

					else:

						print("invalid response: number not in list")

				except:

					print("invalid response: input is not a number")

		elif user_input == 'see':

			if not order:

				print("No task recorded")

			else:

				fx.print_tasks(order, tasks)

		else: # When user input a string that is not a part of the Menu Options.

			print("invalid input, example input: 'see'")

	if order: # Only prompted when there are things to be saved

			print("Task Manager ended, tasks will be saved at: " + file_name)
	
	fx.write_file(file_name, order, tasks)
    
if __name__ == "__main__":
    demo()