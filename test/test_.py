import pytest
from pyclassify.utils import distance, majority_vote


def test_distance():
    point1 = [0, 1, 2]
    point2 = [5, 6, 7]

    assert distance(point1, point2) == distance(point2, point1)  # symmetry
    with pytest.raises(AssertionError):
        assert distance(point1, point2) != distance(point2, point1)  # symmetry breaking

    assert distance(point1, point2) >= 0  # test positivity
    with pytest.raises(AssertionError):
        assert -distance(point1, point2) >= 0  # test positivity

    assert distance(point1, point1) == 0
    with pytest.raises(AssertionError):  # tests identity breaking
        assert distance(point1, point1) != 0

    point3 = [1, 9, 8]
    assert distance(point1, point2) + distance(point2, point3) >= distance(
        point1, point3
    )
    with pytest.raises(AssertionError):  # tests identity triangle inequality
        assert distance(point1, point2) + distance(point2, point3) < distance(
            point1, point3
        )


def test_majority_vote():
    neighb = [0, 1, 1, 1, 1, 0]
    print(type(neighb))
    assert majority_vote(neighb) == 1
    fake_neigh = "aaa"
    with pytest.raises(TypeError):
        majority_vote(fake_neigh)
