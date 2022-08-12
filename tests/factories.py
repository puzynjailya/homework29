import factory.django
from django.contrib.auth import get_user_model

from advertisements.models import Advertisement
from categories.models import Category
from selections.models import Selection


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "testing"
    slug = factory.Faker('word')


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Faker("name")
    password = 'qwerty123'
    role = 'admin'
    email = factory.Faker("email")
    age = 22
    birth_date = "2000-01-01"
    is_superuser = False


class AdvertisementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Advertisement

    name = "test_advertisement"
    author = factory.SubFactory(UserFactory)
    price = 100500
    description = "test_description"
    category = factory.SubFactory(CategoryFactory)