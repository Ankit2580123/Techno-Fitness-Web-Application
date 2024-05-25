from django.shortcuts import render
import json
import requests
from django.http import HttpResponse


# Create your views here.
api_key='DHvQPkdabpi9NfYwIBiu6NRxKekXD6elzWvF9uB6'
def nutritions_page(request):
    if request.method=='POST':
        query=request.POST['query']
        api_url='https://api.api-ninjas.com/v1/nutrition?query='
        api_request=requests.get(api_url+ query, headers={'X-Api-Key': api_key})
        # response = requests.get(api_url)

        # if response.status_code != 200:
        #        return HttpResponse("Failed to fetch data from the API", status=500)

        try:
            api=json.loads(api_request.content)
        
        except Exception as e:
            api="Ops There was an Error"  

        
   
        return render(request,'nutrition.html',{'food_data':api})
    
    else:
        
        return render(request,'nutrition.html',{'query':"Please Enter Valid Food Name"})


