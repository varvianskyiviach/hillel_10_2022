from pathlib import Path
from typing import Generator

from pympler import asizeof

lesson_04_DIR = Path(__file__).parent
ROCKYOU_FILE = lesson_04_DIR / "rockyou.txt"


def filtered_line(filename: Path, key_word: str) -> Generator:
    with open(filename, encoding="utf-8") as file:
        while True:
            line = file.readline()

            if not line:
                break

            if key_word in line.lower():
                yield line


def created_file_result(file_name, key_word):
    with open(lesson_04_DIR / file_name, "w", encoding="utf-8") as file:
        for word in filtered_line(ROCKYOU_FILE, key_word):
            file.write(word)
    return file_name


def lines_for_file_result(file_name):
    with open(lesson_04_DIR / file_name, encoding="utf-8") as file:
        lines = file.readlines()
        print(f"Total lines in file:{len(lines)}")
        print(f"Total size of file in bytes:{asizeof.asizeof(lines)}")
        return lines


# seach_word_input = input("Please enter parameter for search: ")
seach_word_input = "cat"
seach_word_input_02 = "hillel"


file_name_01 = created_file_result("result_01.txt", seach_word_input)
file_name_02 = created_file_result("result_02.txt", seach_word_input_02)

result_01 = lines_for_file_result(file_name_01)
result_02 = lines_for_file_result(file_name_02)
