from test_app.models import Product
import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db

@pytest.mark.urls('test_app.urls')
def test_demo(client, settings):
      settings.DEBUG = True
      url = reverse("test_endpoint")
      response = client.get(url)
      assert response.status_code == 200

