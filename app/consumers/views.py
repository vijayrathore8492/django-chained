from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
from .models import Consumer


class IndexView(generic.TemplateView):
    template_name = 'consumers/index.html'

class ListView(generic.ListView):
    template_name = 'consumers/list.html'
    model = Consumer
    context_object_name = 'all_consumers'

class AddView(generic.CreateView):
    model = Consumer
    fields = ['name','email']
    template_name = 'consumers/add.html'
    success_url = reverse_lazy('consumers:list')

    #if consumer detail is getting added
    def form_valid(self, form):
        return super().form_valid(form)