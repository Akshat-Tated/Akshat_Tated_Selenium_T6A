import requests

from core.base_api import BaseAPI
from utils.config import BASE_URL

class WishlistAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def add_to_wishlist(self, shopper_id, headers, payload):
        return self.api.post(
            f"/shoppers/{shopper_id}/wishlist",
            headers=headers,
            json=payload
        )

    def get_wishlist(self, shopper_id, headers):
        return self.api.get(
            f"/shoppers/{shopper_id}/wishlist",
            headers=headers
        )
