from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def home(request):
    producttMainModel_obj = producttMainModel.objects.all()
    serializer=productMainModelSerializer(producttMainModel_obj,many=True)
    return Response({'status':200,"payload":serializer.data})

@api_view(['GET'])
def home1(request):
    productImageModel_obj = productImageModel.objects.all()
    serializer=productImageModelSerializer(productImageModel_obj,many=True)
    return Response({'status':200,"payload":serializer.data})

@api_view(['POST'])
def productMainmodel_post(request):
    producttMainModel_obj = producttMainModel.objects.all()
    serializer=productMainModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def imgview(request,id):
    productImageModel_obj = productImageModel.objects.get(id=id)
    productImageModel_obj.view()
    return Response('image viewed')