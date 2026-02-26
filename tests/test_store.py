import pytest
import allure
from base_request import BaseRequest
from models import OrderModel

BASE_URL = "https://petstore.swagger.io/v2"
base_request = BaseRequest(BASE_URL)

order_id = 9999

@allure.feature("Store")
@allure.story("Create Order")
def test_create_order():
    order_body = OrderModel(
        id=order_id,
        petId=1,
        quantity=1,
        shipDate="2026-02-25T10:00:00.000Z",
        status="placed",
        complete=True
    ).model_dump()
    response = base_request.post("store/order", "", order_body)
    allure.attach(str(response), name="POST Response", attachment_type=allure.attachment_type.JSON)

    # Проверка через GET
    order_info = base_request.get("store/order", order_id)
    allure.attach(str(order_info), name="GET Response", attachment_type=allure.attachment_type.JSON)
    assert order_info["id"] == order_id


@allure.feature("Store")
@allure.story("Delete Order")
def test_delete_order():
    base_request.delete("store/order", order_id)
    response = base_request.get("store/order", order_id, expected_error=True)
    allure.attach(str(response), name="GET Response after Delete", attachment_type=allure.attachment_type.JSON)
    assert response is not None