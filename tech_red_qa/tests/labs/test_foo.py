from tech_red_qa.core.labs.my_code import foo
import logging

def test_foo():
    result = foo()
    print("Resultado de foo:", result)
    assert result == "¡Hola, mundo!", "la prueba no salió exitosa"
    logging.info("la prueba salió exitosa") 