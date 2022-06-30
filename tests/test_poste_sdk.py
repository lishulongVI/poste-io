from poste_sdk import __version__
from poste_sdk.client import PosteClient
from poste_sdk.models import Box, Mail


def test_version():
    assert __version__ == '0.1.9'


def test_sdk():
    with PosteClient(address='admin@xgmail.tk', password='WgnLAJKwrh', domain='140.143.231.237',
                     verify_ssl=False) as client:
        box_client = client.init_box_client(email_prefix='test', password='test')
        print(box_client, box_client.address)
        assert box_client.address == 'test@xgmail.tk'

        print(box_client.server.stat())
        mail = box_client.get_latest()
        print(mail)


def test_sdk_list_boxes():
    print('\n')
    with PosteClient(address='admin@xgmail.tk', password='WgnLAJKwrh', domain='140.143.231.237',
                     verify_ssl=False) as client:
        v = client.get_boxes()
        print(v)

        assert v.results_count > 0
        print(v.results_count)


def test_sdk_delete_box():
    print('\n')
    with PosteClient(address='admin@xgmail.tk', password='WgnLAJKwrh', domain='140.143.231.237',
                     verify_ssl=False) as client:
        is_delete, message = client.delete_box('test@xgmail.tk')
        assert isinstance(is_delete, bool)
        print(is_delete, message)
        is_delete, message = client.delete_box('test1@xgmail.tk')
        assert isinstance(is_delete, bool)
        print(is_delete, message)


def test_sdk_get_mails():
    print('\n')
    with PosteClient(address='admin@xgmail.tk', password='WgnLAJKwrh', domain='140.143.231.237',
                     verify_ssl=False) as client:
        box = client.init_box_client(email_prefix='admin', password='WgnLAJKwrh')
        print('总数')
        print(box.get_email_cnt())

        print('get_emails')
        for i in box.get_emails(2):
            print(i.subject)

        print('get_latest')

        print(box.get_latest())
        print('get_origin_mails')
        for i in box.get_origin_mails():
            if isinstance(i, Mail):
                print(i.id_, i.subject)

        # 删除
        box.delete_by_id(i.id_)
        print('总数')
        print(box.get_email_cnt())

        # 删除所有邮件
        box.drop_mails()


if __name__ == '__main__':
    test_sdk()
