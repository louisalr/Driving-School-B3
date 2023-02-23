from django.views import generic
from home.models import School


class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'schools'

    def get_queryset(self):
        return School.objects.all()
        


class DetailView(generic.DetailView):
    model = School
    template_name = 'home/detail.html'
