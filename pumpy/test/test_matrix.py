"""Testing functions for matrix module."""


from ..matrix import Matrix


def test_getitem():
    """Test matrix getitem."""
    m = Matrix([[1, 2], [3, 4]])
    assert m[0, 1] == 2
    assert m[1, 1] == 4


def test_transpose():
    """Test Matrix transpose method."""
    m = Matrix([[1, 2], [3, 4]])
    mt = m.transpose()
    assert mt[0, 0] == 1
    assert m[0, 1] == mt[1, 0]
    assert mt[1, 0] == 2


def test_T():
    """Test Matrix T propery."""
    m = Matrix([[1, 2], [3, 4]])
    mt = m.T
    assert m[0, 1] == mt[1, 0]
