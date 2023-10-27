from django.shortcuts import render
from .models import Product
import json
from django.http import JsonResponse
from django.core.serializers import serialize

def home(request):
      qs = Product.objects.all()
      serialized_data = serialize("json", qs)
      serialized_data = json.loads(serialized_data)
      return JsonResponse(serialized_data, safe=False, status=200)