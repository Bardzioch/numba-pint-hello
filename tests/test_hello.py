"""Testy funkcji demo z pakietu numpi_hello."""

from numpi_hello import hello_numba, hello_pint

def test_hello_numba_sum_of_squares():
    # dla n=10: 0^2+1^2+...+9^2 = 285.0
    result = hello_numba(10)
    assert result == 285.0

def test_hello_numba_zero():
    assert hello_numba(0) == 0.0

def test_hello_pint_conversion():
    out = hello_pint(100.0)
    assert "100.0 km/h" in out
    assert "27.78 m/s" in out  # dokładnie 27.777... -> format .2f daje 27.78

def test_hello_pint_different_speed():
    out = hello_pint(36.0)
    assert "36.0 km/h" in out
    assert "10.00 m/s" in out