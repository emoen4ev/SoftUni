# admin.py

from django.contrib import admin

from models_1.web.models import Employee, NullBlankDemo, Department, Project, Category


# The 'Employee' model is enabled in django admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'level',
        # 'department',
        'employee_department',
    )
    list_filter = (
        'level',
        'first_name',
        'department',
    )
    search_fields = (
        'first_name',
        'last_name',
    )
    sortable_by = ('id', 'first_name')

    def employee_department(self, obj):
        return obj.department.name

    fieldsets = (
        (
            'Personal info',
            {
                'fields': ('first_name', 'last_name', 'age'),
            }
        ),
        (
            'Professional Info',
            {
                'fields': ('level', 'years_of_experience'),
            }
        ),
        (
            'Company Info',
            {
                'fields': ('department', 'is_full_time', 'email', 'start_date')
            }
        ),
    )

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass