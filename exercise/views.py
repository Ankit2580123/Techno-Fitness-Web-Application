from django.shortcuts import render
from exercise.models import *
import requests
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
import json
from django.contrib import messages
from rest_framework import serializers,viewsets
from exercise.serializers import ExerciseSerializer


Api_key='DHvQPkdabpi9NfYwIBiu6NRxKekXD6elzWvF9uB6'

def send_exercise(request):

    if request.method=='POST':
        user_name=request.POST['name']
        email=request.POST['email']
        exercise_choice=request.POST['exercise_choice']
        print(exercise_choice)
        
    
        api_url='https://api.api-ninjas.com/v1/exercises?muscle='
        api_request=requests.get(api_url + exercise_choice, headers={'X-Api-Key':Api_key})

    
        api_data = api_request.json()
        # print(api_data)
       
        

    # print(api)
        name_list=[]
        for item in api_data:
        # Assuming 'name' is a key in each item
            name = item.get("name")
            if name:
                name_list.append(name) 
            
    
        
        email_subject = "API Data Notification"
        email_message = f"Hello {user_name} \nHere is the List of Exercise For {exercise_choice} \n\n {name_list} \n\n Thank You"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,] 
        send_mail(email_subject, email_message, email_from, recipient_list)
        messages.success(request,"We are Send a Exercise plan on your entered gmail,Check Your Mail")
        
    return render(request,"send_exercise.html")




class ExerciseViewSet(viewsets.ModelViewSet):
    queryset=ExerciseApis.objects.all()
    serializer_class=ExerciseSerializer

        


     
       
