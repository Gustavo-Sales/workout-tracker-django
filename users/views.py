from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginView(View):
    template_name = "users/login.html"

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
        else:
            return render(
                request,
                self.template_name,
                {
                    "form": form,
                    "error": "Invalid Credentials",
                },
            )


class RegisterView(View):
    template_name = "users/register.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/auth/login/")

        first_error = None
        if form.errors:
            first_error = list(form.errors.values())[0][0]

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "error": first_error,
            },
        )


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy("users:login"))
