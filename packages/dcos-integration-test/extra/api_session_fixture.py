"""This file has only one function: to provide a correctly configured
DcosApiSession object that will be injected into the pytest 'dcos_api_session' fixture
via the make_session_fixture() method
"""

from dcos_test_utils import dcos_api
from test_helpers import get_expanded_config


def make_session_fixture():
    args = dcos_api.DcosApiSession.get_args_from_env()

    exhibitor_admin_password = None
    expanded_config = get_expanded_config()
    if expanded_config['exhibitor_admin_password_enabled'] == 'true':
        exhibitor_admin_password = expanded_config['exhibitor_admin_password']

    dcos_api_session = dcos_api.DcosApiSession(
        exhibitor_admin_password=exhibitor_admin_password,
        **args)
    dcos_api_session.wait_for_dcos()
    return dcos_api_session
