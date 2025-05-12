from lib_core.labs.my_code import foo
import logging
import pytest

@pytest.mark.regression
class TestFoo:

    def test_foo(self):
        result = foo()
        print("Resultado de foo:", result)
        assert result == "¡Hola, mundo!", "la prueba no salió exitosa"
        logging.info("la prueba salió exitosa")