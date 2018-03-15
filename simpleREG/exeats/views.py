from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Holiday, LeaveInfo


def exeats(request):
    latest_holiday_list = Holiday.objects.order_by('-id')[:3]
    context = {'latest_holiday_list': latest_holiday_list}
    return render(request, 'exeats/exeats.html', context)


@login_required()
def catalog(request):
    holiday_list = Holiday.objects.order_by('-id')
    context = {'holiday_list': holiday_list}
    return render(request, 'exeats/catalog.html', context)


@login_required()
def holiday_detail(request, holiday_id):
    holiday = get_object_or_404(Holiday, pk=holiday_id)
    try:
        leaveinfo = holiday.leaveinfo_set.get(StuNumber_int=request.user.StuNumber)
    except (KeyError, LeaveInfo.DoesNotExist):
        leaveinfo = LeaveInfo()
    context = {'holiday': holiday, 'leaveinfo': leaveinfo}
    return render(request, 'exeats/HolidayDetail.html', context)