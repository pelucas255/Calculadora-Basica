import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import pytest
from Calculadora import raiz_cuadrada


# ---------- Caso correcto ----------
def test_raiz_cuadrada_caso_correcto():
    """La raíz cuadrada de 9 debe ser 3."""
    assert raiz_cuadrada(9) == 3.0


def test_raiz_cuadrada_numero_decimal():
    """La raíz cuadrada de 2.25 debe ser 1.5."""
    assert raiz_cuadrada(2.25) == 1.5


# ---------- Caso límite ----------
def test_raiz_cuadrada_caso_limite_cero():
    """El caso límite: la raíz cuadrada de 0 es 0."""
    assert raiz_cuadrada(0) == 0.0


def test_raiz_cuadrada_numero_muy_grande():
    """Número muy grande: el resultado debe ser finito."""
    resultado = raiz_cuadrada(1e308)
    assert math.isfinite(resultado)
    assert resultado == pytest.approx(1e154, rel=1e-9)


# ---------- Caso error ----------
def test_raiz_cuadrada_numero_negativo_lanza_valueerror():
    """Un número negativo debe lanzar ValueError."""
    with pytest.raises(ValueError):
        raiz_cuadrada(-4)


def test_raiz_cuadrada_texto_lanza_typeerror():
    """Un texto debe lanzar TypeError."""
    with pytest.raises(TypeError):
        raiz_cuadrada("hola")


def test_raiz_cuadrada_booleano_lanza_typeerror():
    """Un booleano debe lanzar TypeError (no es un número válido)."""
    with pytest.raises(TypeError):
        raiz_cuadrada(True)


def test_raiz_cuadrada_infinito_lanza_valueerror():
    """Infinity debe lanzar ValueError (no es finito)."""
    with pytest.raises(ValueError):
        raiz_cuadrada(math.inf)
