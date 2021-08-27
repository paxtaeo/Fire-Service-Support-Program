from django.contrib import admin
from .models import Incident, BaseTeam, DispatchedTeam


class IncidentAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'outline', 'in_progress', 'updated_at')
    list_filter = ('in_progress',)


class BaseTeamAdmin(admin.ModelAdmin):
    list_display = ('agency', 'location', 'vehicle', 'headcount')
    list_filter = ('agency', 'location', 'vehicle')


class DispatchedTeamAdmin(admin.ModelAdmin):
    list_display = ('incident', 'agency', 'location', 'vehicle', 'headcount', 'is_dispatched')
    list_filter = ('incident', 'agency', 'location', 'vehicle', 'headcount', 'is_dispatched')


admin.site.register(Incident, IncidentAdmin)
admin.site.register(BaseTeam, BaseTeamAdmin)
admin.site.register(DispatchedTeam, DispatchedTeamAdmin)
