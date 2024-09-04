from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_objetc_or_404
from .models import Tasks
from .serializers import TaskSerializer


@api_view(['GET'])
def task_list(request):
	try:
		tasks = Tasks.objects.filter(owner=request.user)
		serializer = TaskSerializer(tasks, many=True)
		return Response(serializer.data)
	except:
		content = 'Unknown user credentials.'
		return Response(content, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def task_detail(request, pk):
	try:
		task = Tasks.objects.get(id=pk, owner=request.user)
		serializer = TaskSerializer(task, many=False)
		return Response(serializer.data)
	except:
		return Response('You are not allowed to see this task.')


@api_view(['POST'])
def task_create(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	return Response(serializer.errors)


@api_view(['POST'])
def task_update(request, pk):
	task = Tasks.objects.get(id=pk, owner=request.user)
	serializer = TaskSerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	return Response(serializer.errors)


@api_view(['DELETE'])
def task_delete(request, pk):
	task = Tasks.objects.get(id=pk, owner=request.user)
	task.delete()
	return Response("Task has been deleted successfully.")
