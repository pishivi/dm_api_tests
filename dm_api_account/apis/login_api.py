import requests
from requests import Response
from requests import session
from restclient.restclient import Restclient

from ..models.login_credentials_model import login_credentials_model


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host,headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json : login_credentials_model, **kwargs ) -> Response:
        """
        Authenticate via credentials
        :param json:login_credentials_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/login",
            json=json,
            **kwargs
        )

        return response

    def del_v1_account_login(self, **kwargs) -> Response:
        """
      Logout as current user
        :return:
        """
        response = self.session.delete(
            url=f"{self.host}/v1/account/login",
            **kwargs
        )
        return response

    def del_v1_account_login_all(self, **kwargs) -> Response:
        """
      Logout from every device
        :return:
        """

        response = self.session.delete(
            url=f"{self.host}/v1/account/login/all",
            **kwargs
        )
        return response