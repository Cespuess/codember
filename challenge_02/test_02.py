from ej_02 import decoder, open_file

def test_open_file():
    assert open_file("./challenge_02/text_test_02.txt") == "Probando texto"

def test_decoder_one():
    assert decoder("##*&") == "4"

def test_decoder_more():
    assert decoder("&##&*&@&") == "0243"