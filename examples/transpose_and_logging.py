"""Transpose and logging example."""

from logging import getLogger, StreamHandler, Formatter, DEBUG
import pumpy

A = pumpy.Matrix([[1, 2], [3, 4]])
A.T

log = getLogger()
log.setLevel(DEBUG)
handler = StreamHandler()
formatter = Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

A = pumpy.Matrix([[1, 2], [3, 4]])
A.T
