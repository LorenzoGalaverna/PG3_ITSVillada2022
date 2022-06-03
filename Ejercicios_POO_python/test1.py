from Ejercicio1 import *

def test_string_equal():
    assert Persona.inicializar(persona1, "Juan") == "Juan"
    assert Persona.inicializar(persona2, "Pedro") == "Pedro"