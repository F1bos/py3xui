"""This module contains the PanelSettings class which represents panel settings in the XUI API."""

from pydantic import BaseModel, ConfigDict, Field


# pylint: disable=too-few-public-methods
class PanelSettingsFields:
    """Stores the fields returned by the XUI API for parsing."""

    WEB_LISTEN = "webListen"
    WEB_DOMAIN = "webDomain"
    WEB_PORT = "webPort"
    WEB_CERT_FILE = "webCertFile"
    WEB_KEY_FILE = "webKeyFile"
    WEB_BASE_PATH = "webBasePath"
    SESSION_MAX_AGE = "sessionMaxAge"
    PAGE_SIZE = "pageSize"
    EXPIRE_DIFF = "expireDiff"
    TRAFFIC_DIFF = "trafficDiff"
    REMARK_MODEL = "remarkModel"
    TG_BOT_ENABLE = "tgBotEnable"
    TG_BOT_TOKEN = "tgBotToken"
    TG_BOT_PROXY = "tgBotProxy"
    TG_BOT_API_SERVER = "tgBotAPIServer"
    TG_BOT_CHAT_ID = "tgBotChatId"
    TG_RUN_TIME = "tgRunTime"
    TG_BOT_BACKUP = "tgBotBackup"
    TG_BOT_LOGIN_NOTIFY = "tgBotLoginNotify"
    TG_CPU = "tgCpu"
    TG_LANG = "tgLang"
    TIME_LOCATION = "timeLocation"
    SECRET_ENABLE = "secretEnable"
    SUB_ENABLE = "subEnable"
    SUB_LISTEN = "subListen"
    SUB_PORT = "subPort"
    SUB_PATH = "subPath"
    SUB_DOMAIN = "subDomain"
    SUB_CERT_FILE = "subCertFile"
    SUB_KEY_FILE = "subKeyFile"
    SUB_UPDATES = "subUpdates"
    SUB_ENCRYPT = "subEncrypt"
    SUB_SHOW_INFO = "subShowInfo"
    SUB_URI = "subURI"
    SUB_JSON_PATH = "subJsonPath"
    SUB_JSON_URI = "subJsonURI"
    SUB_JSON_FRAGMENT = "subJsonFragment"
    SUB_JSON_NOISES = "subJsonNoises"
    SUB_JSON_MUX = "subJsonMux"
    SUB_JSON_RULES = "subJsonRules"
    DATEPICKER = "datepicker"


