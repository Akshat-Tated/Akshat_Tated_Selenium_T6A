from core.base_api import BaseAPI
from utils.config import BASE_URL
from conftest import headers

class CartApi:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def add_to_cart(self,headers,payload,shopper_id):
        return self.api.post(
            f"/shoppers/{shopper_id}/carts",
            headers=headers,
            json=payload
        )
    def get_cart(self,headers,shopper_id):
        return self.api.get(
            f"/shoppers/{shopper_id}/carts",
            headers=headers,
        )

    def update_cart(self,headers,shopper_id,itemid,payload):
        return self.api.put(
            f"/shoppers/{shopper_id}/carts/{itemid}",
            headers=headers,
            json=payload
        )