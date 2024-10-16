"""
WARNING:
    Do not import from this file!
    Required for Django monoapp strategy.
    To import model class, use direct imports from the apps' models.
"""


from apps.chains import models as _chains_models
from apps.portfolio import models as _portfolio_models
from apps.users import models as _users_models
from apps.wallets import models as _wallets_models
