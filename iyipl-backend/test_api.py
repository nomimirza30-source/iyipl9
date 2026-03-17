from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

response = client.post(
    "/api/token",
    data={"username": "Partner 1", "password": "password"},
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)

print(response.status_code)
print(response.json())

if response.status_code == 200:
    token = response.json().get("access_token")
    headers = {"Authorization": f"Bearer {token}"}
    me_resp = client.get("/api/me", headers=headers)
    print(me_resp.status_code)
    print(me_resp.json())
