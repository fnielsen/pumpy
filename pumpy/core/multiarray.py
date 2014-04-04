
import logging
from logging import NullHandler

log = logging.getLogger(__name__)

# Avoid "No handlers" message if no logger
log.addHandler(NullHandler())


class Matrix(object):
    """Numerical matrix."""

    def __init__(self, obj):
        log.debug("Constructing matrix object")
        self._matrix = obj

    def __getitem__(self, indices):
        """Get element in matrix.

        Example
        -------
        >>> m = Matrix([[1, 2], [3, 4]])
        >>> m[0, 1]
        2

        """
        return self._matrix[indices[0]][indices[1]]
            
    def __setitem__(self, indices, value):
        """Set element in matrix.

        Example
        -------
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
        """Return shape of matrix."""
        rows = len(self._matrix)
        if rows == 0: 
            rows = 1
            columns = 0
        else:
            columns = len(self._matrix[0])
        return (rows, columns)

    def transpose(self):
        """Return transposed matrix."""
        log.debug("Transposing")
        return Matrix(zip(*self._matrix))

    @property
    def T(self):
        """Transposed of matrix."""
        return self.transpose()
