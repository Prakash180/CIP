from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.
# from sklearn.externals import joblib

import joblib
import models
import pickle
import models

# pickle.dump(open('./models/rffile.pkl', 'wb'))

reloadmodel=joblib.load('./models/rffilef.pkl')

def index(request):
    context={'a':'hello world'}
    return render(request,'index.html',context)

def predictHDisease(request):
    print(request)
    if request.method == 'POST':
       temp=[[]]
       age=request.POST.get('age')
       sex=request.POST.get('sex')
       chest_pain_type=request.POST.get('cp')
       blood_pressure=request.POST.get('bp')
       cholesterol=request.POST.get('chol')
       fasting_bloods_lvl=request.POST.get('fbs')
       ECG_results=request.POST.get('ecg')
       max_heart_rates=request.POST.get('maxhr')
       anigma=request.POST.get('EIA')
       ST_depression=request.POST.get('ST')
       slope_ST=request.POST.get('slopest')
       fluoro=request.POST.get('nov')
       thallium=request.POST.get('thal')
       temp=[[age,sex,chest_pain_type,blood_pressure,cholesterol,fasting_bloods_lvl,ECG_results,max_heart_rates,anigma,ST_depression,slope_ST,fluoro,thallium]]
       print(temp)
       predictvalue=reloadmodel.predict(temp)
       print(predictvalue[0])
       ans=predictvalue[0]

    if predictvalue[0]==1:
        print("heart disease detected")
        result="WARNING!!! HEART DISEASE DETECTED"
    elif predictvalue[0]==0:
        print("heart disease not detected")
        result="HEART DISEASE NIL"
 
    context ={'result':result}
    return render(request,'index.html',context)

     