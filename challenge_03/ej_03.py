from pathlib import Path
from typing import Union
import re

def open_file(file: Union[str, Path]) -> list[str]:
    """
    Devuelve una lol con las palabras del archivo de texto sin espacios en blanco
    """
    with open(file, "r") as text_file:
        content = text_file.read()
        list_file = content.split("\n")
        lol_file = []
        for element in list_file:
            no_space = element.replace(" ","")
            lol_file.append(no_space.split(":"))
        return lol_file

def verify_invalid_key(lista: list[str]) -> bool:
    '''
    Recibe una lista con las políticas de las clave y la clave, y devulve un bool de si es incorrecta o no
    '''
    min = get_min(lista[0])
    max = get_max(lista[0][:-1])
    character = lista[0][-1]
    num_rep_char = count_char(lista[1], character)

    return False if min <= num_rep_char <= max else True # devuelve true si la clave es inválida

def get_min(politica_clave: str) -> int:
    '''
    Recibe la política de la clave y devuelve el mínimo de veces que debe encontrarse el carácter.
    '''
    regex = r'^\d+'
    number = re.search(regex, politica_clave)
    min = int(number.group())
    return min

def get_max(politica_clave: str) -> int:
    '''
    Recibe la política de la clave y devuelve el máximo.
    '''
    regex = r'\d+$'
    number = re.search(regex, politica_clave)
    max = int(number.group())
    return max

def count_char(clave: str, char:str) -> int:
    count = 0
    for letter in clave:
        if letter == char:
            count += 1
    
    return count

def find_invalid_key(lol: list[list[str]], pos: int) -> Union[str, Exception]:
    try:
        return lol[pos - 1][1]
    except IndexError as error:
        return error

if __name__ == "__main__":
    file_path = Path("./challenge_03/encryption_policies.txt")
    list_text = open_file(file_path)
    invalid_list = list(filter(verify_invalid_key, list_text))
    invalid_key_pos = find_invalid_key(invalid_list, 13)
    print(invalid_key_pos)
    
    