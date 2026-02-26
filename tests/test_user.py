import pytest
import allure
from base_request import BaseRequest
from models import UserModel

BASE_URL = "https://petstore.swagger.io/v2"
base_request = BaseRequest(BASE_URL)

username = "esket1"

@allure.feature("User")
@allure.story("Create User")
def test_create_user():
    user_body = UserModel(
        id=101,
        username=username,
        firstName="Dan",
        lastName="Baykov",
        email="baykovdr23@st.ithub.ru",
        password="12345",
        phone="1234567890",
        userStatus=1
    ).model_dump()  # для Pydantic v2
    response = base_request.post("user", "", user_body)
    allure.attach(str(response), name="POST Response", attachment_type=allure.attachment_type.JSON)

    # Проверка через GET
    user_info = base_request.get("user", username)
    allure.attach(str(user_info), name="GET Response", attachment_type=allure.attachment_type.JSON)
    assert user_info["username"] == username


@allure.feature("User")
@allure.story("Update User")
def test_update_user():
    updated_body = UserModel(
        id=101,
        username=username,
        firstName="UpdatedDan",
        lastName="Baykov",
        email="baykovdr23@st.ithub.ru",
        password="12345",
        phone="1234567890",
        userStatus=1
    ).model_dump()
    response = base_request.put("user", username, updated_body)
    allure.attach(str(response), name="PUT Response", attachment_type=allure.attachment_type.JSON)

    # Проверка через GET
    user_info = base_request.get("user", username)
    allure.attach(str(user_info), name="GET Response after Update", attachment_type=allure.attachment_type.JSON)
    assert user_info["firstName"] == "UpdatedDan"


@allure.feature("User")
@allure.story("Delete User")
def test_delete_user():
    base_request.delete("user", username)
    response = base_request.get("user", username, expected_error=True)
    allure.attach(str(response), name="GET Response after Delete", attachment_type=allure.attachment_type.JSON)
    assert response is not None