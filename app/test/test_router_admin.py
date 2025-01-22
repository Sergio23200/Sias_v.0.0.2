from fastapi.testclient import TestClient
from schemas.admin_schema import Admin_schema, admin_filter_schema, Admin_update
from main import app

client = TestClient(app)

user_v = Admin_schema(
    fullname="andres sergio alarcon cardozo",
    document_number=10357481,
    document_type="cedula",
    birthdate="2004-03-23",
    email="andres.cardozo.car@gmail.com",
    first_number="3144331848",
    city="Bogota",
    password="Sergi@123",
    job_title="admin"
)

filter_v = admin_filter_schema(
    id=1,
    fullname="sergio andres alarcon cardozo",
    document_number=1034776533,
    email="sergio.alarcon.car@gmail.com",
    city="Bogotá",
    job_title="admin"
)
update_v = Admin_update(
    email="sergio.alarcon.car@gmail.com",
    first_number="3223205296",
    city="medellin",
    password="Sergi@123",
    job_title="director"
)


def test_create_admin_success():

    data = user_v.model_dump()

    data["birthdate"] = str(user_v.birthdate)

    response = client.post(
        "/create/admin",
        json=data,
        headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJzZXJnaW8uYWxhcmNvbi5jYXJAZ21haWwuY29tIn0.LuQLr-wBrPpXWezQY1RU5eTjdsmY8d_U0X3nv-NRzdg"}
    )

    assert response.status_code == 200
    assert response.json()["mensage"] == "el usuario se ha registrado"


def test_create_admin_failure():
    data = user_v.model_dump()
    if "birthdate" in data:
        data["birthdate"] = str(data["birthdate"])

    data["password"] = str(user_v.password)

    response = client.post(
        "/create/admin",
        json=data,
        headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJzZXJnaW8uYWxhcm9jbi5jYXJAZ21haWwuY29tIn0.MB1Q1qLuMgK6Y29dWwTEYJQlKRfgabaJzHHqaUSUtdA"}
    )

    assert response.status_code == 200
    assert response.json()["mensage"] == "el usuario no tiene permisos"


def test_all_admin_sucess():
    response = client.get(
        "/all/admin",
        headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJzZXJnaW8uYWxhcmNvbi5jYXJAZ21haWwuY29tIn0.LuQLr-wBrPpXWezQY1RU5eTjdsmY8d_U0X3nv-NRzdg"}
    )

    assert response.status_code == 200

    response_data = response.json()
    assert len(response_data) > 0
    assert isinstance(response_data, list)


def test_filter_admin_success():
    data = filter_v.model_dump()

    response = client.get(
        "/filters/admin",
        params=data,
        headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJzZXJnaW8uYWxhcmNvbi5jYXJAZ21haWwuY29tIn0.LuQLr-wBrPpXWezQY1RU5eTjdsmY8d_U0X3nv-NRzdg"}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) > 0
    assert isinstance(response_data, list)


def test_update_admin_success():
    data = update_v.model_dump()
    response = client.put("/update/admin",
                          json=data,
                          headers={
                              "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJzZXJnaW8uYWxhcmNvbi5jYXJAZ21haWwuY29tIn0.LuQLr-wBrPpXWezQY1RU5eTjdsmY8d_U0X3nv-NRzdg"})
    assert response.status_code == 200
    assert response.json()["mensage"] == "EL admin ha sido actualizado"


def test_delete_admin_success():
    response = client.delete("/dalete/admin",
                             headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJzZXJnaW8uYWxhcmNvbi5jYXJAZ21haWwuY29tIn0.LuQLr-wBrPpXWezQY1RU5eTjdsmY8d_U0X3nv-NRzdg"})
    assert response.status_code == 200
    assert response.json()["mensage"] == "el admin ha sido eliminados"
