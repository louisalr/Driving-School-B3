from django.shortcuts import render
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
    return render(request=request, template_name="home/login.html")


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "home/register.html"
