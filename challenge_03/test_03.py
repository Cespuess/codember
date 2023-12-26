from ej_03 import open_file, get_min, get_max, count_char

def test_open_file():
    assert open_file("./challenge_03/prueba.txt") == [["4-2r", "holamundo."], ["2-3r", "adiosmundo"]]

def test_get_min():
    assert get_min('10-10b') == 10
    assert get_min('7-9x') == 7

def test_get_max():
    assert get_max("10-13") == 13
    assert get_max("7-9") == 9

def test_count_char():
    assert count_char("hihje", "h") == 2
    assert count_char("jjkllepdddlll", "l") == 5