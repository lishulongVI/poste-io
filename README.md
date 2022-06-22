### Poste-sdk

> poste操作助手

### 部署Poste

### docker-compose

```
version: '3'

services:
  mailserver:
    image: analogic/poste.io
    container_name: mailserver
    restart: unless-stopped
    ports:
      - "25:25"
      - "80:80"
      - "443:443"
      - "4190:4190"
      - "110:110"
      - "143:143"
      - "465:465"
      - "587:587"
      - "993:993"
      - "995:995"
    privileged: true
    environment:
      - HTTPS=ON
      - TZ=America/Mexico_City
    volumes:
      - ./mailserver_data:/data
```

### DNS配置

https://poste.io/doc/configuring-dns



#### Admin操作

```python
from typing import List

from poste_sdk.client import PosteClient
from poste_sdk.models import Domains
from poste_sdk.models import Box

with PosteClient(address='管理账户', password='密码', domain='域名') as client:
    # 获取可用域名
    domains = client.get_domains()
    assert isinstance(domains, List)
    assert isinstance(domains[0], Domains)
    # 获取邮箱列表
    boxes = client.get_boxes()
    assert isinstance(boxes, List)
    assert isinstance(boxes[0], Box)

```



#### 邮箱操作

```python
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

```

