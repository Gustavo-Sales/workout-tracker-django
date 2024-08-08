from django.urls import path

from . import views


app_name = "core"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "workout/<str:id>/",
        views.WorkoutDetailView.as_view(),
        name="detail",
    ),
    path("create_workout/", views.CreateWorkoutView.as_view(), name="create"),
    path("delete_workout/<pk>/", views.DeleteWorkoutView.as_view(), name="delete"),
    path("update_workout/<str:id>/", views.UpdateWorkoutView.as_view(), name="update"),
]
