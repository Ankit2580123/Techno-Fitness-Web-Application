from rest_framework import serializers
from exercise.models import *

class ExerciseSerializer(serializers.Serializer):
    class meta:
            model:ExerciseApis
            fields= '__all__' 