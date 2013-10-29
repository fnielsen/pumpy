
import logging
from logging import NullHandler

log = logging.getLogger(__name__)

# Avoid "No handlers" message if no logger
log.addHandler(NullHandler())

class Matrix():

    def __init__(self, object):
        log.info("Constructing matrix object")
        self._matrix = object

    @property
    def shape(self):
        rows = len(self._matrix)
        if rows == 0: 
            rows = 1
            columns = 0
        else:
            columns = len(self._matrix[0])
        return (rows, columns)

    def transpose(self):
        log.warning("Transposing")
        return zip(*self._matrix)

    @property
    def T(self):
        return self.transpose()
