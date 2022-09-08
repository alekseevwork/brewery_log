from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.urls.base import reverse_lazy, reverse

from .models import Measuring, Tank
from .forms import MeasuringForm, AddTankForm


class HomeBrewery(ListView):
    model = Measuring
    context_object_name = 'brewery'
    template_name = 'brewery/measuring_list.html'


class DetailTank(DetailView):
    model = Tank
    context_object_name = 'brewery'
    template_name = 'brewery/tank_detail.html'

    # def get_queryset(self):
    #     return Tank.objects.filter(id=self.kwargs['pk'])


class AllTanks(ListView):
    model = Measuring
    template_name = 'brewery/measuring_list.html'
    context_object_name = 'brewery'

    def get_queryset(self):
        return Measuring.objects.filter(tank_id=self.kwargs['pk'])


class CreateMeasuring(CreateView):
    form_class = MeasuringForm
    template_name = 'brewery/add_measuring.html'


class AddTanks(CreateView):
    form_class = AddTankForm
    template_name = 'brewery/add_tank.html'
    success_url = reverse_lazy('home')


class DeleteTank(DeleteView):
    model = Tank
    template_name = 'brewery/delete_tank.html'

    success_url = reverse_lazy('home')
