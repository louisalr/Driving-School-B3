from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.list import BaseListView, ListView

from home.forms import RegistrationForm, LoginForm
from home.models import School, Customer, Booking


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
        form = LoginForm(request, data=request.POST)
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
        form = LoginForm()
        return render(request=request, template_name="registration/login.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect('home:index')


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "home/register.html"


class SchoolIndexView(generic.ListView):
    template_name = 'home/school_list.html'
    context_object_name = 'schools'

    def get_queryset(self):
        return School.objects.all()


def indexAccountView(request):
    # Get all the infos related to the current user logged in
    user_infos = Customer.objects.get(id=request.user.id)
    user_reservations = ""

    # If user is not a school
    if user_infos.isManager:
        # Returns the only/multiple driving schools user owns
        print('School manager')

    # Else user is a school
    else:
        print('User is linked to at least one school')
        # Get all the schools user is associated
        # TO-DO
        # get_schools = School.objects.get()
        # user_reservations = Booking.objects.get(customer=user_infos)

    return render(request, template_name="account/profile.html", context={"user": user_infos, "reservations":
        user_reservations})


class SchoolDetailsView(ListView):
    template_name = 'school/school_details.html'
    context_object_name = 'school'

    def get_queryset(self):
        return School.objects.get(id=self.kwargs['id'])
