from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from .export import exportWeeklyMenus

from .models import DailyMenu, Favorites
from .forms import DailyMenuForm, FavoritesForm

from datetime import date, datetime

class IndexView(generic.TemplateView):
    template_name = 'meal/index.html'
    
    def get_context_data(self):
        context = super().get_context_data()

        try:
            context['todoFirst'] = DailyMenu.objects.filter(user = self.request.user, status = 0).order_by('date')[0].pk
        except:
            context['todoFirst'] = None
        finally:
            context['todoNum'] = DailyMenu.objects.filter(user = self.request.user, status = 0).count()
        
        try:
            context['todayMenus'] = DailyMenu.objects.get(user = self.request.user, date = date.today())
        except:
            context['todayMenus'] = None

        return context


class OrderListView(generic.ListView):
    template_name = 'meal/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return DailyMenu.objects.filter(user = self.request.user, status__gt = 0).order_by('-date')[:30]


class OrderUpdateView(generic.UpdateView):
    form_class = DailyMenuForm

    template_name = 'meal/order.html'
    context_object_name = 'order'

    def form_valid(self, form):
        form.instance.status = 1
        return super().form_valid(form)

    def get_object(self): 
        order = get_object_or_404(DailyMenu, pk = self.kwargs['pk'])
        return order

    def get_context_data(self):
        context = super().get_context_data()
        try:
            context['favoritesList'] = Favorites.objects.all()
        except:
            context['favoritesList'] = None
        return context

    def get_success_url(self):
        try:
            todo = DailyMenu.objects.filter(user = self.request.user, status = 0).order_by('date')[0].pk
        except:
            return reverse('meal:order_list')
        return reverse('meal:order_update', kwargs={'pk':todo})
        

class FavoritesCreateView(generic.CreateView):
    form_class = FavoritesForm

    template_name = 'meal/favorites.html'
    success_url = reverse_lazy('meal:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def create(request):
    DailyMenu.createDrafts(datetime.strptime(request.POST['startDate'], '%Y-%m-%d'), 7)
    return redirect('meal:index')

def export(request):
    return exportWeeklyMenus(request)