class PanelSettings(BaseModel):
    """Represents panel settings in the XUI API.

    Attributes:
        web_listen (str): Web server listen address
        web_domain (str): Web domain
        web_port (int): Web server port
        web_cert_file (str): Path to SSL certificate file
        web_key_file (str): Path to SSL key file
        web_base_path (str): Base path for web interface
        session_max_age (int): Session maximum age in minutes
        page_size (int): Number of items per page
        expire_diff (int): Expiration difference
        traffic_diff (int): Traffic difference
        remark_model (str): Remark model format
        tg_bot_enable (bool): Enable Telegram bot
        tg_bot_token (str): Telegram bot token
        tg_bot_proxy (str): Telegram bot proxy
        tg_bot_api_server (str): Telegram bot API server
        tg_bot_chat_id (str): Telegram chat ID
        tg_run_time (str): Telegram bot run schedule
        tg_bot_backup (bool): Enable Telegram bot backup
        tg_bot_login_notify (bool): Enable login notifications
        tg_cpu (int): CPU threshold for notifications
        tg_lang (str): Telegram bot language
        time_location (str): Time zone location
        secret_enable (bool): Enable secret
        sub_enable (bool): Enable subscription
        sub_listen (str): Subscription listen address
        sub_port (int): Subscription port
        sub_path (str): Subscription path
        sub_domain (str): Subscription domain
        sub_cert_file (str): Subscription SSL certificate file
        sub_key_file (str): Subscription SSL key file
        sub_updates (int): Subscription update interval
        sub_encrypt (bool): Enable subscription encryption
        sub_show_info (bool): Show subscription info
        sub_uri (str): Subscription URI
        sub_json_path (str): JSON subscription path
        sub_json_uri (str): JSON subscription URI
        sub_json_fragment (str): JSON subscription fragment
        sub_json_noises (str): JSON subscription noises
        sub_json_mux (str): JSON subscription mux
        sub_json_rules (str): JSON subscription rules
        datepicker (str): Date picker format
    """

    web_listen: str = Field(default="", alias=PanelSettingsFields.WEB_LISTEN)  # type: ignore pylint: disable=line-too-long
    web_domain: str = Field(default="", alias=PanelSettingsFields.WEB_DOMAIN)  # type: ignore pylint: disable=line-too-long
    web_port: int = Field(default=0, alias=PanelSettingsFields.WEB_PORT)  # type: ignore pylint: disable=line-too-long
    web_cert_file: str = Field(default="", alias=PanelSettingsFields.WEB_CERT_FILE)  # type: ignore pylint: disable=line-too-long
    web_key_file: str = Field(default="", alias=PanelSettingsFields.WEB_KEY_FILE)  # type: ignore pylint: disable=line-too-long
    web_base_path: str = Field(default="", alias=PanelSettingsFields.WEB_BASE_PATH)  # type: ignore pylint: disable=line-too-long
    session_max_age: int = Field(default=60, alias=PanelSettingsFields.SESSION_MAX_AGE)  # type: ignore pylint: disable=line-too-long
    page_size: int = Field(default=50, alias=PanelSettingsFields.PAGE_SIZE)  # type: ignore pylint: disable=line-too-long
    expire_diff: int = Field(default=0, alias=PanelSettingsFields.EXPIRE_DIFF)  # type: ignore pylint: disable=line-too-long
    traffic_diff: int = Field(default=0, alias=PanelSettingsFields.TRAFFIC_DIFF)  # type: ignore pylint: disable=line-too-long
    remark_model: str = Field(default="-ieo", alias=PanelSettingsFields.REMARK_MODEL)  # type: ignore pylint: disable=line-too-long
    tg_bot_enable: bool = Field(default=False, alias=PanelSettingsFields.TG_BOT_ENABLE)  # type: ignore pylint: disable=line-too-long
    tg_bot_token: str = Field(default="", alias=PanelSettingsFields.TG_BOT_TOKEN)  # type: ignore pylint: disable=line-too-long
    tg_bot_proxy: str = Field(default="", alias=PanelSettingsFields.TG_BOT_PROXY)  # type: ignore pylint: disable=line-too-long
    tg_bot_api_server: str = Field(default="", alias=PanelSettingsFields.TG_BOT_API_SERVER)  # type: ignore pylint: disable=line-too-long
    tg_bot_chat_id: str = Field(default="", alias=PanelSettingsFields.TG_BOT_CHAT_ID)  # type: ignore pylint: disable=line-too-long
    tg_run_time: str = Field(default="@daily", alias=PanelSettingsFields.TG_RUN_TIME)  # type: ignore pylint: disable=line-too-long
    tg_bot_backup: bool = Field(default=False, alias=PanelSettingsFields.TG_BOT_BACKUP)  # type: ignore pylint: disable=line-too-long
    tg_bot_login_notify: bool = Field(default=True, alias=PanelSettingsFields.TG_BOT_LOGIN_NOTIFY)  # type: ignore pylint: disable=line-too-long
    tg_cpu: int = Field(default=80, alias=PanelSettingsFields.TG_CPU)  # type: ignore pylint: disable=line-too-long
    tg_lang: str = Field(default="en-US", alias=PanelSettingsFields.TG_LANG)  # type: ignore pylint: disable=line-too-long
    time_location: str = Field(default="Asia/Tehran", alias=PanelSettingsFields.TIME_LOCATION)  # type: ignore pylint: disable=line-too-long
    secret_enable: bool = Field(default=False, alias=PanelSettingsFields.SECRET_ENABLE)  # type: ignore pylint: disable=line-too-long
    sub_enable: bool = Field(default=False, alias=PanelSettingsFields.SUB_ENABLE)  # type: ignore pylint: disable=line-too-long
    sub_listen: str = Field(default="", alias=PanelSettingsFields.SUB_LISTEN)  # type: ignore pylint: disable=line-too-long
    sub_port: int = Field(default=2096, alias=PanelSettingsFields.SUB_PORT)  # type: ignore pylint: disable=line-too-long
    sub_path: str = Field(default="/sub/", alias=PanelSettingsFields.SUB_PATH)  # type: ignore pylint: disable=line-too-long
    sub_domain: str = Field(default="", alias=PanelSettingsFields.SUB_DOMAIN)  # type: ignore pylint: disable=line-too-long
    sub_cert_file: str = Field(default="", alias=PanelSettingsFields.SUB_CERT_FILE)  # type: ignore pylint: disable=line-too-long
    sub_key_file: str = Field(default="", alias=PanelSettingsFields.SUB_KEY_FILE)  # type: ignore pylint: disable=line-too-long
    sub_updates: int = Field(default=12, alias=PanelSettingsFields.SUB_UPDATES)  # type: ignore pylint: disable=line-too-long
    sub_encrypt: bool = Field(default=True, alias=PanelSettingsFields.SUB_ENCRYPT)  # type: ignore pylint: disable=line-too-long
    sub_show_info: bool = Field(default=True, alias=PanelSettingsFields.SUB_SHOW_INFO)  # type: ignore pylint: disable=line-too-long
    sub_uri: str = Field(default="", alias=PanelSettingsFields.SUB_URI)  # type: ignore pylint: disable=line-too-long
    sub_json_path: str = Field(default="/json/", alias=PanelSettingsFields.SUB_JSON_PATH)  # type: ignore pylint: disable=line-too-long
    sub_json_uri: str = Field(default="", alias=PanelSettingsFields.SUB_JSON_URI)  # type: ignore pylint: disable=line-too-long
    sub_json_fragment: str = Field(default="", alias=PanelSettingsFields.SUB_JSON_FRAGMENT)  # type: ignore pylint: disable=line-too-long
    sub_json_noises: str = Field(default="", alias=PanelSettingsFields.SUB_JSON_NOISES)  # type: ignore pylint: disable=line-too-long
    sub_json_mux: str = Field(default="", alias=PanelSettingsFields.SUB_JSON_MUX)  # type: ignore pylint: disable=line-too-long
    sub_json_rules: str = Field(default="", alias=PanelSettingsFields.SUB_JSON_RULES)  # type: ignore pylint: disable=line-too-long
    datepicker: str = Field(default="gregorian", alias=PanelSettingsFields.DATEPICKER)  # type: ignore pylint: disable=line-too-long

    model_config = ConfigDict(
        populate_by_name=True,
    )
