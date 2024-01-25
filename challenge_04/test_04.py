from ej_04 import open_file, separated_string, count_char, main

def test_open_file():
  assert open_file("./challenge_04/prueba.txt") == ["3n3E65A-nE65A", "U6Z1WWc0LP-U6Z1c0LP", "la6bqS-la6bqS", "la6bbqS-la6bqS", "rea-era"]

def test_separated_string():
  assert separated_string("3n3E65A-nE65A") == ["3n3E65A","nE65A"]

def test_count_char():
  assert count_char("3n3E65A") == "nE65A"
  assert count_char("U6Z1WWc0LP") == "U6Z1c0LP"

def test_main():
  assert main("./challenge_04/prueba.txt") == ["3n3E65A-nE65A", "U6Z1WWc0LP-U6Z1c0LP","la6bqS-la6bqS"]