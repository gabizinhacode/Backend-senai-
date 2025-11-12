from django.shortcuts import render
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import api_view



@api_view(['GET'])
def listar_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criar_task(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response (serializer.data, status=201)
    return Response(serializer.errors, status=400)




# Create your views here.