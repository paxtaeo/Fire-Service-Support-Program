from django import forms
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from .models import Incident, DispatchedTeam


class IndexView(generic.TemplateView):
    template_name = 'dispatch/index.html'
    
    def get_context_data(self):
        context = super().get_context_data()

        try:
            context['incidents'] = Incident.objects.all().order_by('created_at')
        except:
            context['incidents'] = None

        return context


def DispatchedTeamUpdateView(request, pk):
    DispatchedTeamFormSet=inlineformset_factory(Incident, DispatchedTeam, 
                                                fields=('agency', 'location', 'vehicle', 'headcount', 'is_dispatched'), 
                                                extra=0,
                                                widgets={
                                                    'headcount': forms.NumberInput(attrs={'class': 'w-75 text-center border', 'onchange': 'calculateHeadcount()'}),
                                                    'is_dispatched': forms.CheckboxInput(attrs={'class': 'form-check-input mx-0', 'onchange': 'calculateHeadcount()'})
                                                })
    incident = Incident.objects.get(id=pk)
    formset = DispatchedTeamFormSet(instance=incident)
    
    if request.method == "POST":
        formset=DispatchedTeamFormSet(request.POST, instance=incident)
        if formset.is_valid():
            formset.save()
            return redirect('dispatch:index')

    return render(request, 'dispatch/update_dispatchedTeam.html', {'formset':formset})


def createIncident(request):
    incident = Incident.objects.create(outline=request.POST['outline'])
    DispatchedTeam.createDrafts(incident)

    return HttpResponseRedirect(reverse('dispatch:update_dispatchedTeam', kwargs={'pk':incident.pk}))
