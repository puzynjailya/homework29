import pytest
from django.contrib.auth import get_user_model

from categories.models import Category


@pytest.mark.django_db
def test_create_advertisement(client, get_user_token):
    expected_result = {
        "name": "test_advertisement",
        "author": 1,
        "price": 100500,
        "description": "test_description",
        "is_published": False,
        "category": 1,
        "author": 1
    }

    Category.objects.create(name="testing", slug="testing")

    data = {
        "name": "test_advertisement",
        "author": 1,
        "price": 100500,
        "description": "test_description",
        "category": 1
    }

    response = client.post('/ad/create/',
                           data=data,
                           content_type="application/json",
                           HTTP_AUTHORIZATION="Bearer " + get_user_token)

    assert response.status_code == 201
    assert response.data == expected_result
