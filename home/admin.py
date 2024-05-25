from django.contrib import admin
from .models import *
from exercise.models import *


# Register your models here.
admin.site.register(Enquiry)
admin.site.register(Plans)

admin.site.register(Programs)
admin.site.register(Gallery)
admin.site.register(Reviews)
admin.site.register(OnlineBookings)
admin.site.register(HeroBanner)
admin.site.register(TotalMember)
admin.site.register(Equipments)




##Exercise Apps
admin.site.register(Exercise)
admin.site.register(ExerciseApis)


