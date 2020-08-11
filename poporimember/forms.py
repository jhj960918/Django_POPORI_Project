from django import forms
from .models import CustomUser
class LoginForm(forms.ModelForm):
    username = forms.ModelChoiceField(
        queryset = CustomUser.objects.all(),
        label = 'id를 입력하세요',
        required = True,
        widget = forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.ModelChoiceField(
        queryset = CustomUser.objects.all(),
        label = 'password를 입력하세요',
        required = True,
        widget = forms.PasswordInput(attrs={'class':'form-control'})
    )
    class Meta:
        model = CustomUser
        fields = ['username','password']