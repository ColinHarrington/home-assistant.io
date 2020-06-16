"""Support for Plum Lightpad devices."""
import asyncio
import logging

import voluptuous as vol

from homeassistant.components.plum_lightpad.const import DOMAIN, PLUM_DATA
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME, EVENT_HOMEASSISTANT_STOP
from homeassistant.helpers import discovery
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)


CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_USERNAME): cv.string,
                vol.Required(CONF_PASSWORD): cv.string,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)


async def async_setup(hass, config):
    """Plum Lightpad Platform initialization."""

    plum = hass.data[PLUM_DATA]

    def cleanup(event):
        """Clean up resources."""
        plum.cleanup()

    hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STOP, cleanup)

    async def new_load(device):
        """Load light and sensor platforms when LogicalLoad is detected."""
        await asyncio.wait(
            [
                hass.async_create_task(
                    discovery.async_load_platform(
                        hass, "light", DOMAIN, discovered=device, hass_config=config
                    )
                )
            ]
        )

    async def new_lightpad(device):
        """Load light and binary sensor platforms when Lightpad detected."""
        await asyncio.wait(
            [
                hass.async_create_task(
                    discovery.async_load_platform(
                        hass, "light", DOMAIN, discovered=device, hass_config=config
                    )
                )
            ]
        )

    device_web_session = async_get_clientsession(hass, verify_ssl=False)
    hass.async_create_task(
        plum.discover(
            hass.loop,
            loadListener=new_load,
            lightpadListener=new_lightpad,
            websession=device_web_session,
        )
    )

    return True
