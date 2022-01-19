from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import serializers, viewsets
from .models import Careers#, Jobs
from .serializers import CareersSerializers #, JobSerializers

class careersViewSet(APIView):

    def post(self, request, format=None):
        print(request.data)
        serializer = CareersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    # queryset = Careers.objects.all()
    # serializer_class = CareersSerializers
    


# class jobsViewset(viewsets.ModelViewSet):
#     queryset = Jobs.objects.all()
#     serializer_class = JobSerializers   

def home(request):
    # if request.method == "POST":
        # full_name = request.POST.get('name')
        # email =  request.POST.get('email')
        # resume =  request.POST.get('resume')
        # phone_number = request.POST.get('PhoneNumber')
        # applicant_description = request.POST.get('description')
        # job_description = request.POST.get('job_description')
        # job_title = request.POST.get('job_title')

        # Careers.objects.create(full_name=full_name,phone_number=phone_number,email=email ,applicant_description=applicant_description)
        # Jobs.objects.create(job_description=job_description,job_title=job_title)
    return render(request,'careersapp/home.html')




