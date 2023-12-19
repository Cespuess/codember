from pathlib import Path
from typing import Union

def open_file(file: Union[str, Path]) -> str:
    """
    Devuelve una cadena con el texto del archivo.
    """
    with open(file, "r") as text_file:
        content = text_file.read()
        return content

def decoder(text: str) -> str:
    res = ""
    value = 0
    for code in text:
        if code == "#":
            value += 1
        elif code == "@":
            value -= 1
        elif code == "*":
            value = value ** 2
        else:
            res += str(value)

    return res


if __name__ == "__main__":
    file_path = Path("./challenge_02/message_02.txt")
    text = open_file(file_path)
    text_decoded = decoder(text)
    print(text_decoded)
    