import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_login(client, admin_user):
    url = reverse("login")
    response = client.post(
        url,
        {"username": "admin@test.com", "password": "admin"},
        content_type="application/json",
    )
    assert response.status_code == 200

    assert response.json() == {"detail": "Successfully logged in."}


@pytest.mark.django_db
def test_login_bad_user(client, admin_user):
    url = reverse("login")
    response = client.post(
        url,
        {"username": "idontexists@test.com", "password": "admin"},
        content_type="application/json",
    )
    assert response.status_code == 400

    assert response.json() == {"detail": "Invalid credentials."}


@pytest.mark.django_db
def test_logout(logged_in_client):
    url = reverse("logout")
    response = logged_in_client.get(url)
    assert response.status_code == 200
    assert response.json() == {"detail": "Successfully logged out."}


@pytest.mark.django_db
def test_logout_unauthenticated_request(client):
    url = reverse("logout")
    response = client.get(url)
    assert response.status_code == 400
    assert response.json() == {"detail": "You're not logged in."}


@pytest.mark.django_db
def test_get_current_user(logged_in_client):
    url = reverse("current-user")
    response = logged_in_client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["isStaff"]


@pytest.mark.django_db
def test_get_current_user_unauthenticaded_request(client):
    url = reverse("current-user")
    response = client.get(url)
    assert response.status_code == 403


def test_get_csrf(client):
    url = reverse("get-csrf")
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == {"detail": "CSRF cookie set"}
    assert "X-CSRFToken" in response
    assert response["X-CSRFToken"]
