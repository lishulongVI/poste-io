from poste_sdk import __version__
from poste_sdk.client import PosteClient


def test_version():
    assert __version__ == '0.1.8'


def test_sdk():
    with PosteClient(address='admin@xgmail.tk', password='WgnLAJKwrh', domain='140.143.231.237',
                     verify_ssl=False) as client:
        box_client = client.init_box_client(email_prefix='test', password='test')
        assert box_client
        mail = box_client.get_latest()
        assert mail


if __name__ == '__main__':
    test_sdk()
