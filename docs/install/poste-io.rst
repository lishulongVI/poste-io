============
部署poste.io
============

官网安装方式
============

1. `How to install? <https://poste.io/open>`_
2. docker-compose

::

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

3.  `DNS 配置 <https://poste.io/doc/configuring-dns>`_


Ubuntu安装
============

安装docker&docker-compose
-------------------------
- apt update
- apt install docker.io
- apt install docker-compose

部署
--------
.. code-block:: shell

    docker-compose up -d

域名申请
============

1. `Freenom <https://my.freenom.com/>`_
2. 修改nameserver，托管到cloudflare


cloudflare操作
---------------------
.. note::
    A 和 CNAME 记录

    mail.your-domain.com A → 外网IP

    smtp.your-domain.com CNAME mail.your-domain.com

    pop.your-domain.com CNAME mail.your-domain.com

    imap.your-domain.com CNAME mail.your-domain.com

    MX for your domain

    your-domain.com MX mail.your-domain.com

    SPF record:your-domain.com. IN TXT "v=spf1 mx ~all"

    DMARC record:_dmarc.our-domain.com. IN TXT "v=DMARC1; p=none; rua=mailto:dmarc-reports@our-domain.com"

    DKIM record ： Virtual domains → your-domain.com→ regenerate key