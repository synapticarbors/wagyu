from hypothesis import given

from tests.binding_tests.utils import BoundRing
from tests.integration_tests.utils import (BoundPortedMaybeRingsListsPair,
                                           BoundPortedPointsListsPair,
                                           are_bound_ported_rings_equal)
from tests.port_tests.utils import PortedRing
from . import strategies


@given(strategies.sizes, strategies.maybe_rings_lists_pairs,
       strategies.points_lists_pairs, strategies.booleans)
def test_basic(index: int,
               children_pair: BoundPortedMaybeRingsListsPair,
               points_pair: BoundPortedPointsListsPair,
               corrected: bool) -> None:
    bound_children, ported_children = children_pair
    bound_points, ported_points = points_pair

    bound, ported = (BoundRing(index, bound_children, bound_points, corrected),
                     PortedRing(index, ported_children, ported_points,
                                corrected))

    assert are_bound_ported_rings_equal(bound, ported)
