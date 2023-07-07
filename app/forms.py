from django import forms
class SignUpForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=10,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea)
    gender=forms.ChoiceField(choices=[('male','MALE'),('female','FEMALE')])
    