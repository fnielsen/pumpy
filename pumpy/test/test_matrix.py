"""Testing functions for matrix module."""


from .. import Matrix


def test_abs():
    matrix = Matrix([[-2, 3]])
    abs_matrix = abs(matrix)
    assert abs_matrix[0, 0] == 2
    assert abs_matrix[0, 1] == 3


def test_getitem():
    """Test matrix getitem."""
    m = Matrix([[1, 2], [3, 4]])
    assert m[0, 1] == 2
    assert m[1, 1] == 4


def test_setitem():
    matrix = Matrix([[1, 2]])
    matrix[0, 1] = 3
    assert matrix[0, 1] == 3
    assert matrix[0, 0] == 1


def test_shape():
    matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    assert matrix.shape == (3, 2)


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
