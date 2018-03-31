from django.forms import ModelForm, DateField
from django.contrib.admin import widgets

from .models import LeaveInfo

class LeaveInfoForm(ModelForm):
    class Meta:
        model = LeaveInfo
        fields = ['isLeaving_bool', 'LeaveTime_date', 'BackTime_date', 'Destination_text',
                  'StuPhone_bigint', 'Contact_text', 'ContactPhone_bigint']
    LeaveTime_date = DateField(widget=widgets.AdminDateWidget())
    BackTime_date = DateField(widget=widgets.AdminDateWidget())
