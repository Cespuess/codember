from pathlib import Path
from typing import Union

def open_file(file: Union[str, Path]) -> list[str]:
  '''
  Abre un archivo y devuelve una lista con las líneas.
  '''
  with open(file, "r") as text_file:
    content = text_file.read()
    list_file = content.split("\n")
    return list_file
  
def separated_string(list_files_name: str) -> list[str]:
  '''
  Recibe el elemento de la lista con el nombre del archivo y su checksum separados por guión, y devuelve una lista con el nombre y el checksum separados.
  '''
  file_checksum = list_files_name.split("-")
  return file_checksum

def count_char(file_name: str) -> str:
  '''
  Recibe el str con el nombre del archivo, y devuelve un str con los caracteres que solo aparezcan una vez.
  '''
  res = ''

  for char in file_name:
    count = file_name.count(char)
    if count == 1:
      res += char

  return res

def main(path_file: Union[str, Path]) -> list[str]:
  real_files = []
  list_names = open_file(path_file)
  for names_checksum in list_names:
    list_separated = separated_string(names_checksum)
    one_char_str = count_char(list_separated[0])
    if one_char_str == list_separated[1]:
      real_files.append(names_checksum)

  return real_files

if __name__ == "__main__":
  file_path = Path("./challenge_04/files_quarantine.txt")
  correct_files = main(file_path)
  print(correct_files[32])