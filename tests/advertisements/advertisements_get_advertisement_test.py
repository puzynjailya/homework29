import pytest

@pytest.mark.django_db
def test_get_advertisement_by_id(client, advertisement,get_user_token):

    expected_result = {
        "id": advertisement.pk,
        "name": advertisement.name,
        "author": advertisement.author_id,
        "price": advertisement.price,
        "description": advertisement.description,
        "is_published": False,
        "category": advertisement.category_id,
        "image": None
    }

    response = client.get(f'/ad/{advertisement.pk}/', HTTP_AUTHORIZATION="Bearer " + get_user_token)

    assert response.status_code == 200
    assert response.data == expected_result