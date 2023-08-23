import time

import requests
from  services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

login = "psh2222"
email = "psh118@kk.aa"
password = "pshpshpsh5"
def test_put_v1_account_token():
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

    api.account.put_v1_account_token(token = "123")
    #token = "d652c8e4-6b29-4487-b697-3ca5ce6710ad"





