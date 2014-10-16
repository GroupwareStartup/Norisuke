from django.shortcuts import render

from django.http import HttpResponse
from norisuke.models import *

def schedule_list(request):

    return render(request, "ScheduleList.html", None)

