## Poste-sdk

> poste操作助手

### Poste服务部署
1. 生成文档 `cd docs && make html`
2. [在线文档](https://poste-sdk.readthedocs.io)


### 安装
```
pip install poste-sdk
```

### 简要使用
```python
from poste_sdk.client import PosteClient
from poste_sdk.client import BoxClient
from poste_sdk.models import Mail

with PosteClient(address='管理账户', password='密码', domain='域名/ip', verify_ssl=False) as client:
    # 初始化

    box_client = client.init_box_client(email_prefix='test', password='test',domain=None) 
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
```
