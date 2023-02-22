from django.views import generic
from home.models import School


class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'cars'

    def get_queryset(self):
        """Return the last five published questions."""
        return School.objects.order_by('marque')[:5]
