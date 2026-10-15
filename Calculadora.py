
import math


def raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número.

    Args:
        numero (int o float): Número que se desea calcular.

    Returns:
        float: Resultado de la raíz cuadrada.

    Raises:
        TypeError: Si la entrada no es numérica.
        ValueError: Si el número es negativo o no es finito.
    """
    if isinstance(numero, bool) or not isinstance(numero, (int, float)):
        raise TypeError("Debes ingresar un número válido")

    if not math.isfinite(numero):
        raise ValueError("El número debe ser finito")

    if numero < 0:
        raise ValueError("No se puede calcular la raíz de un número negativo")

    return math.sqrt(numero)
