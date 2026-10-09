import pytest
from Calculadora import sumar, restar, multiplicar, dividir


def test_sumar():
    assert sumar(5, 3) == 8
    assert sumar(-2, 2) == 0


def test_restar():
    assert restar(10, 4) == 6
    assert restar(5, 8) == -3


def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert multiplicar(-2, 3) == -6


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3


def test_dividir_entre_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)