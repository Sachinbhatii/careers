from django.db.models import fields
from rest_framework import serializers
from .models import Careers #, Jobs
from careersapp import models


# class JobSerializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = Jobs
#         fields = '__all__'

class CareersSerializers(serializers.ModelSerializer):
    # jobs = JobSerializers(many=True, read_only=True )
    class Meta:
        model = Careers
        fields = '__all__'