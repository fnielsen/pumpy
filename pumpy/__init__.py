# -*- coding: utf-8 -*-
"""pumpy - pure python numerics."""

__title__ = "pumpy"
__version__ = 0.1
__author__ = "Finn Aarup Nielsen"
__license__ = "GPLv3"
__copyright__ = "DTU"

from . import matrix
from .matrix import Matrix

__all__ = ('matrix', 'Matrix',)
