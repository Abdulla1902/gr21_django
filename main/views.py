from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime

date = datetime.now().date()

def main(request):
    return HttpResponse('<h2><center>Главная<center><h2>')
def about_us(request):
    return HttpResponse('<h2><center>Сайт создан в субботу 22 октября 2022 года, в 3:21 ночи!<center><h2>')
def date_now(request):
    return HttpResponse(f'<h2><center>{date}<center><h2>')
