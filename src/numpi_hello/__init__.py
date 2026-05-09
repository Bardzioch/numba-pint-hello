"""Pakiet demonstracyjny łączący Numbę i Pint."""

from ._version import __version__
from .hello import hello_numba, hello_pint

__all__ = ["hello_numba", "hello_pint", "__version__"]