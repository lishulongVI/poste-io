import random
from typing import List

import httpx
import zmail

from poste_sdk.models import Mail, Domains, Box


class BoxClient:
    """
    Box 操作邮箱
    提取邮件内容
    删除邮件
    """

    def __init__(self, address, password):
        self.server = zmail.server(address, password)
        self.address = address
        self.password = password
        self.id_ = None

    def get_email_cnt(self):
        """
        邮件数量
        :return:
        """
        count, _ = self.server.stat()
        return count

    def get_email(self, id_):
        """
        获取指定邮件
        :param id_:
        :return:
        """
        return Mail(**self.server.get_mail(which=id_))

    def get_latest(self):
        """
        获取最近一条记录
        :return:
        """
        count, size = self.server.stat()
        if count:
            v = Mail(**self.server.get_latest())
            self.id_ = v.id_
            return v
        return None

    def get_origin_mails(
            self,
            subject=None,
            start_time=None,
            end_time=None,
            sender=None,
            start_index: Optional[int] = None,
            end_index: Optional[int] = None
    ) -> list:
        """
        获取邮件列表
        """
        count, size = self.server.stat()
        if not count:
            return []
        else:
            start_index = 1 if start_index is None else start_index
            end_index = count if end_index is None else end_index
        z = self.server.get_mails(
            subject=subject,
            start_time=start_time,
            end_time=end_time,
            sender=sender,
            start_index=start_index,
            end_index=end_index,

        )
        return [Mail(**i) for i in z]

    def get_emails(self, cnt):
        """
        获取最近几条邮件
        :param cnt:
        :return:
        """
        count, size = self.server.stat()
        if not count:
            return []

        return self.get_origin_mails(
            start_index=count - cnt,
            end_index=cnt
        )

    def delete_by_id(self, id_):
        """
        删除指定邮件
        :param id_:
        :return:
        """
        self.server.delete(which=id_)

    def drop_mails(self):
        """
        删除所有邮件
        :return:
        """
        id_, size = self.server.stat()
        while id_:
            self.delete_by_id(id_=id_)
            id_, size = self.server.stat()


class PosteClient:
    """
    适配https://poste.io/
    """

    def __init__(self, address, password, domain):
        self.uri = f'https://{domain}/admin/api/v1/'
        self.client = httpx.Client(auth=(address, password))

    def __str__(self):
        return self.uri

    def get_domains(self, page=1, paging=50) -> List[Domains]:
        """
        List all Domains
        :return:
        """
        res = self.client.get(url=f'{self.uri}domains?page={page}&paging={paging}', timeout=(2, 2))
        if res.status_code != 200:
            raise Exception(f'get_domains res:{res.status_code},{res.text}')
        return [Domains(**i) for i in res.json()['results']]

    def get_boxes(self) -> List[Box]:
        """
        List all Boxes
        :return:
        """
        res = self.client.get(url=f'{self.uri}boxes', timeout=(2, 2))
        if res.status_code != 200:
            raise Exception(f'get_domains res:{res.status_code},{res.text}')
        return [Box(**i) for i in res.json()['results']]

    def init_box_client(self, email_prefix, password, domain=None) -> BoxClient:
        """
        初始化一个Box，不存在就创建
        :param email_prefix:
        :param password:
        :param domain:
        :return:
        """
        if domain is None:
            domain = random.choice(self.get_domains()).name

        email = f'{email_prefix}@{domain}'
        req = {
            "name": email_prefix,
            "email": email,
            "passwordPlaintext": password,
            "disabled": False,
            "superAdmin": False
        }
        res = self.client.post(url=f'{self.uri}boxes', json=req, timeout=(2, 2))
        if res.status_code == 201:
            pass
        elif res.status_code == 400 and 'This combination of username and domain is already in database' in res.text:
            pass
        else:
            raise Exception(f'create_account res:{res.status_code},{res.text}')
        return BoxClient(email, password)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
