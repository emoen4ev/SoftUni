# "departments"'s app urls.py


from django.urls import path

from departments_app.departments.views import sample_view

urlpatterns = (
    # /departments/
    path("", sample_view),

    # /departments/{department_id}/
    path("<department_id>/", sample_view),

    # /departments/int/{department_id}/
    path("int/<int:department_id>/", sample_view),
)


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