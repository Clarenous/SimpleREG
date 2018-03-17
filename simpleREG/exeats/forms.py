from django.forms import ModelForm, DateField
from django.contrib.admin.widgets import AdminDateWidget

from .models import LeaveInfo

class LeaveInfoForm(ModelForm):
    class Meta:
        model = LeaveInfo
        fields = ['LeaveTime_date', 'BackTime_date','Destination_text',
                  'StuPhone_bigint', 'Contact_text', 'ContactPhone_bigint']
    def __init__(self, *args, **kwargs):
        super(LeaveInfoForm, self).__init__(*args, **kwargs)
        self.fields['LeaveTime_date'].widget = AdminDateWidget()
        self.fields['BackTime_date'].widget = AdminDateWidget()