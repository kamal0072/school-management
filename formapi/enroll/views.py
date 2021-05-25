from django.shortcuts import render
from .forms import Studentform,ExampleForm

def homeview(request):
    stufm=Studentform()
    stuexm=ExampleForm()
    # stufm=Studentform(auto_id='kamal') 
    # stufm=Studentform(
    #     auto_id='some_%s',
    #     label_suffix=' ',
    #     initial={'name':'Enter Your Name','address':'Enter a valid address',
    #     'email':'abc@gmail.com'}
    #     )    
    return render(request,'enroll/home.html',{'fm':stufm,'fm2':stuexm})

def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'enroll/map.html', {'mapbox_access_token':mapbox_access_token})