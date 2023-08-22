import requests
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog

structlog.configure(
    processors= [
        structlog.processors.JSONRenderer(indent = 4, sort_keys = True, ensure_ascii = False)
    ]
)
def test_put_v1_account_email():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": "psh99",
        "password": "pshpshpsh4",
        "email": "psh123@mail.ru"
    }
    response = api.account.put_v1_account_email(json=json)
    assert response.status_code == 200, f"Статус код ответа {response.status_code}, должен быть 200"
    print(response)

