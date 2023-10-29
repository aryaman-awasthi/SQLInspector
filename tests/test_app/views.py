from .models import Product
from django.http import HttpResponse

def test_endpoint(request):
      qs = Product.objects.all()
      return HttpResponse(qs)