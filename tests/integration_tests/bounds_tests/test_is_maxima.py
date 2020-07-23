from hypothesis import given

from tests.utils import (BoundPortedBoundsPair,
                         equivalence)
from wagyu.hints import Coordinate
from . import strategies


@given(strategies.initialized_bounds_pairs, strategies.coordinates)
def test_basic(pair: BoundPortedBoundsPair, y: Coordinate) -> None:
    bound, ported = pair

    assert equivalence(bound.is_maxima(y), ported.is_maxima(y))
