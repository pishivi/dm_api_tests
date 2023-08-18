import requests
from  services.dm_api_account import DmApiAccount

def test_put_v1_account_token():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    token = "d652c8e4-6b29-4487-b697-3ca5ce6710ad"
    response = api.account.put_v1_account_token(token)
    print(response)




