============
部署poste.io
============

官网安装方式
============

1. `How to install? <https://poste.io/open>`_
2. RSPAMD: 快速、免费和开源的垃圾邮件过滤系统. `查看rspamd <https://rspamd.com/>`_
3. CLAMAV: 病毒扫描 `查看clamav <https://github.com/Cisco-Talos/clamav>`_
4. docker-compose， 不关闭垃圾过滤&病毒扫描，会耗费更多的内存，还会不定时的拉取更新病毒库

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
          - DISABLE_RSPAMD=TRUE
          - DISABLE_CLAMAV=TRUE
          - TZ=Asia/Shanghai
        volumes:
          - ./mailserver_data:/data

5.  `DNS 配置 <https://poste.io/doc/configuring-dns>`_
6. 机器配置1C2G 就可以启动，所有服务，要想稳定运行需要加内存。或者关闭病毒扫描CLAMAV内存大户
7. 可以把发信方加入白名单，提高优先级，达到快速接信的目的，有多快？快三倍的样子


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

    # 需要垃圾过滤，病毒扫描的可以打开 DISABLE_RSPAMD。DISABLE_CLAMAV
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