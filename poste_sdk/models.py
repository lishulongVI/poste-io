from typing import List, Dict, Tuple

from pydantic.generics import GenericModel
from pydantic.fields import Field
from datetime import datetime


class Box(GenericModel):
    """
    邮箱账户
    """
    address: str = Field(
        ...,
        description='Complete mailbox email address'
    )
    user: str = Field(
        ...,
        description=r'User part of email address pattern: [a-zA-Z0-9\_\.\-]+'
    )
    home: str = Field(
        ...,
        description='Directory for emails, settings and other data'
    )
    name: str = Field(
        None,
        description='Account name'
    )
    disabled: bool = Field(
        None,
        description='Enable/disable mailbox functionality'
    )
    domain_admin: bool = Field(
        None,
        description='Is user administrator of his domain (PRO version only)'
    )
    super_admin: bool = Field(
        None,
        description='Is user system administrator'
    )
    strict_from_disabled: bool = Field(
        None,
        description='Disable strict From header check'
    )
    created: str = Field(
        None,
        description='Account creation date (exported in ISO 8601 format - 2004-02-12T15:19:21+0000)'
    )
    updated: str = Field(
        None,
        description='Account last update date (exported in ISO 8601 format - 2004-02-12T15:19:21+0000)'
    )
    redirect_only: bool = Field(
        None,
        description='Is this redirect only (empty data)'
    )
    redirect_to: List[str] = Field(
        [],
        description='If it is redirect, where it is directed[ If it is redirect, where it is directedstring]'
    )
    discard: bool = Field(
        None,
        description='Enable/disable mailbox functionality'
    )


class Boxes(GenericModel):
    page: int = Field(
        ...,
        description='第几页'
    )
    paging: int = Field(
        ...,
        description='每页多少条记录'
    )
    last_page: int = Field(
        ...,
        description='总页数'
    )
    results_count: int = Field(
        ...,
        description='总记录数'
    )

    results: List[Box] = Field(
        ...,
        description='box记录'
    )


class Domains(GenericModel):
    """
    可用域名
    """
    home: str = Field(
        None,
        description='Domain home directory'
    )
    name: str = Field(
        ...,
        description=r'Domain name pattern: [^\+\@ ]+'
    )
    created: str = Field(
        None,
        description='Creation datetime (exported in ISO 8601 format - 2004-02-12T15:19:21+0000)'
    )
    updated: str = Field(
        None,
        description='Last update datetime (exported in ISO 8601 format - 2004-02-12T15:19:21+0000)'
    )
    domain_bin: bool = Field(
        None,
        description='Toggle to domain bin func'
    )

    forward: bool = Field(
        None,
        description='Toggle to domain bin func'
    )
    force_route: bool = Field(
        None,
        description='Toggle to domain bin func'
    )


class Mail(GenericModel):
    """
    邮箱详情
    """
    id_: int = Field(..., alias='id')
    from_: str = Field(..., alias='from')
    date_: datetime = Field(..., alias='date')
    subject: str = Field(..., alias='subject')
    content_text: List[str] = Field(..., )
    content_html: List[str] = Field(..., )
    attachments: List[Tuple[str, bytes]] = Field([], description='附件')
