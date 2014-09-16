

from ..matrix import Matrix


def test_getitem():
    m = Matrix([[1, 2], [3, 4]])
    assert m[0, 1] == 2
    assert m[1, 1] == 4


def test_transpose():
    m = Matrix([[1, 2], [3, 4]])
    mt = m.transpose()
    assert m[0, 1] == mt[1, 0]


def test_T():
    m = Matrix([[1, 2], [3, 4]])
    mt = m.T
    assert m[0, 1] == mt[1, 0]
