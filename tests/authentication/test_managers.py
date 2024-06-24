import pytest
from django.contrib.auth import get_user_model


User = get_user_model()


@pytest.mark.django_db
def test_create_user(user_model):
    user = user_model.objects.create_user(email="normal@user.com", password="foo")
    assert user.email == "normal@user.com"
    assert user.is_active
    assert user.is_staff == False
    assert user.is_superuser == False

    with pytest.raises(TypeError):
        user_model.objects.create_user()
    with pytest.raises(TypeError):
        user_model.objects.create_user(email="")
    with pytest.raises(ValueError):
        user_model.objects.create_user(email="", password="foo")


@pytest.mark.django_db
def test_create_superuser(user_model):
    admin_user = user_model.objects.create_superuser(
        email="super@user.com", password="foo"
    )
    assert admin_user.email == "super@user.com"
    assert admin_user.is_active
    assert admin_user.is_staff
    assert admin_user.is_superuser

    with pytest.raises(ValueError):
        user_model.objects.create_superuser(
            email="super@user.com", password="foo", is_superuser=False
        )
