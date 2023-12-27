from ej_03 import open_file, get_min, get_max, count_char, verify_invalid_key, find_invalid_key

import pytest

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

def test_verify_invalid_key():
    assert verify_invalid_key(['4-8o', 'cjgmhv']) == True
    assert verify_invalid_key(['8-8p', 'swjluowwhypqo']) == True
    assert verify_invalid_key(["2-5d", "doudaje"]) == False
    assert verify_invalid_key(["10-34a", "aaaaaiodjfsaaaoeuraaaa"]) == False

def test_find_invalid_key():
    invalid_list = [['4-8o', 'cjgmhv'], ['8-8p', 'swjluowwhypqo'], ["1-3t", "hodsdk"]]
    assert find_invalid_key(invalid_list, 2) == 'swjluowwhypqo'
    assert find_invalid_key(invalid_list, 1) == 'cjgmhv'
    assert find_invalid_key(invalid_list, 3) == "hodsdk"
    result = find_invalid_key(invalid_list, 6)
    assert isinstance(result, IndexError)