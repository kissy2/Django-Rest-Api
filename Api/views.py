from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer

from .models import Note
# Create your views here.

@api_view(['GET'])
def apiEntrypoints(request):
	api_urls = {
		'List':'/list/',
		'Get':'/get/<str:pk>/',
		'Create':'/create/',
		'Update':'/update/<str:pk>/',
		'Delete':'/delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def NoteList(request):
	Notes = Note.objects.all().order_by('-id')
	serializer = NoteSerializer(Notes, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def NoteDetail(request, pk):
	Notes = Note.objects.get(id=pk)
	serializer = NoteSerializer(Notes, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def NoteCreate(request):
	serializer = NoteSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def NoteUpdate(request, pk):
	Note_instance = Note.objects.get(id=pk)
	serializer = NoteSerializer(instance=Note_instance, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def NoteDelete(request, pk):
	Note_instance = Note.objects.get(id=pk)
	serializer = NoteSerializer(instance=Note_instance, data=request.data)

	Note_instance.delete()

	if serializer.is_valid():
		return Response(serializer.data)




