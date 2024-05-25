from django.contrib import admin
from django.urls import path,include
from exercise.views import ExerciseViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'exercise',ExerciseViewSet)

urlpatterns = [
    path('',include(router.urls))
]



