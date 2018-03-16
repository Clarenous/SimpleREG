from django.forms import ModelForm
from .models import LeaveInfo

class LeaveInfoForm(ModelForm):
    class Meta:
        model = LeaveInfo
        fields = ['LeaveTime_date', 'BackTime_date','Destination_text',
                  'StuPhone_bigint', 'Contact_text', 'ContactPhone_bigint']