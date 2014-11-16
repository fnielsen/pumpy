"""Matrix."""

import logging
from logging import NullHandler

log = logging.getLogger(__name__)

# Avoid "No handlers" message if no logger
log.addHandler(NullHandler())


class Matrix(object):

    """Numerical matrix."""

    def __init__(self, obj):
        """Initialize matrix object."""
        log.debug("Constructing matrix object")
        self._matrix = obj

    def __getitem__(self, indices):
        """Get element in matrix.

        Examples
        --------
        >>> m = Matrix([[1, 2], [3, 4]])
        >>> m[0, 1]
        2

        """
        return self._matrix[indices[0]][indices[1]]

    def __setitem__(self, indices, value):
        """Set element in matrix.

        Examples
        --------
        >>> m = Matrix([[1, 2], [3, 4]])
        >>> m[0, 1]
        2
        >>> m[0, 1] = 5
        >>> m[0, 1]
        5

        """
        self._matrix[indices[0]][indices[1]] = value

    @property
    def shape(self):
        """Return shape of matrix.

        Examples
        --------
        >>> m = Matrix([[1, 2], [3, 4], [5, 6]])
        >>> m.shape
        (3, 2)

        """
        rows = len(self._matrix)
        if rows == 0:
            rows = 1
            columns = 0
        else:
            columns = len(self._matrix[0])
        return (rows, columns)

    def __abs__(self):
        """Return the absolute value.

        Examples
        --------
        >>> m = Matrix([[1, -1]])
        >>> m_abs = abs(m)
        >>> m_abs[0, 1]
        1

        """
        result = Matrix([[abs(element) for element in row]
                         for row in self._matrix])
        return result

    def __add__(self, other):
        """Add number to matrix.

        Parameters
        ----------
        other : integer or Matrix

        Returns
        -------
        m : Matrix
            Matrix of the same size as the original matrix

        Examples
        --------
        >>> m = Matrix([[1, 2], [3, 4]])
        >>> m = m + 1
        >>> m[0, 0]
        2

        >>> m = m + Matrix([[5, 6], [7, 8]])
        >>> m[0, 0]
        7

        """
        if isinstance(other, int) or isinstance(other, float):
            result = [[element + other for element in row]
                      for row in self._matrix]
        elif isinstance(other, Matrix):
            result = [[self[m, n] + other[m, n]
                       for n in range(self.shape[1])]
                      for m in range(self.shape[0])]
        else:
            raise TypeError
        return Matrix(result)

    def __mul__(self, other):
        """Multiply number to matrix.

        Parameters
        ----------
        other : integer, float

        Returns
        -------
        m : Matrix
            Matrix with multiplication result

        Examples
        --------
        >>> m = Matrix([[1, 2], [3, 4]])
        >>> m = m * 2
        >>> m[0, 0]
        2

        """
        if isinstance(other, int) or isinstance(other, float):
            result = [[element * other for element in row]
                      for row in self._matrix]
        else:
            raise TypeError
        return Matrix(result)

    def __pow__(self, other):
        """Compute power of element with `other` as the exponent.

        Parameters
        ----------
        other : integer, float

        Returns
        -------
        m : Matrix
            Matrix with multiplication result

        Examples
        --------
        >>> m = Matrix([[1, 2], [3, 4]])
        >>> m = m ** 3
        >>> m[0, 1]
        8

        """
        if isinstance(other, int) or isinstance(other, float):
            result = [[element ** other for element in row]
                      for row in self._matrix]
        else:
            raise TypeError
        return Matrix(result)

    def __str__(self):
        """Return string representation of matrix."""
        return str(self._matrix)

    def transpose(self):
        """Return transposed matrix.

        Examples
        --------
        >>> m = Matrix([[1, 2], [3, 4]])
        >>> m = m.transpose()
        >>> m[0, 1]
        3

        """
        log.debug("Transposing")
        # list necessary for Python 3 where zip is a generator
        return Matrix(list(zip(*self._matrix)))

    @property
    def T(self):
        """Transposed of matrix.

        Returns
        -------
        m : Matrix
            Copy of matrix

        Examples
        --------
        >>> m = Matrix([[1, 2], [3, 4]])
        >>> m = m.T
        >>> m[0, 1]
        3

        """
        log.debug("Calling transpose()")
        return self.transpose()
