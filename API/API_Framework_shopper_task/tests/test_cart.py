from api_pages.cart.cart_api import CartApi
from utils.read_data import read_json

cart_api = CartApi()

def test_add_to_cart(auth_data,headers):
    payload = read_json("test_data/cart_data.json")
    shopper_id = auth_data["shopper_id"]
    response = cart_api.add_to_cart(headers,payload,shopper_id)
    assert response.status_code in [200,409]
    global itemId
    itemId = response.json()["data"][0]["itemId"]

def test_get_cart(auth_data,headers):
    shopper_id = auth_data["shopper_id"]
    response = cart_api.get_cart(headers,shopper_id)
    assert response.status_code == 200

def test_update_cart(auth_data,headers):
    shopper_id = auth_data["shopper_id"]

