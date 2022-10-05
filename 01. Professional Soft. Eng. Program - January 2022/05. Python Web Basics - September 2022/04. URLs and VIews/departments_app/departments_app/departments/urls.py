# "departments"'s app urls.py
from django.shortcuts import redirect
from django.urls import path

# from departments_app.departments.views import sample_view
from departments_app.departments.views import show_departments, show_department_details, redirect_to_first_department

urlpatterns = (
    # /departments/
    path("", show_departments, name= "show departments"),

    path("redirect/", redirect_to_first_department, name= "redirect demo"),

    # /departments/{department_id}/
    # path("<department_id>/", show_departments),
    path("<department_id>/", show_department_details, name= "show department details with string"),

    # /departments/int/{department_id}/
    # path("int/<int:department_id>/", show_departments),
    path("int/<int:department_id>/", show_department_details, name= "show department details"),
    path("by-id/<int:department_id>/", show_department_details, name="show department details"),

)

# urlpatterns = (
#     # /departments/
#     path("", sample_view),
#
#     # /departments/{department_id}/
#     path("<department_id>/", sample_view),
#
#     # /departments/int/{department_id}/
#     path("int/<int:department_id>/", sample_view),
# )

# paths = (
#     "",
#     "<department_id>/",
#     "int/<int:department_id>/",
# )
#
# urlpatterns = [path(url, sample_view) for url in paths]


# urlpatterns = ()
# urlpatterns += (path("", sample_view), )
# urlpatterns += (path("<department_id>/", sample_view), )
# urlpatterns += (path("int/<int:department_id>/", sample_view), )