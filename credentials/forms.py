from django import forms
from .models import Detail, Place


class DetailForm(forms.ModelForm):
    GENDER = (

        ('female', 'FEMALE'),
        ('male', 'MALE'),

    )
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER)

    account = (

        ('1','SAVINGS'),
        ('2', 'CURRENT')
    )
    account_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=account)
    materials = (
        ('1','CREDIT CARD'),
        ('2','DEBIT CARD'),
        ('3','CHEQUE BOOK')
    )
    materials_required = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=materials)
    YEARS = [x for x in range(1940, 2021)]
    dob = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    class Meta:
        model = Detail
        fields=['name','dob','age','gender','phone','email','address','district','place','account_type','materials_required']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['place'].queryset = Place.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['place'].queryset = Place.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['place'].queryset = self.instance.district.place_set.order_by('name')


