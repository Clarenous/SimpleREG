from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse

from .models import Holiday, LeaveInfo

from .forms import LeaveInfoForm


def exeats(request):
    latest_holiday_list = Holiday.objects.order_by('-id')[:2]
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


@login_required()
def leaveinfo_edit(request, holiday_id):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    holiday = get_object_or_404(Holiday, pk=holiday_id)
    # 只有当请求为 POST 时，才表示用户提交了离校登记表
    if request.method == 'POST':
        form = LeaveInfoForm(request.POST)
        # 验证数据的合法性
        if form.is_valid():
            leaveinfo = form.save(commit=False)
            leaveinfo.holiday = holiday
            leaveinfo.StuNumber_int = request.user.StuNumber
            leaveinfo.StuClass_int = request.user.StuClass
            leaveinfo.StuName_text = request.user.StuName
            leaveinfo.pub_date = timezone.localtime(timezone.now())
            # 检查是否已提交过离校表
            try:
                current_leaveinfo = holiday.leaveinfo_set.get(StuNumber_int=request.user.StuNumber)
                leaveinfo.pk = current_leaveinfo.pk
            except (KeyError, LeaveInfo.DoesNotExist):
                pass
            leaveinfo.save()

            if reverse('exeats:holiday_detail', args=(holiday_id,)):
                return redirect(reverse('exeats:holiday_detail', args=(holiday_id,)))
            else:
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问填表页面，返回已有的表格信息
        try:
            leaveinfo = holiday.leaveinfo_set.get(StuNumber_int=request.user.StuNumber)
        except (KeyError, LeaveInfo.DoesNotExist):
            leaveinfo = LeaveInfo()
        form = LeaveInfoForm(instance=leaveinfo)

    context = {'form': form, 'next': redirect_to, 'holiday': holiday}
    return render(request, 'exeats/LeaveInfo_edit_form.html', context)