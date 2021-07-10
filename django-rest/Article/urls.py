from django.urls import path
from . import views


urlpatterns = [
    path("", views.api_overview, name="article"),
    path("tasks/", views.task_list, name="task"),
    path("tasks/<id>", views.detail_view, name="detail"),
    path("create/", views.task_create, name="create"),
    path("update/<pk>", views.task_update, name="update"),
    path("delete/<pk>", views.task_delete, name="delete"),
]