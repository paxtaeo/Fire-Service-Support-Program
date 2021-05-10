from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from datetime import timedelta, date

from meal.constants import *

class DailyMenu(models.Model):
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    menu1 = models.CharField(max_length = 100, blank = True, null = True, choices = choice_list)
    menu2 = models.CharField(max_length = 100, blank = True, null = True, choices = choice_list)
    menu3 = models.CharField(max_length = 100, blank = True, null = True, choices = choice_list)

    status = models.IntegerField(default = 0)
    # 0 : Created by admin
    # 1 : Selected by user
    # 2 : Order complete

    def createDrafts(startDate, duration):
        users = User.objects.all()
        for delta in range(duration):
            date = startDate + timedelta(days = delta)
            DailyMenu.objects.bulk_create([
                DailyMenu(date = date, user = user) for user in users
            ])
    
# from meal.models import DailyMenu
# from datetime import timedelta, date
# DailyMenu.createDrafts(date(2021,5,20), 10)

    def setDailyMenu(self, menu1, menu2, menu3):
        self.menu1 = menu1
        self.menu2 = menu2
        self.menu3 = menu3
        self.status = 1
        self.save()

    def completeOrder(self):
        self.status = 2
        self.save()

    def __str__(self):
        return f'{self.date} | {self.user} | {self.menu1} | {self.menu2} | {self.menu3} | {self.status}'


class Favorites(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    menu1 = models.CharField(max_length = 100, choices = choice_list)
    menu2 = models.CharField(max_length = 100, choices = choice_list)
    menu3 = models.CharField(max_length = 100, blank = True, null = True, choices = choice_list)

    def __str__(self):
        string = f'{self.user} | {self.menu1} | {self.menu2}'
        if self.menu3:
            string += f' | {self.menu3}'
        return string