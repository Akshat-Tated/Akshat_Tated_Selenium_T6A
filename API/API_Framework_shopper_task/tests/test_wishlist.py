from api_pages.wishlist.wishlist_api import WishlistAPI
from utils.read_data import read_json

wishlist_api = WishlistAPI()

def test_add_to_wishlist(auth_data,headers):
    shopper_id = auth_data["shopper_id"]
    payload = read_json("test_data/wishlist_data.json")

    response = wishlist_api.add_to_wishlist(shopper_id,headers,payload)
    assert response.status_code in [200, 409,201]
