from typing import Any

from py3xui.api.api_base import ApiFields, BaseApi
from py3xui.panel.panel_settings import PanelSettings


class SettingApi(BaseApi):
    def get_all(self) -> PanelSettings:
        endpoint = "panel/setting/all"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}
        self.logger.info("Getting all settings...")

        response = self._post(url, headers, data)
        self.logger.info("All settings retrieved successfully.")

        settings = response.json().get(ApiFields.OBJ)
        return PanelSettings.model_validate(settings)

    def update(self, settings: PanelSettings):
        endpoint = "panel/setting/update"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data = settings.model_dump(by_alias=True)

        self.logger.info("Updating settings...")

        self._post(url, headers, data)
        self.logger.info("Settings updated successfully.")

    def restart_panel(self):
        endpoint = "panel/setting/restartPanel"
        headers = {"Accept": "application/json"}

        url = self._url(endpoint)
        data: dict[str, Any] = {}

        self.logger.info("Restarting panel...")
        self._post(url, headers, data)
        self.logger.info("Panel restarted successfully.")
