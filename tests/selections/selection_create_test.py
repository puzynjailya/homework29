import pytest

from advertisements.serializers import AdvertisementListSerializer
from tests.factories import AdvertisementFactory


@pytest.mark.django_db
def test_create_selection(client, advertisement, user, get_user_token):

    expected_result = {
        "id": 1,
        "name": "test_selection",
        "owner": user.pk,
        "items": [advertisement.id]
    }
    data={
        "name": "test_selection",
        "owner": user.pk,
        "items": [advertisement.id]
    }
    response = client.post('/selection/create/',
                           data=data,
                           content_type="application/json",
                           HTTP_AUTHORIZATION="Bearer " + get_user_token)

    assert response.status_code == 201
    assert response.data == expected_result