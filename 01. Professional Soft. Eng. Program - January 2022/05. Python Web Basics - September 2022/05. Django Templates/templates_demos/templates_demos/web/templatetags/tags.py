from django.template import Library

from templates_demos.web.views import Student

register = Library()


# Simple tag always return string !!!
# Example of simple tag:
@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f'Hello, My name is {student.name} and I am {student.age}-years old.'


@register.simple_tag(name='sample_tag')
def sample_tag(*args, **kwargs):
    return ', '.join(str(x) for x in (list(args) + list(kwargs.items())))


# @register.inclusion_tag('tags/nav.html', name='app_nav')
# def generate_nav(*args):
#     context = {
#         'url_names': args,
#
#     }
#
#     return context


@register.inclusion_tag('tags/nav.html', name='app_nav', takes_context=True)
def generate_nav(context, *args):
    return {
        'url_names': args,
    }