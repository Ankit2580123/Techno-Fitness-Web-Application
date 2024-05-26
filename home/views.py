from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import *
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q,Sum
import pandas as pd
import string
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def homepage(request):
    program=Programs.objects.all()
    gallery_img=Gallery.objects.all()[0:3]
    reviews=Reviews.objects.all().order_by('-stars')[0:3]
    feedback=Reviews.objects.all().count()
    hero_banner=HeroBanner.objects.all()[:1]
    members=TotalMember.objects.all().count()
    equip=Equipments.objects.all().count()

    return render(request,'index.html',{'data':program, 'gallery_img':gallery_img,
                           'feedbacks':reviews,  'hero_img':hero_banner,
                           'total_feedback_counts':feedback,
                           'member_cnt':members,'equip_cnt':equip,

                 } )

def feedback(request):
    if request.method=="POST":
        data=request.POST
        name=data.get('name')
        stars=data.get('stars')
        message=data.get('message')
        Reviews.objects.create(
            name=name,
            stars=stars,
            message=message
        )
        messages.success(request,"Successfully Feedback Post")
    return render(request,'feedback.html')


def all_feedbacks(request):
    obj=Reviews.objects.all()
    return render(request,'all_feedback.html',{'data':obj})

def enquiry(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile_no=request.POST['number']
        message=request.POST['message']

        Enquiry.objects.create(
            name=name,
            email=email,
            phone_no=mobile_no,
            message=message
        )
        email_subject = "Techno Fitness"
        email_message = f"Dear {name} \n\nI hope this message finds you well. You are interested in joining our gym and would you like to learn more about the membership options, offer, including pricing and any special promotions currently available.\n\n Thank you for your time."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,] 
        send_mail(email_subject, email_message, email_from, recipient_list)
        messages.success(request,"Thanks for Contact us we will contact you soon.")
        return redirect('homepage')
        

    return render(request,'enquiry.html')

def admin_login(request):
    if request.method=="POST":
        
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)

        try:
            if user.is_staff:
                login(request,user)
                messages.success(request,"Admin Successfully Login")
                return redirect('admin_dashboard')
                
        except Exception as e:
            messages.error(request,"Wrong Password")
            print(e)
    return render(request,'admin_login.html')

@login_required(login_url='admin_login')
def admin_dashboard(request):

    online_registers=OnlineBookings.objects.all().count()
    enquiry_cnt=Enquiry.objects.all().count()
    enquiry_obj=Enquiry.objects.all()
    feedback=Reviews.objects.all().count()
    total_members=TotalMember.objects.all().count()
    equip=Equipments.objects.all().count()
    search=request.GET.get('search')
    if request.GET.get('search'):
        enquiry_obj=enquiry_obj.filter(

              Q(name__startswith = search) |
              Q(name__icontains = search) 
        )




    paginator = Paginator(enquiry_obj, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    
    return render(request,'dashboard.html',{
            'reg_count':online_registers,
            'enq_count':enquiry_cnt,
            'enquiry_data':enquiry_obj,
            'feedback_count':feedback,
            "enquiry_obj": page_obj,
            'members_count':total_members,
            'equip_cnt':equip,

    })





def admin_logout(request):
    logout(request)
    messages.success(request,"Logged Out")
    return redirect('homepage')



def delete_enquiry(request,pid):
    queryset=Enquiry.objects.get(id=pid)
    queryset.delete()
    return redirect('admin_dashboard')


def online_booking_page(request):
    if request.method=="POST":  
        name=request.POST['name']
        age=request.POST['age']
        phone_no=request.POST['phone_no']
        email=request.POST['email']
        plans=request.POST['plans']

        OnlineBookings.objects.create(
            name=name,
            age=age,
            phone_no=phone_no,
            email=email,
            plan=plans
        )
        messages.success(request,"Booked Successfully We will Contact Soon!")
        return redirect('homepage')

    return render(request,'online_booking.html')

def about_page(request):
    return render(request,'about.html')

def price_page(request):
    return render(request,'price.html')

def schedule_page(request):
    return render(request,'schedule.html')

#Admin Pannel
@login_required(login_url='admin_login')
def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('homepage')
    user = request.user
    if request.method == "POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password=request.POST['confirm_password']
        if(new_password!=confirm_password):
            messages.error(request,"Your new Password not matched with Confirm Password Enter Again.")
            return redirect('change_password')
        else:

            try:
                u = User.objects.get(id=request.user.id)
                if user.check_password(old_password):
                    u.set_password(new_password)
                    u.save()
                    messages.success(request,"Password Changed Successfully")
            except Exception as e:
                error = e
    return render(request,'change_password.html')


@login_required(login_url='admin_login')
def show_feedback(request):

    feedbacks_obj=Reviews.objects.all().order_by('-stars')


    paginator = Paginator(feedbacks_obj, 8)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request,'show_feedback.html',{'data':page_obj})

