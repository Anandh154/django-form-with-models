from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
# Create your views here.
def django_form(request):
    SUFO=SignUpForm()
    d={'sufo':SUFO}
    if request.method=='POST':
        SFDT=SignUpForm(request.POST)
        if SFDT.is_valid():
            n=SFDT.cleaned_data.get('name')
            a=SFDT.cleaned_data['age']
            e=SFDT.cleaned_data['email']
            pw=SFDT.cleaned_data['password']
            ad=SFDT.cleaned_data['address']
            g=SFDT.cleaned_data['gender']
            SO=SignForm.objects.get_or_create(name=n,age=a,password=pw,address=ad,gender=g)[0]
            SO.save()
            return HttpResponse(str(SFDT.cleaned_data))
    return render(request,'django_form.html',d)