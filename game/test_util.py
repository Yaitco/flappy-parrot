import pytest
from game import util

@pytest.mark.parametrize("p1, p2, answer", [
    ((0, 0), (0, 0), 0),
    ((0, 0), (2000, 1000), 2236.06797749979),
    ((12345, 54321), (1234, 4321), 51219.667326135575),
])
def test_distance(p1, p2, answer):
    assert abs(util.distance(p1, p2) - answer) < 1e-6 

@pytest.mark.parametrize("rect1, rect2, answer", [
    (((0, 0), (2, 2)), ((1, 1), (3, 3)), True),
    (((0, 0), (2, 2)), ((-10, -10), (-1, -1)), False),
])
def test_is_rect_sect(rect1, rect2, answer):
    assert util.is_rect_sect(rect1, rect2) == answer
