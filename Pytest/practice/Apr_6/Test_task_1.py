# import requests
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#
# base_url = "https://www.shoppersstack.com"
#
# payload = {
#     "city": "jaora",
#     "country": "india",
#     "email": "akshat18@gmail.com",
#     "firstName": "Akshat",
#     "gender": "MALE",
#     "lastName": "Tated",
#     "password": "Akshat@34",
#     "phone": 7441176670,
#     "state": "MP",
#     "zoneId": "ALPHA"
# }
#
# jwtToken = 0
# def reg_post():
#     response = requests.post(f"{base_url}/shopping/shoppers", json=payload, verify=False)
#     return response.json()
#
# reg_post()
#
# logindata={
#   "email": "akshat18@gmail.com",
#   "password": "Akshat@34",
#   "role": "SHOPPER"
# }
# def login_post():
#     response = requests.post(f'{base_url}/shopping/users/login', json=logindata, verify=False)
#     global jwtToken, id
#     jwtToken = response.json()['data']['jwtToken']
#     id = response.json()['data']['userId']
#     return response.json()
#
# def getUserData():
#     header = { "Authorization": f"Bearer {jwtToken}"}
#     userData = requests.get(f"{base_url}/shopping/shoppers/{id}",  headers=header, verify=False)
#     print(userData.status_code)
#
#     return userData.json()
#
# print(reg_post())
# print(login_post())
# print(getUserData())

# id = res.data['userId']
# data =


# using session
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://www.shoppersstack.com"
session = requests.Session()

payload = {
    "city": "jaora",
    "country": "india",
    "email": "akshat18@gmail.com",
    "firstName": "Akshat",
    "gender": "MALE",
    "lastName": "Tated",
    "password": "Akshat@34",
    "phone": 7441176670,
    "state": "MP",
    "zoneId": "ALPHA"
}

jwtToken = 0
def reg_post():
    response = session.post(f"{base_url}/shopping/shoppers", json=payload, verify=False)
    return response.json()

reg_post()

logindata={
  "email": "akshat18@gmail.com",
  "password": "Akshat@34",
  "role": "SHOPPER"
}
def login_post():
    response = session.post(f'{base_url}/shopping/users/login', json=logindata, verify=False)
    global jwtToken, id
    jwtToken = response.json()['data']['jwtToken']
    id = response.json()['data']['userId']
    return response.json()

def getUserData():
    session.headers.update({
        'Authorization': f'Bearer {jwtToken}'
    })
    userData = session.get(f"{base_url}/shopping/shoppers/{id}", verify=False)
    print(userData.status_code)

    return userData.json()

print(reg_post())
print(login_post())
print(getUserData())