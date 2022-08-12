from tests.factories import UserFactory, CategoryFactory, AdvertisementFactory
from pytest_factoryboy import register

pytest_plugins = "tests.fixtures"

register(AdvertisementFactory)
register(CategoryFactory)
register(UserFactory)