def delete_feedbacks(request,id):
    obj=Reviews.objects.get(id=id)
    obj.delete()
    messages.success(request,"Record Deleted Successfully")
    return redirect('show_feedback')


@login_required(login_url='admin_login')
def gym_members_page(request):
        
    obj=TotalMember.objects.all()

    search=request.GET.get('search')

    if request.GET.get('search'):
        obj=TotalMember.objects.filter(

              Q(name__startswith = search) |
              Q(age__startswith = search) |
              Q(fathers_name__startswith=search) |
              Q(plan__startswith=search ) 
      
        )
    paginator = Paginator(obj, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    paginator = Paginator(obj, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    if request.method=="POST":  
        name=request.POST['name']
        fathers_name=request.POST['fathers_name']
        phone_no=request.POST['phone_no']
        age=request.POST['age']
        address=request.POST['address']
        plans=request.POST['plan']
        date=request.POST['date']

       
        TotalMember.objects.create(
            name=name,
            fathers_name=fathers_name,
            phone_no=phone_no,
            age=age,
            address=address,
            plan=plans,
            date_of_admissions=date,
        )
        messages.success(request,"Members Added Successfully")
        return redirect('total_gymmembers')
     
    return render(request,'total_members.html',{'members_data':page_obj})

@login_required(login_url='admin_login')
def show_all_bookings(request):

    bookings_obj=OnlineBookings.objects.all()
    search=request.GET.get('search')

    if request.GET.get('search'):
        bookings_obj=bookings_obj.filter(

              Q(name__startswith = search) |
              Q(age__startswith = search) 

        )


    paginator = Paginator(bookings_obj, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    return render(request,'showall_bookings.html',{'bookings_data':page_obj})

def delete_bookings(request,id):
    obj=OnlineBookings.objects.get(id=id)
    obj.delete()
    return redirect('all_bookings')

def delete_members(request,id):
    obj=TotalMember.objects.get(id=id)
    obj.delete()
    messages.success(request,"Members Deleted Successfully")
    return redirect('total_gymmembers')



def update_members(request,id):
        member_obj=TotalMember.objects.get(id=id)

        # context={
        #         'data':member_obj
        # }

        if request.method=="POST":  

            name=request.POST['name']
            fathers_name=request.POST['fathers_name']
            phone_no=request.POST['phone_no']
            age=request.POST['age']
            address=request.POST['address']
            plans=request.POST['plan']     
            date=request.POST['date']


        

            member_obj.name=name
            member_obj.fathers_name=fathers_name
            member_obj.phone_no=phone_no
            member_obj.age=age
            member_obj.address=address
            member_obj.plan=plans
            member_obj.date_of_admissions=date
            member_obj.save()
            messages.success(request,"Record Update Successfully")
            return redirect('total_gymmembers')
            

        return render(request,'editUser.html',{'data':member_obj})


def export_data_to_excel(request):
    objs=TotalMember.objects.all()

    data_list=[]

    for data in objs:
        data_list.append({
            "Name": data.name,
            "Father's Name":data.fathers_name,
            "Phone_no":data.phone_no,
            "Age":data.age,
            "Plan": data.plan,
            "Address":data.address,
            "Date of Admission": data.date_of_admissions
        }
 
        )
    pd.DataFrame(data_list).to_excel('output.xlsx')
    messages.success(request,"Excel File Download Successfully")
    return redirect('total_gymmembers')
  
def equipments(request):

    obj=Equipments.objects.all()
    if request.method=="POST":  
        equipment_name=request.POST['name']
        price=request.POST['price']
        units=request.POST['units']
        desc=request.POST['description']
        purchase_date=request.POST['purchase_date']

       
        Equipments.objects.create(
            name=equipment_name,
            price=price,
            unit=units,
            description=desc,
            purchase_date=purchase_date,   
        )
        messages.success(request,"Equipments Added Successfully")
        return redirect('equipments')
    
    paginator = Paginator(obj, 8)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
        
    return render(request,'equipment.html',{'equipment_data':page_obj})

def delete_equipments(request,id):
    obj=Equipments.objects.filter(id=id)
    obj.delete()
    messages.success(request,"Equipments Deleted")
    return redirect('equipments')
