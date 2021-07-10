from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


@api_view(["GET"])
def api_overview(request):
    api_urls = [
        {"List": "/api/list",
        "Create": "api/create",
        "Update": "api/update",
        "Delete": "api/delete"}
    ]
    return Response(api_urls)

@api_view(["GET"])
def task_list(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def detail_view(request, id):
    task = Task.objects.get(pk=id)
    serializer = TaskSerializer(many=False)
    return Response(serializer.data)

@api_view(["POST"])
def task_create(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def task_update(request, pk):
    task = Task.objects.get(pk=id)
    serializer = TaskSerializer(instance = task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def task_delete(request, pk):
    task = Task.objects.get(pk=id)
    task.delete()
    return Response("TASK DELETED")