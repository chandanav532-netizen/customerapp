from django.urls import reverse_lazy
from django.views.generic import(ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import customer
class CustomerListView(ListView):
    model=customer
    template_name='customers/customer-list.html'
    context_object_name='custsomers'
    paginate_by=10

class CustomerDetailView(DetailView):
    model=customer
    template_name='customers/customer-detail.html'
    context_object_name='customer'

class CustomerCreateView(CreateView):
    model=customer
    fields=['name','email','phone','address']
    template_name='customers/customer_form.html'
    success_url=reverse_lazy('customer-list')

class CustomerUpdateView(UpdateView):
    model=customer
    fields=['name','email','phone','address']
    template_name='customers/customer_form.html'
    success_url=reverse_lazy('customer-list')

class CustomerDeleteView(DeleteView):
    model=customer
    template_name='customers/customer_confirm_delete.html'
    success_url=reverse_lazy('customer-list')
    

    

