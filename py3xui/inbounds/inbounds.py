from pydantic import BaseModel, Field

from py3xui.clients.client import Client
from py3xui.inbounds.settings import Settings
from py3xui.inbounds.sniffing import Sniffing
from py3xui.inbounds.stream_settings import StreamSettings


# pylint: disable=too-few-public-methods
class InboundFields:
    """Stores the fields returned by the XUI API for parsing."""

    ID = "id"
    UP = "up"
    DOWN = "down"
    TOTAL = "total"
    REMARK = "remark"
    ENABLE = "enable"
    EXPIRY_TIME = "expiryTime"
    CLIENT_STATS = "clientStats"
    LISTEN = "listen"
    PORT = "port"
    PROTOCOL = "protocol"
    SETTINGS = "settings"
    STREAM_SETTINGS = "streamSettings"
    TAG = "tag"
    SNIFFING = "sniffing"


class Inbound(BaseModel):
    id: int
    up: int
    down: int
    total: int
    remark: str
    enable: bool
    expiry_time: int = Field(alias=InboundFields.EXPIRY_TIME)  # type: ignore
    client_stats: list[Client] = Field(alias=InboundFields.CLIENT_STATS)  # type: ignore
    listen: str
    port: int
    protocol: str
    settings: Settings
    stream_settings: StreamSettings = Field(alias=InboundFields.STREAM_SETTINGS)  # type: ignore
    tag: str
    sniffing: Sniffing

    def __repr__(self) -> str:
        return (
            f"Inbound(id={self.id}, up={self.up}, down={self.down}, total={self.total}, "
            f"remark={self.remark}, enable={self.enable}, expiryTime={self.expiry_time}, "
            f"clientStats={self.client_stats}, listen={self.listen}, port={self.port}, "
            f"protocol={self.protocol}, settings={self.settings}, "
            f"streamSettings={self.stream_settings}, tag={self.tag}, sniffing={self.sniffing})"
        )
