from django.urls import reverse_lazy
from django.views import generic

#Consumer model
from .models import Consumer

class IndexView(generic.TemplateView):
    """
    Homepage /
    """
    template_name = 'consumers/index.html'

class ListView(generic.ListView):
    """
    List page of consumer details
    /list
    """
    template_name = 'consumers/list.html'
    model = Consumer
    context_object_name = 'all_consumers'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # If redirection from succesfull Add of consumer
        if 'add_success' in self.request.session :
            del self.request.session['add_success']
            #Add flag to show success message
            context['add_success'] = True
        return context

class AddView(generic.CreateView):
    """
    Consumer Add page
    /add
    """
    model = Consumer
    fields = ['name','email']
    template_name = 'consumers/add.html'
    #Redirect to list if consumer add is successful
    success_url = reverse_lazy('consumers:list')

    #if consumer detail is getting added
    def form_valid(self, form):
        result = super().form_valid(form)
        #if successful, Add flag in session to show alert on list page
        self.request.session['add_success'] = True
        return result