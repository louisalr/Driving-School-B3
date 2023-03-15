from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from home.forms import RegistrationForm, LoginForm, SchoolForm, EventForm
from home.models import School, Customer, Event


class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'schools'

    def get_queryset(self):
        return School.objects.all()


class DetailView(generic.DetailView):
    model = School
    template_name = 'home/detail.html'


# Display only the schools with available slots
class SchoolsWithReservationsOnly(generic.ListView):
    template_name = 'home/schools_available.slots.html'
    context_object_name = 'schools'

    def get_queryset(self):
        return School.objects.filter(event__isnull=False).distinct()


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


# Modify to take in account the checkbox
class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "home/register.html"


class SchoolIndexView(generic.ListView):
    template_name = 'home/school_list.html'
    context_object_name = 'schools'

    def get_queryset(self):
        return School.objects.all()


class CreateSchoolView(generic.CreateView):
    form_class = SchoolForm
    success_url = reverse_lazy("home:account")
    template_name = "school/school_create.html"

    def form_valid(self, form):
        # Get the current user to add the corresponding user to the new created school
        form.instance.creator = self.request.user.id

        # Save the form data to the database
        self.object = form.save()

        # Save the user corresponding to this schools
        user_school = Customer.objects.get(id=form.instance.creator).school.add(self.object)

        return super().form_valid(form)


def indexAccountView(request):
    # Get all the infos related to the current user logged in
    user_infos = Customer.objects.get(id=request.user.id)
    user_informations = ""
    user_reservations = ""

    # If user is not a school
    if user_infos.isManager:
        # Returns the only/multiple driving schools user owns
        print('School manager')
        customer = Customer.objects.get(id=request.user.id)
        user_informations = customer.school.all()
        print(user_infos.school)
    # Else user is a school
    else:
        # Get all the schools user is associated
        # TO-DO
        user_reservations = Event.objects.filter(attendees=request.user)
        print(user_reservations)

    return render(request, template_name="account/profile.html", context={"schools": user_informations, "reservations":
        user_reservations})


class SchoolDetailsView(TemplateView):
    template_name = 'school/school_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school'] = School.objects.get(id=self.kwargs['id'])
        context['events'] = Event.objects.all()
        return context


def account_address_delete(request, pk):
    # Returns an error if the schools has some reservations with at least one person in it

    # Get the school for the reference
    school = School.objects.get(pk=pk)

    # Delete the user linked to the school
    get_customer = Customer.objects.get(id=request.user.id)
    get_customer.school.remove(school)
    get_customer.save()

    # Then delete the school
    school.delete()
    school.save()

    return HttpResponseRedirect('/account/')


def DeleteEvent(request, pk):
    Event.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/account/')


class ManageEventView(generic.CreateView, generic.UpdateView):
    # Edit the form by getting all its informations
    form_class = EventForm
    success_url = reverse_lazy("home:account")
    template_name = "school/school_add_event.html"

    def get_object(self, queryset=None):
        # This method is called to get the object to edit in the UpdateView
        # We override it to check if the object exists and return it
        # or return None if it doesn't exist
        pk2 = self.kwargs.get('pk2')
        print(pk2)
        if pk2 is not None:
            return Event.objects.get(pk=pk2)
        return None

    def form_valid(self, form):
        form.instance.school = self.kwargs['pk']

        # Retrieve the school and
        # Save the form data to the database
        form.instance.creator = School.objects.get(id=form.instance.school)
        self.object = form.save()

        return super().form_valid(form)


class SchoolSlotsDetails(TemplateView):
    template_name = 'home/school_slots.html'

    def get_context_data(self, **kwargs):
        # Returns only the details for the selected school
        context = super().get_context_data(**kwargs)
        school = School.objects.get(id=self.kwargs['pk'])
        context['school'] = school
        context['events'] = Event.objects.filter(creator=school)
        return context


@login_required
def RegisterUserEvent(request, id):
    # Get the event and add the new user
    event = Event.objects.get(creator_id=id)
    event.attendees.add(request.user)

    # If user already participate in the event, return an error
    return redirect('/')


def DeleteUserEvent(request, id):
    # Remove the user from an event

    event = Event.objects.get(id=id)
    event.attendees.remove(request.user)
    return redirect('/account/')


class UserEventDetails(TemplateView):
    template_name = 'account/user_event_details.html'

    def get_context_data(self, **kwargs):
        # Returns only the details for the selected school
        context = super().get_context_data(**kwargs)
        context['event'] = Event.objects.get(id=self.kwargs['pk'])
        return context
