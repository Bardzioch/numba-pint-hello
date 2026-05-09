"""Funkcje pokazujące użycie Numba i Pint."""

import numpy as np
from numba import njit
from pint import UnitRegistry

ureg = UnitRegistry()

@njit
def hello_numba(n: int = 10) -> float:
    """
    Oblicza sumę kwadratów liczb od 0 do n-1 za pomocą Numba–JIT.

    Args:
        n: Liczba elementów.

    Returns:
        Suma kwadratów.
    """
    arr = np.arange(n, dtype=np.float64)
    result = 0.0
    for i in range(arr.size):
        result += arr[i] * arr[i]
    return result

def hello_pint(speed_kmh: float = 100.0) -> str:
    """
    Konwertuje prędkość z km/h na m/s za pomocą Pint i zwraca opis.

    Args:
        speed_kmh: Prędkość w kilometrach na godzinę.

    Returns:
        String z przeliczoną wartością.
    """
    speed = speed_kmh * ureg.kilometer / ureg.hour
    converted = speed.to(ureg.meter / ureg.second)
    return f"{speed_kmh} km/h = {converted.magnitude:.2f} {converted.units:~}"