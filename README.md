# Task Manager

## Introduction

Date Created: 3/16/2021 [COGS 18 Final Project]


Welcome to Task Manager 1.0

The objective of this project is to have a Terminal-runned or Jupyter Notebook based local task planning service, functionalities of this project include:
- add/delete tasks
- preview all tasks in list
- view all tasks in detail
- automatically save tasks (if there are tasks active before quitting Task Manager)
- automatically re-open tasks from previous sessions (if it exists)


#### Notes:
- To run this program in Jupyter Notebook: Import the program and call the "demo" function from script.py as belows. (Look at "Task_Manager_Demo_Notebook.ipynb")
- To run this program in Terminal, make sure Python 3 is installed. Head to folder program_script and run: "Python3 script" (preferred method)

## Run Program in Terminal/Command Prompt
1. Download Task_Manager folder (Entire file)
2. Open terminal/Command Prompt, switch directory to ../Task_manager/program_script
3. After the current direcotry is set to program_script, run script.py by:
```Bash
python3 script.py
```
4. Program now runs, be ware the defaulted data storing location will be located at "Task_Manager\data.md"


## Project Format

Task_Manager [Main Folder] \
| README.md (Description of Project for Github) \
| Task_Manager_Demo_Notebook.ipynb (Description + Demo on Jupyter Notebook)\
| example_data.md (Example for this demo)\
| test_data.md (For auto/manual function testing)\
| my_module [Folder] \
---| classes.py (The only class used for this project) \
---| functions.py (Includes all the function used for this project) \
---| test_functions.py (For function testing) \
| program_script [Folder] \
---| script.py (Run this in terminal/command prompt to run project)

## Rerquirements
- Install Python2 or Python3
- (Optional) Install Jupyter Notebook

## About Author

This Project is made by Jason H. for COGS 18 course.

I started with AP Comp Sci course with Java. Transitioned to Python after the course. I this is my 3rd Python Project. I have been using Python to code for about a year (with pauses in between)

#### Skills I learned and mastered upon complete this project:
- Object-Oriented Programing for Python (Classes, Functions, Main script)
- Accessing external file (os, open file, write/read file)
- PEP8 Formatting
- Formal documentation with Docstrings
- Function Testing (Note: Automatic/Manual testing)

#### Things planned to be included in Task_Manager 2.0 (Coming Soon):
- Choose a task to turn it into calander file (.ics)
- Sort tasks
- Convert to popular data formats such as json, csv

### License

MIT License - https://opensource.org/licenses/MIT