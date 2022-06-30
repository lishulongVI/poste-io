=================
使用样例
=================

.. note::

    1. 支持 verify_ssl = False 国内无域名 开443端口情况

    2. 解析dns 要是在国内托管给cloudflare 会有不稳定的情况，可以修改本地host

    3. 主要用途：临时邮箱接受邮件



安装
------------
.. code-block:: python

    pip install poste-sdk -U



获取可用域名
------------

.. code-block:: python

    from typing import List

    from poste_sdk.client import PosteClient
    from poste_sdk.models import Domains
    from poste_sdk.models import Box

    with PosteClient(address='管理账户', password='密码', domain='域名/ip', verify_ssl = False) as client:
        # 获取可用域名
        domains = client.get_domains()
        assert isinstance(domains, List)
        assert isinstance(domains[0], Domains)



获取邮箱列表
------------
.. code-block:: python

    from typing import List

    from poste_sdk.client import PosteClient
    from poste_sdk.models import Domains
    from poste_sdk.models import Box

    with PosteClient(address='管理账户', password='密码', domain='域名') as client:
        # 获取邮箱列表
        # page=1,paging=14000 分页
        # boxes = client.get_boxes(page=1,paging=14000)
        boxes = client.get_boxes()
        assert isinstance(boxes, List)
        assert isinstance(boxes[0], Box)

删除邮箱列表
------------
.. code-block:: python

    from typing import List

    from poste_sdk.client import PosteClient
    from poste_sdk.models import Domains
    from poste_sdk.models import Box

    with PosteClient(address='管理账户', password='密码', domain='域名') as client:
        # 获取邮箱列表
        for i in tqdm(EMAIL_CLIENT.get_boxes(page=1,paging=14000)):
            # 跳过管理账户
            if 'admin' in i.address:
                continue
            # 删除邮件数量为0的邮箱
            v = BoxClient(address=i.address,password=i.user).get_email_cnt()
            if v == 0 and 'admin' not in i.address:
                EMAIL_CLIENT.delete_box(i.address)



邮箱操作
----------
.. code-block:: python

    from poste_sdk.client import PosteClient
    from poste_sdk.client import BoxClient
    from poste_sdk.models import Mail

    with PosteClient(address='管理账户', password='密码', domain='域名') as client:
        # 初始化
        box_client = client.init_box_client(email_prefix='test', password='test')
        assert isinstance(box_client, BoxClient)
        # 获取最近1条邮件
        mail = box_client.get_latest()
        assert isinstance(mail, Mail)

        # email 总数量
        box_client.get_email_cnt()

        # 获取指定邮件
        mail = box_client.get_email(id_=1)
        assert isinstance(mail, Mail)

        # 删除邮件
        box_client.delete_by_id(1)

        # 清空邮件
        box_client.drop_mails()

