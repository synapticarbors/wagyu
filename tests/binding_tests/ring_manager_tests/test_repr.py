import sys

from _wagyu import RingManager
from hypothesis import given

from . import strategies


@given(strategies.ring_managers)
def test_basic(ring_manager: RingManager) -> None:
    result = repr(ring_manager)

    assert result.startswith(RingManager.__module__)
    assert RingManager.__qualname__ in result


@given(strategies.ring_managers)
def test_round_trip(ring_manager: RingManager) -> None:
    result = repr(ring_manager)

    assert eval(result, sys.modules) == ring_manager
