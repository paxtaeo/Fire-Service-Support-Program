from django.forms import ModelForm
from .models import DailyMenu, Favorites

class DailyMenuForm(ModelForm):
    class Meta:
        model = DailyMenu
        fields = ['menu1', 'menu2', 'menu3',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu1'].widget.attrs.update({'class': 'form-select', 'onchange' : 'calculateTotalPrice();'})
        self.fields['menu2'].widget.attrs.update({'class': 'form-select', 'onchange' : 'calculateTotalPrice();'})
        self.fields['menu3'].widget.attrs.update({'class': 'form-select', 'onchange' : 'calculateTotalPrice();'})


class FavoritesForm(ModelForm):
    class Meta:
        model = Favorites
        fields = ['menu1', 'menu2', 'menu3',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu1'].widget.attrs.update({'class': 'form-select', 'onchange' : 'calculateTotalPrice();'})
        self.fields['menu2'].widget.attrs.update({'class': 'form-select', 'onchange' : 'calculateTotalPrice();'})
        self.fields['menu3'].widget.attrs.update({'class': 'form-select', 'onchange' : 'calculateTotalPrice();'})
