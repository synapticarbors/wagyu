from hypothesis import strategies
from hypothesis_geometry import planar

from tests.binding_tests.utils import (bound_edges_sides,
                                       bound_polygon_kinds)
from tests.integration_tests.utils import (
    to_bound_with_ported_bounds_pair,
    to_bound_with_ported_edges_lists,
    to_bound_with_ported_intersect_nodes_pair,
    to_bound_with_ported_linear_rings_pair,
    to_bound_with_ported_points_lists_pair,
    to_bound_with_ported_points_pair,
    to_bound_with_ported_rings_pair)
from tests.port_tests.utils import (ported_edges_sides,
                                    ported_polygon_kinds)
from tests.strategies import (coordinates,
                              floats,
                              integers_32,
                              sizes,
                              trits)
from tests.utils import (to_maybe_pairs,
                         transpose_pairs)

booleans = strategies.booleans()
sizes = sizes
coordinates_lists = strategies.lists(coordinates)
points_pairs = strategies.builds(to_bound_with_ported_points_pair, coordinates,
                                 coordinates)
points_lists_pairs = strategies.lists(points_pairs).map(transpose_pairs)
maybe_rings_pairs = to_maybe_pairs(strategies.deferred(lambda: rings_pairs))
maybe_rings_lists_pairs = (strategies.lists(maybe_rings_pairs)
                           .map(transpose_pairs))
rings_pairs = strategies.builds(to_bound_with_ported_rings_pair,
                                sizes, maybe_rings_lists_pairs,
                                points_lists_pairs, booleans)
linear_rings_points_pairs = (
    planar.contours(coordinates).map(
            to_bound_with_ported_points_lists_pair))
linear_rings_pairs = (linear_rings_points_pairs
                      .map(to_bound_with_ported_linear_rings_pair))
edges_lists_pairs = linear_rings_pairs.map(to_bound_with_ported_edges_lists)
polygon_kinds_pairs = strategies.sampled_from(
        list(zip(bound_polygon_kinds, ported_polygon_kinds)))
edges_sides_pairs = strategies.sampled_from(list(zip(bound_edges_sides,
                                                     ported_edges_sides)))
bounds_pairs = strategies.builds(to_bound_with_ported_bounds_pair,
                                 edges_lists_pairs, sizes, sizes, points_pairs,
                                 maybe_rings_pairs, floats, sizes, integers_32,
                                 integers_32, trits, polygon_kinds_pairs,
                                 edges_sides_pairs)
intersect_nodes_pairs = strategies.builds(
        to_bound_with_ported_intersect_nodes_pair, bounds_pairs, bounds_pairs,
        points_pairs)
