from django.urls import path

from taskmanager.views import index, TaskListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list",
    ),
]

app_name = "taskmanager"