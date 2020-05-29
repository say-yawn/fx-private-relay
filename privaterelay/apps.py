import requests

from django.apps import AppConfig
from django.conf import settings


class PrivateRelayConfig(AppConfig):
    name = 'privaterelay'

    def __init__(self, app_name, app_module):
        super(PrivateRelayConfig, self).__init__(app_name, app_module)
        self.fxa_verifying_keys = []

    def ready(self):
        resp = requests.get(
            '%s/jwks' %
            settings.SOCIALACCOUNT_PROVIDERS['fxa']['OAUTH_ENDPOINT']
        )
        # import ipdb; ipdb.set_trace()
        # resp_json = resp.json()
        # self.fxa_verifying_keys = resp_json['keys']

        from allauth.socialaccount.signals import pre_social_login
        from .signals import invitations_only

        pre_social_login.connect(invitations_only)
