from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
