import pytest

from advertisements.serializers import AdvertisementListSerializer
from tests.factories import AdvertisementFactory


@pytest.mark.django_db
def test_get_advertisements_list(client, get_user_token):
    advertisements = AdvertisementFactory.create_batch(10)

    expected_result = {
        "count": 10,
        "next": None,
        "previous": None,
        "results": AdvertisementListSerializer(advertisements, many=True).data
    }

    response = client.get("/ad/", HTTP_AUTHORIZATION="Bearer " + get_user_token)

    assert response.status_code == 200
    assert response.data == expected_result
