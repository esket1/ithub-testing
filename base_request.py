import requests
import pprint


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        while not stop_flag:

            if request_type == 'GET':
                response = requests.get(url)

            elif request_type == 'POST':
                response = requests.post(url, json=data)

            elif request_type == 'PUT':
                response = requests.put(url, json=data)

            else:
                response = requests.delete(url)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True

        # log part
        pprint.pprint(f'{request_type} example')
        pprint.pprint(response.url)
        pprint.pprint(response.status_code)
        pprint.pprint(response.reason)
        pprint.pprint(response.text)
        try:
            pprint.pprint(response.json())
        except:
            pass
        pprint.pprint('**********')

        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'GET', expected_error=expected_error)
        return response.json()

    def post(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'POST', data=body)
        return response.json()

    def put(self, endpoint, endpoint_id, body):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'PUT', data=body)
        return response.json()

    def delete(self, endpoint, endpoint_id):
        url = f'{self.base_url}/{endpoint}/{endpoint_id}'
        response = self._request(url, 'DELETE')
        return response.json()

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'
base_request = BaseRequest(BASE_URL_PETSTORE)


# запросы к user

username = "esket1"

user_body = {
    "id": 101,
    "username": username,
    "firstName": "Dan",
    "lastName": "Baykov",
    "email": "baykovdr23@st.ithub.ru",
    "password": "12345",
    "phone": "1234567890",
    "userStatus": 1
}

# create
create_user = base_request.post('user', '', user_body)

# get
user_info = base_request.get('user', username)
assert user_info['username'] == username

# update
updated_body = user_body.copy()
updated_body["firstName"] = "UpdatedDan"

update_user = base_request.put('user', username, updated_body)

# delete
delete_user = base_request.delete('user', username)

# проверка delete
deleted_user = base_request.get('user', username, expected_error=True)


# запросы к store

order_id = 9999

order_body = {
    "id": order_id,
    "petId": 1,
    "quantity": 1,
    "shipDate": "2026-02-25T10:00:00.000Z",
    "status": "placed",
    "complete": True
}

# create
create_order = base_request.post('store/order', '', order_body)

# get
order_info = base_request.get('store/order', order_id)
assert order_info['id'] == order_id

# delete
delete_order = base_request.delete('store/order', order_id)

# get inventory
inventory_url = f'{BASE_URL_PETSTORE}/store/inventory'
inventory = base_request._request(inventory_url, 'GET')
pprint.pprint(inventory.json())