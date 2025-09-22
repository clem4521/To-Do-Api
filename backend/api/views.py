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

@api_view(["POST"])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(["DELETE"])
def delete_task(request,pk=None):
    modelData = Task.objects.get(pk=pk)
    modelData.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)