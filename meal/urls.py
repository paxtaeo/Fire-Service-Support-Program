from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

app_name = 'meal'
urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name = 'index'),
    path('orders/', login_required(views.OrderListView.as_view()), name = 'order_list'),
    path('orders/<int:pk>/update/', login_required(views.OrderUpdateView.as_view()), name='order_update'),
    path('favorites/new', login_required(views.FavoritesCreateView.as_view()), name='favorites_new'),

    path('create/', views.create, name='create'),
    path('export/', views.export, name='export'),
]
