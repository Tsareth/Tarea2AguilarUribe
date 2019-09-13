import Tarea2


def test_1():
    assert Tarea2.result(3, 2) == ("Suma:", 5, "Resta:", 1,
                                   "Multiplicacion:", 6)


def test_2():
    assert Tarea2.result(1, 2) == -3


def test_3():
    assert Tarea2.result("a", 3) == -1
