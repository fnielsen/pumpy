

import logging
import pumpy

A = pumpy.Matrix([[1, 2], [3, 4]])
A.T

log = logging.getLogger()
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler()  
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s'))
log.addHandler(handler)

A = pumpy.Matrix([[1, 2], [3, 4]])
A.T
