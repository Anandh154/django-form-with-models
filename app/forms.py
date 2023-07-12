from django import forms
from django.core import validators
class SignUpForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=10,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea)
    gender=forms.ChoiceField(choices=[('male','MALE'),('female','FEMALE')])

def val_for_a(sname):
    if sname[0].lower()=='a':
        raise forms.ValidationError('it should not with a')
    
def val_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError('name is less than 5')

class Student_Form(forms.Form):
    sname=forms.CharField(max_length=100,validators=[val_for_a,validators.MinLengthValidator(5)])
    sage=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    # mob=forms.CharField(max_length=10)
    bot=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    url=forms.URLField()
    mob=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']
        if e!=re:
            raise forms.ValidationError('email is not match')
        
    def clean_bot(self):
        b=self.cleaned_data['bot']
        if len(b)>0:
            raise forms.ValidationError('ghjjhgfdsd')