from django.shortcuts import render
from rest_framework.response import Response
from .models import Eductor
from .serializers import EductorSerializer
from rest_framework import status
from rest_framework import viewsets


class EductorViewSet(viewsets.ViewSet):
 def list(self, request):
  stu = Eductor.objects.all()
  serializer = EductorSerializer(stu, many=True)
  return Response(serializer.data)

 def retrieve(self, request, pk=None):
  id = pk
  if id is not None:
   stu = Eductor.objects.get(id=id)
   serializer = EductorSerializer(stu)
   return Response(serializer.data)

 def create(self, request):
  serializer = EductorSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def update(self,request, pk):
  id = pk
  stu = Eductor.objects.get(pk=id)
  serializer = EductorSerializer(stu, data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Complete Data Updated'})
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def partial_update(self,request, pk):
  id = pk
  stu = Eductor.objects.get(pk=id)
  serializer = EductorSerializer(stu, data=request.data, partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Partial Data Updated'})
  return Response(serializer.errors)

 def destroy(self,request, pk):
  id = pk
  stu = Eductor.objects.get(pk=id)
  stu.delete()
  return Response({'msg':'Data Deleted'})