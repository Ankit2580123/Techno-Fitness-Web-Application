"""
URL configuration for GymManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import *
from nutrition_track.views import *
from exercise.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # for Home Apps
    path('',homepage,name="homepage"),
    path('feedback/',feedback,name="feedback"),
    path('enquiry/',enquiry,name="enquiry"),
    path('admin_login/', admin_login, name='admin_login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('logout/',admin_logout,name='logout'),
    path('online_booking/',online_booking_page,name='online_booking'),
    path('about',about_page,name='about'),
    path('pricing',price_page,name='pricing'),
    path('schedule',schedule_page,name='schedule'),
    path('all_feedbacks',all_feedbacks,name='all_feedback'),

    #For Admin
    
    path('change_password',changePassword,name='change_password'),
    path('delete_enquiry<int:pid>',delete_enquiry,name='delete_enquiry'),
    path('show_feedback',show_feedback,name='show_feedback'),
    path('delete_feedbacks<int:id>',delete_feedbacks,name='delete_feedbacks'),
    path('total_gymmembers',gym_members_page,name='total_gymmembers'),
    path('all_bookings/',show_all_bookings,name='all_bookings'),
    path('delete_booking<int:id>',delete_bookings,name='delete_bookings'),
    path('delete_member<int:id>',delete_members,name='delete_members'),
    path('update_member<int:id>',update_members,name='update_members'),

    path('export_data',export_data_to_excel,name='export_data'),

    path('equipment_page',equipments,name='equipments'),
    path('delete_equip<int:id>',delete_equipments,name='delete_equip'),



    # path('edit_user<int:id>',edit_members,name='edit_users'),

    # path('edit_user<int:id>',edit_members,name='edit_users'),

    
    path('admin/', admin.site.urls),


    #for nutrition_track Apps
    path('nutrition_track',nutritions_page,name="nutrition_track"),



    #for Exercise Apps
    # path('exercise_page',exercise,name='exercise_page'),
    path('send_exercise',send_exercise,name='send_exercise'),
    path('api/v1/',include('exercise.urls'))
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)