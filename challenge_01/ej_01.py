from pathlib import Path
from typing import Union

def open_file(file: Union[str, Path]) -> list[str]:
    """
    Devuelve una lista con las palabras del archivo de texto en minúsculas.
    """
    with open(file, "r") as text_file:
        content = text_file.read()
        list_file = content.lower().split()
        return list_file


def count_words (lista: list[str]) -> dict[str,int]:
    """
    Devuelve un diccionario con la palabra como clave y el número de veces que se repite como valor.
    """
    repetitions = {}
    for word in lista:
        if word not in repetitions:
            repetitions[word] = lista.count(word)
    return repetitions

def print_result(dict_words: dict[str,int]) -> str:
    """
    Recibe el diccionario de las repeticiones de cada palabra y lo devuelve en una cadena.
    """
    result = ""
    for clave, valor in dict_words.items():
        result += clave + str(valor)
    
    return result


if __name__ == "__main__":
    file_path = Path("./challenge_01/message_01.txt")
    list_words = open_file(file_path)
    dict_counts = count_words(list_words)
    count_str = print_result(dict_counts)
    
    
