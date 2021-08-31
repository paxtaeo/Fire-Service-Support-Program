from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'dispatch'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('incidents/create/', views.createIncident, name='create_incident'),
    path('dispatchedteams/<int:pk>/', views.DispatchedTeamUpdateView, name='update_dispatchedTeam'),
]
