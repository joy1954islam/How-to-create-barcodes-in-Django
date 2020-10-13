

from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib import messages
from BarCodeApps.forms import BarCodeForm
from BarCodeApps.models import BarCode


class BarCodeList(ListView):
    model = BarCode
    template_name = 'barcode_views.html'
    context_object_name = 'BarCode'

    def get_queryset(self):
        return BarCode.objects.all().order_by('SiteName')


class BarCodeCreate(CreateView):
    form_class = BarCodeForm
    template_name = 'barcode_create.html'

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request,messages.INFO,'BARCODE SAVE SUCCESSFULLY')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('create')

