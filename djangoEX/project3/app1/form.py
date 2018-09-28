from django import forms
from app1.models import Employee
class loginForm(forms.Form):
    countryList = (
        ('EN','England'),
        ('FR','France'),
        ('JP','Japan'),
        )
    username = forms.CharField(label="Enter Username",max_length=50,required=False)
    password = forms.CharField(label="Enter password",max_length=50,required=False,widget=forms.PasswordInput)
    country = forms.ChoiceField(label="Select Country",choices=countryList)
    myPhoto = forms.FileField(label="select Photo",required=False)
    Comment = forms.CharField(label="Enter Comment",required=False,widget=forms.Textarea)

class EmployeeForm(forms.ModelForm):
    countryList = (
        ('EN','England'),
        ('FR','France'),
        ('JP','Japan'),
        )
    country = forms.ChoiceField(label="Select Country",choices=countryList)
    class Meta:
        model = Employee
        fields = "__all__"
        
        