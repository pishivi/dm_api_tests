import time

import requests
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog

structlog.configure(
    processors= [
        structlog.processors.JSONRenderer(indent = 4, sort_keys = True, ensure_ascii = False)
    ]
)
login = "psh121"
email = "psh121@kk.aa"
password = "pshpshpsh5"
def test_post_v1_account():
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": login,
        "email": email,
        "password": password
    }
    response = api.account.post_v1_account(json = json)
    assert response.status_code == 201, f"Статус код ответа {response.status_code}, должен быть 201"
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
