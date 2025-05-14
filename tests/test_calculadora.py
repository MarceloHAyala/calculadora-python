import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from calculadora import calcular

@pytest.mark.parametrize("num1, num2, op, esperado", [
    (2, 3, '+', 5),
    (5, 3, '-', 2),
    (2, 3, '*', 6),
    (6, 2, '/', 3),
    (2, 3, '^', 8),
    (2.5, 3.5, '+', 6.0),
    (-2, -3, '+', -5),
    (-2, 3, '*', -6),
    (0, 3, '/', 0),
    (3, 0, '/', None),
    (2, 0, '^', 1),
    (0, 0, '^', 1),
    (2, 3, 'x', None),
    (3, 3, '', None),
    (2, 3, '-', -1),
    (10, 2, '/', 5),
    (9, 2, '^', 81),
    (5, -2, '^', 0.04),
    (-3, 2, '^', 9),
    (4, 0.5, '^', 2.0),
])
def test_calcular(num1, num2, op, esperado):
    assert calcular(num1, num2, op) == pytest.approx(esperado)
