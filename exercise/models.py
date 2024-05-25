from django.db import models

# Create your models here.
class Exercise(models.Model):
    exercise_img=models.ImageField(upload_to="Exercise_images")
    muscles_name=models.CharField(max_length=15)
    message=models.CharField(max_length=80)

    def __str__(self) -> str:
        return f'{self.muscles_name} {self.message}'
    
    class Meta:

         ordering=['muscles_name']

class ExerciseApis(models.Model):
    exercise_id=models.AutoField(primary_key=True)
    muscles=models.CharField(max_length=50)
    img=models.ImageField(upload_to='Exercise_img_apis')
    exercise_name=models.CharField(max_length=60)
    equipment_required=models.CharField(max_length=50)