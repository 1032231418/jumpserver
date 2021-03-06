# ~*~ coding: utf-8 ~*~
#
from collections import defaultdict
from common.utils import get_object_or_none
from .models import Asset, SystemUser


def get_assets_by_id_list(id_list):
    return Asset.objects.filter(id__in=id_list)


def get_assets_by_hostname_list(hostname_list):
    return Asset.objects.filter(hostname__in=hostname_list)


def get_system_user_by_name(name):
    system_user = get_object_or_none(SystemUser, name=name)
    return system_user


def check_assets_have_system_user(assets, system_users):
    errors = defaultdict(list)

    for system_user in system_users:
        clusters = system_user.cluster.all()
        for asset in assets:
            if asset.cluster not in clusters:
                errors[asset].append(system_user)
    return errors
