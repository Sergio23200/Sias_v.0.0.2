from fastapi.testclient import TestClient
from fastapi import HTTPException
from routers.login import login_router
import pytest
from unittest.mock import patch, MagicMock

client = TestClient(login_router)


def mock_vericate_afilate_success(email, password):
    mock_affiliate = MagicMock()
    mock_affiliate.id = 1
    mock_affiliate.password = password
    mock_affiliate.email = email
    return mock_affiliate


def mock_verificate_admin_success(email, password):

    mock_admin = MagicMock()
    mock_admin.id = 1
    mock_admin.password = password
    mock_admin.email = email
    return mock_admin


def mock_verificate_admin_failure(email, password):
    return None


def mock_verificate_afiliate_failure(email, password):
    return None


@patch("services.affiliate_services.Affiliate_service.vericate_afilate", side_effect=mock_vericate_afilate_success)
def test_login_affiliate_success(mock_vericate_afilate):
    response = client.get(
        "/login",
        params={"email": "affiliate@example.com",
                "password": "correct_password"}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    assert response_data["token_type"] == "bearer"
    assert response_data["user_type"] == "affiliate"


@patch("services.admin_services.Admin_service.verificate_admin", side_effect=mock_verificate_admin_success)
def test_login_admin_success(mock_verificate_admin):
    response = client.get(
        "/login",
        params={"email": "affiliate@example.com",
                "password": "correct_password"}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    assert response_data["token_type"] == "bearer"
    assert response_data["user_type"] == "admin"


@patch("services.admin_services.Admin_service.verificate_admin", side_effect=mock_verificate_admin_failure)
def test_login_failure_admin(mock_verificate_admin):
    with pytest.raises(HTTPException) as excinfo:
        response = client.get(
            "/login",
            params={"email": "invalid@example.com",
                    "password": "wrong_password"}
        )

    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "El usuario no está registrado"


@patch("services.affiliate_services.Affiliate_service.vericate_afilate", side_effect=mock_verificate_afiliate_failure)
def test_login_failure_affialte(mock_verificate_admin):

    with pytest.raises(HTTPException) as excinfo:
        response = client.get(
            "/login",
            params={"email": "invalid@example.com",
                    "password": "wrong_password"}
        )

    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == "El usuario no está registrado"
