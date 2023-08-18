import requests
from services.dm_api_account import DmApiAccount

def test_put_v1_account_email():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": "psh1",
        "password": "pshpshpsh1",
        "email": "psh2@mail.ru"
    }
    response = api.account.put_v1_account_email(
        json = json
    )
    print(response)

