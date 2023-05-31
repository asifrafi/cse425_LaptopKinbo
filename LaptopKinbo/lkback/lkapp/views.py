from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from lkapp.models import Laptop
from lkapp.serializers import LaptopSerializer
# Create your views here.

@csrf_exempt
def api_list(request):
    if request.method == 'GET':
        laps = Laptop.objects.all()
        serializer = LaptopSerializer(laps, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)