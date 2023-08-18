import requests
from services.dm_api_account import DmApiAccount
def test_post_v1_account_login():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
    "login": "psh5",
    "password": "pshpshpsh5",
    "rememberMe": "True"
    }
    responce = api.login.post_v1_account_login(
        json = json
    )
    print(responce)