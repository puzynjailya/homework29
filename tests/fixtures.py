import pytest


@pytest.fixture()
@pytest.mark.django_db
def get_user_token(client, django_user_model):
    username = 'test_user'
    password = 'qwerty123'
    role = 'admin'
    email = 'test@test.com'
    age = 22
    birth_date = "2000-01-01"
    is_superuser = False

    django_user_model.objects.create_user(
        username=username,
        password=password,
        role=role,
        email=email,
        age=age,
        birth_date=birth_date,
        is_superuser=is_superuser,
    )

    response = client.post(
        "/user/token/",
        {"username": username,
         "password": password},
        content_type='application/json'
    )

    return response.data["access"]
