from pydantic import ConfigDict, Field

from py3xui.inbound.bases import JsonStringModel


# pylint: disable=too-few-public-methods
class StreamSettingsFields:
    """Stores the fields returned by the XUI API for parsing."""

    SECURITY = "security"
    NETWORK = "network"
    TCP_SETTINGS = "tcpSettings"

    EXTERNAL_PROXY = "externalProxy"

    REALITY_SETTINGS = "realitySettings"
    XTLS_SETTINGS = "xtlsSettings"
    TLS_SETTINGS = "tlsSettings"


class StreamSettings(JsonStringModel):
    security: str
    network: str
    tcp_settings: dict = Field(alias=StreamSettingsFields.TCP_SETTINGS)  # type: ignore

    external_proxy: list = Field(
        default=[], alias=StreamSettingsFields.EXTERNAL_PROXY
    )  # type: ignore

    reality_settings: dict = Field(
        default={}, alias=StreamSettingsFields.REALITY_SETTINGS  # type: ignore
    )
    xtls_settings: dict = Field(
        default={}, alias=StreamSettingsFields.XTLS_SETTINGS  # type: ignore
    )
    tls_settings: dict = Field(default={}, alias=StreamSettingsFields.TLS_SETTINGS)  # type: ignore

    model_config = ConfigDict(
        populate_by_name=True,
    )