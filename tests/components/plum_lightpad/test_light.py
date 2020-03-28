"""The tests for the Plum Lightpad light platform."""
from unittest.mock import MagicMock

from homeassistant.components.plum_lightpad.light import GlowRing


def mockGlowRing(intensity):
    """Build GlowRing mock with a given glow_intensity."""
    mock = MagicMock(glow_intensity=intensity)
    return GlowRing(mock)


def test_glowring_brightness():
    """Test the GlowRing's derived brightness property."""
    assert mockGlowRing(1.0).brightness == 255
    assert mockGlowRing(0.5).brightness == 128
    assert mockGlowRing(0.42).brightness == 107
    assert mockGlowRing(0.1).brightness == 26
    assert mockGlowRing(0.0).brightness == 0

    assert mockGlowRing(9.0).brightness == 255
    assert mockGlowRing(-0.9).brightness == 0
