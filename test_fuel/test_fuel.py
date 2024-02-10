# import libraries
from fuel import convert, gauge
import pytest

def test_valid_C():
    assert convert("3/4") == 75

def test_zero_c():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_str_c():
    with pytest.raises(ValueError):
        convert("d/e")

def test_x_bigger_c():
    with pytest.raises(ValueError):
        convert("5/4")

def test_e_g():
    assert gauge(1) == "E"

def test_per_g():
    assert gauge(87) == "87%"

def test_f_g():
    assert gauge(99) == "F"
