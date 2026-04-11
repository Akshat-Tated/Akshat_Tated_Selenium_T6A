import requests

API_KEY = 'api key here'

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

headers = {
    "x-goog-api-key": API_KEY,
    'Content-Type': 'application/json'
}



while True:
    p = input('enter prompt: ')
    if p == 'fahh':
        break
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": p}
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)

    print("Status: ", response.status_code)
    data = response.json()
    print(data)
    if "candidates" in data:
        print(data["candidates"][0]["content"]["parts"][0]["text"])
    else:
        print("Error", data)


