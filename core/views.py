from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Workout


class IndexView(LoginRequiredMixin, ListView):
    template_name = "core/index.html"
    login_url = "/auth/login/"
    redirect_field_name = "redirect_to"
    context_object_name = "workouts_list"

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)


class WorkoutDetailView(LoginRequiredMixin, DetailView):
    model = Workout
    template_name = "core/detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout = self.get_object()
        context["exercises"] = workout.exercises
        return context


class CreateWorkoutView(LoginRequiredMixin, View):
    template_name = "core/create_workout.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        exercises = []

        workout_name = request.POST.get("workout-name")
        workout_type = request.POST.get("workout-type")
        types = request.POST.getlist("type")

        if workout_type == "CA":
            durations = request.POST.getlist("duration")
            distances = request.POST.getlist("distance")
            paces = request.POST.getlist("pace")

            for i in range(len(types)):
                exercises.append(
                    {
                        "type": types[i],
                        "duration": durations[i],
                        "distance": distances[i],
                        "pace": paces[i],
                    }
                )

        elif workout_type == "ST":
            sets = request.POST.getlist("sets")
            repetitions = request.POST.getlist("repetitions")
            weights = request.POST.getlist("weight")

            for i in range(len(types)):
                exercises.append(
                    {
                        "type": types[i],
                        "sets": sets[i],
                        "repetitions": repetitions[i],
                        "weight": weights[i],
                    }
                )

        workout = Workout.objects.create(
            name=workout_name,
            type_workout=workout_type,
            exercises=exercises,
            user=self.request.user,
        )

        return redirect(workout.get_absolute_url())


class DeleteWorkoutView(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = "/"


class UpdateWorkoutView(LoginRequiredMixin, DetailView):
    model = Workout
    template_name = "core/update_workout.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout = self.get_object()
        context["exercises"] = workout.exercises
        return context

    def post(self, request, *args, **kwargs):
        workout = self.get_object()

        exercises = []

        workout_name = request.POST.get("workout-name")
        workout_type = request.POST.get("workout-type")
        types = request.POST.getlist("type")

        if workout_type == "CA":
            durations = request.POST.getlist("duration")
            distances = request.POST.getlist("distance")
            paces = request.POST.getlist("pace")

            for i in range(len(types)):
                exercises.append(
                    {
                        "type": types[i],
                        "duration": durations[i],
                        "distance": distances[i],
                        "pace": paces[i],
                    }
                )

        elif workout_type == "ST":
            sets = request.POST.getlist("sets")
            repetitions = request.POST.getlist("repetitions")
            weights = request.POST.getlist("weight")

            for i in range(len(types)):
                exercises.append(
                    {
                        "type": types[i],
                        "sets": sets[i],
                        "repetitions": repetitions[i],
                        "weight": weights[i],
                    }
                )

        workout.name = workout_name
        workout.type_workout = workout_type
        workout.exercises = exercises
        workout.save()

        return redirect(workout.get_absolute_url())
