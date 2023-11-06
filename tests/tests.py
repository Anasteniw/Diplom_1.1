from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_get_category(g_category, client_a):
    """Тест на получение категории товаров"""
    category1 = g_category()
    category2 = g_category()
    url = reverse('backend:categories')
    resp = client_a.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json['count'] == 2


@pytest.mark.django_db
def test_get_shop(client_a, shop_one):
    """Тест получения списка магазинов"""
    shop1 = shop_one()
    shop2 = shop_one()
    url = reverse('backend:shops')
    resp = client_a.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json['count'] == 2


@pytest.mark.django_db
def test_create_user(client_a):
    """Тест создания пользователя"""
    url = reverse('backend:user-register')
    user = {"first_name": "Ivan",
            "last_name": "Ivanov",
            "email": "example@email.ru",
            "password": " ",
            "company": "nord",
            "position": ""
            }
    resp = client_a.post(url, user)
    assert resp.status_code == HTTP_201_CREATED
    resp_json = resp.json()
    assert resp_json['Status'] == True