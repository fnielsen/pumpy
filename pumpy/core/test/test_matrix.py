

from ..multiarray import Matrix


def test_getitem():
    m = Matrix([[1, 2], [3, 4]])
    assert m[0, 1] == 2
    assert m[1, 1] == 4
