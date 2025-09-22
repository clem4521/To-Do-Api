from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer
# Create your views here.
def test(request):
    return HttpResponse("Test")
    
@api_view(["GET"])
def getTasks(request):
    modelData = Task.objects.all();
    serializer = TaskSerializer(modelData,many=True)
    
    return Response(serializer.data,status=status.HTTP_200_OK)
