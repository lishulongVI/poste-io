from poste_sdk import __version__
from poste_sdk.client import PosteClient


def test_version():
    assert __version__ == '0.1.0'


def test_sdk():
    with PosteClient(address='admin@godox.ml', password='whvV92EcNo', domain='godox.ml') as client:
        domains = client.get_domains()
        assert len(domains) == 2
        # account = client.create_account(address='test1@godox.ml', passwd='test1')
        box_client = client.init_box_client(email_prefix='admin', password='whvV92EcNo')

        assert box_client

        mail = box_client.get_latest()

        assert mail
