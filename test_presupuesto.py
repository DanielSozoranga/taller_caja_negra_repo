import pytest
from presupuesto_analisis import calcular


def test_caso_feliz_datos_validos():
    intereses, total, cuota = calcular(presupuesto=1000, socios=2, meses=6)
    assert intereses == 720.00
    assert total == 1720.00
    assert cuota == 860.00


def test_cp01_socios_en_cero():
    with pytest.raises(ZeroDivisionError):
        calcular(presupuesto=1000, socios=0, meses=6)


def test_cp02_meses_negativos():
    _, _, cuota = calcular(presupuesto=1000, socios=2, meses=-3)
    assert cuota == 590.00


def test_cp03_socios_negativos():
    _, _, cuota = calcular(presupuesto=1000, socios=-2, meses=6)
    assert cuota == -860.00