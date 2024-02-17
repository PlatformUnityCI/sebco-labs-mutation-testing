import sys
import os

# Agregar la raíz del proyecto al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from  src.labs.my_code import foo

def test_foo():
    result = foo()
    assert result == "¡Hola, mundo!"