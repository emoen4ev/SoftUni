from django.template import Library

from templates_demos.web.views import Student

register = Library()


# Simple tag always return string !!!
# Example of simple tag:
@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f'Hello, My name is {student.name} and I am {student.age}-years old.'