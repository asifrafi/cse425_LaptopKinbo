from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from lkapp.models import Laptop
from lkapp.serializers import LaptopSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pymongo

def load():
    myclient = pymongo.MongoClient("mongodb+srv://asiflogin:asif321@cluster0.scqzz.mongodb.net/?retryWrites=true&w=majority")
    mydb = myclient["CSE425"]
    mycol = mydb["laptopKinbo"] 
    x= mycol.find()
    for d in x:
        serializer = LaptopSerializer(data=d) 
        if serializer.is_valid():
            serializer.save()
@api_view(['GET', 'POST'])
def api_list(request):
    if request.method == 'GET':
        laps = Laptop.objects.all()
        serializer = LaptopSerializer(laps, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        
        return request.data  
@api_view(['GET'])
def api_game(request, l, h):
    laptops = Laptop.objects.filter(price__gt=l, price__lt=h)

    gaming_laptops = []
    for laptop in laptops:
        if "RTX" in laptop.name.upper() or "GTX" in laptop.name.upper():
            gaming_laptops.append(laptop)

    serializer = LaptopSerializer(gaming_laptops, many=True)
    return Response(serializer.data)
@api_view(['GET', 'POST'])
def laptops_list(request,l,h):
    
    laptops = Laptop.objects.filter(price__gt=l,price__lt=h)
   
    if request.method == 'GET':
        serializer = LaptopSerializer(laptops,many=True)
        
        return Response(serializer.data)
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_detail(request, pk):
    
    try:
        snippet = Laptop.objects.get(pk=pk)
    except Laptop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LaptopSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LaptopSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)