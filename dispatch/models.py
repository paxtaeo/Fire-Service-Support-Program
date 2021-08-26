from django.db import models


class Incident(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    outline = models.CharField(max_length = 100)
    in_progress = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.outline}'


class Team(models.Model):
    agency_list = (
		('원주소방서', '원주소방서 소방력 동원'),
        ('응원소방서', '응원소방서 소방력 동원'),
        ('타시도', '타시도 소방력 동원'),
        ('유관기관', '유관기관 소방력 동원'),
    )

    vehicle_list = (
        ('소방', (
            ('펌프', '펌프'),
            ('물탱크', '물탱크'),
            ('경형사다리차', '경형사다리차'),
            ('고가사다리차', '고가사다리차'),
            ('굴절차', '굴절차'),
            ('화학차', '화학차'),
            ('구급', '구급'),
            ('구조공작', '구조공작'),
            ('수난구조', '수난구조'),
            ('산악구조', '산악구조'),
            ('생활안전', '생활안전'),
            ('배연차', '배연차'),
            ('화물차', '화물차'),
            ('버스', '버스'),
            ('무인방수차', '무인방수차'),
        )),
        ('유관기관', (
            ('유관기관펌프', '유관기관 펌프'),
            ('유관기관물탱크', '유관기관 물탱크'),
            ('굴삭기', '굴삭기'),
            ('순찰차', '순찰차'),
            ('행정차', '행정차'),
            ('작업차', '작업차'),
        )),
        ('기타', (
            ('기타', '기타'),
        )),
    )

    agency = models.CharField(max_length = 100, null = True, choices = agency_list)
    location = models.CharField(max_length = 100, null = True)
    vehicle = models.CharField(max_length = 100, null = True, choices = vehicle_list)
    headcount = models.IntegerField()


class DispatchedTeam(Team):
    incident = models.ForeignKey('Incident', on_delete=models.CASCADE)
    is_dispatched = models.BooleanField(default = False)
