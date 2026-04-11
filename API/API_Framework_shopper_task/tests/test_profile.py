from api_pages.profile.profile_api import ProfileApi
from utils.read_data import read_json

profile_api = ProfileApi()

def test_register():
    payload = read_json('test_data/register_data.json')

    response = profile_api.register(payload)
    data = response.json()
    print(data)
    assert data["statusCode"] in [200, 201, 409]

def test_valid_login():
    data = read_json('test_data/login_data.json')
    payload = data["valid_user"]
    response = profile_api.login(payload)
    assert response.status_code == 200
    res_json = response.json()
    shopper_id = res_json["data"]["userId"]
    print("SHOPPER ID:", shopper_id)

def test_invalid_login():
    data = read_json("test_data/login_data.json")

    payload = data["invalid_user"]

    response = profile_api.login(payload)

    assert response.status_code in [400, 401]

