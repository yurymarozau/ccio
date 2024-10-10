import random

import pytest
from django.test.client import RequestFactory


@pytest.fixture
def group_name(faker):
    return faker.pystr()

@pytest.fixture
def permissions(faker):
    return [faker.pystr() for _ in range(random.randint(2, 5))]

@pytest.fixture
def request_factory():
    return RequestFactory()
