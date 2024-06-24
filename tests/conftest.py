import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user_model():
    User = get_user_model()
    return User


@pytest.fixture
def user_factory(user_model):
    def create_user(**kwargs):
        return user_model.objects.create_user(**kwargs)

    return create_user


@pytest.fixture
def admin_user(user_factory):
    return user_factory(
        email="admin@test.com", password="admin", is_staff=True, is_superuser=True
    )


@pytest.fixture
def logged_in_client(client, admin_user):
    client.force_login(admin_user)
    return client
