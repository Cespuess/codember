from ej_01 import count_words, open_file, print_result

def test_open_file():
    assert open_file("./challenge_01/text_test.txt") == ["murcielago", "leon", "jirafa", "cebra", "elefante"]

def test_count_words():
    assert count_words(["llaves", "casa", "casa", "casa", "llaves"]) == {"llaves":2, "casa":3}
    assert count_words(["taza", "ta", "za", "taza"]) == {"taza":2,"ta":1, "za":1}

def test_print_result():
    assert print_result({"llaves":2, "casa":3}) == "llaves2casa3"
    assert print_result({"taza":2,"ta":1, "za":1}) == "taza2ta1za1"