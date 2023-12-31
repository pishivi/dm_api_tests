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

login = "psh4433"
email = "psh4433@mail.ru"
password = "pshpshpsh4"
def test_put_v1_account_email():
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": login,
        "email": email,
        "password": password
    }
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f"Статус код ответа {response.status_code}, должен быть 201"
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)

    json = {
        "login": login,
        "password": password,
        "rememberMe": "True"
    }
    #response = api.login.post_v1_account_login(json=json)
    assert response.status_code == 200, f"Статус код ответа {response.status_code}, должен быть 200"


    json = {
        "login": login,
        "password": password,
        "email": "psh4432@mail.ru"
    }
    response = api.account.put_v1_account_email(json=json)
    assert response.status_code == 200, f"Статус код ответа {response.status_code}, должен быть 200"
    print(response)

