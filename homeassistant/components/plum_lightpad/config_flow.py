"""Config flow for plum_lightpad integration."""
import logging

import aiohttp
from plumlightpad import Plum
import voluptuous as vol

from homeassistant import config_entries, exceptions
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME

from ...helpers.aiohttp_client import async_get_clientsession
from .const import DOMAIN, PLUM_DATA

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema({CONF_USERNAME: str, CONF_PASSWORD: str})


class PlumLightpadConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for plum_lightpad."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            try:
                await self.async_step_cloud_discovery(user_input)

            except InvalidAuth:
                errors["base"] = "invalid_auth"

            if "base" not in errors:
                await self.async_set_unique_id(user_input[CONF_USERNAME])
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=user_input[CONF_USERNAME], data=user_input
                )

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )

    async def async_step_cloud_discovery(self, user_input):
        """Validate the user input allows us to connect."""

        plum = Plum(user_input[CONF_USERNAME], user_input[CONF_PASSWORD])
        self.hass.data[PLUM_DATA] = plum

        try:
            websession = async_get_clientsession(self.hass, verify_ssl=True)
            await plum.loadCloudData(websession)

        # If we get a ContentTypeError its most likely due to issues logging
        # into the server so treat it as InvalidAuth
        except aiohttp.client_exceptions.ContentTypeError:
            raise InvalidAuth

        return plum


class InvalidAuth(exceptions.HomeAssistantError):
    """Error to indicate there is invalid auth."""
