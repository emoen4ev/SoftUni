from project.task import Task
from project.section import Section

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

'''
Test Code:

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

--------------------------------------------------

Output:

Go to University
28.05.2020
Don't forget laptop and notebook
Name: Go to University - Due Date: 28.05.2020
Task Name: Go to University - Due Date: 28.05.2020 is added to the section
Cleared 0 tasks.
Section Daily tasks:
Name: Go to University - Due Date: 28.05.2020
Name: Make bed - Due Date: 27/05/2020
'''