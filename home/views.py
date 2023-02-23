from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from home.forms import RegistrationForm
from home.models import School


class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'schools'

    def get_queryset(self):
        return School.objects.all()


class DetailView(generic.DetailView):
    model = School
    template_name = 'home/detail.html'


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    # If user manages to navigate to this page, but he's logged, redirect to home page
    if request.user.is_authenticated:
        return redirect("home:index")
    # Else show him the login form
    else:
        form = AuthenticationForm()
        return render(request=request, template_name="registration/login.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect('home:index')


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "home/register.html"


class IndexAccountView(generic.ListView):
    template_name = 'account/profile.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return School.objects.all()
