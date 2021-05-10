from django.contrib import admin
from .models import DailyMenu, Favorites
import csv
from django.http import HttpResponse


class DailyMenuAdmin(admin.ModelAdmin):
    # Post 객체를 보여줄 때 출력할 필드 설정
    list_display = ('date', 'user', 'menu1', 'menu2', 'menu3', 'status')
    # 필터링 항목 설정
    list_filter = ('date', 'user', 'status')

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
        )
        response.write(u'\ufeff'.encode('utf8'))

        writer = csv.writer(response)

        field_names = [field.name for field in self.model._meta.fields]
        writer.writerow(field_names)

        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response


class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'menu1', 'menu2', 'menu3')
    list_filter = ('user',)


admin.site.register(DailyMenu, DailyMenuAdmin)
admin.site.register(Favorites, FavoritesAdmin)
