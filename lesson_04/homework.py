from pathlib import Path
from typing import Generator

from pympler import asizeof

lesson_04_DIR = Path(__file__).parent
ROCKYOU_FILE = lesson_04_DIR / "rockyou.txt"


def created_file_result(result_filename: str):
    def deco(func):
        def wrapper(*args):
            with open(
                lesson_04_DIR / result_filename, "w", encoding="utf-8"
            ) as file_result:
                result = list(func(*args))
                for word in result:
                    file_result.write(word)
                print(f"Total lines in file:{len(result)}")
                print(f"Total size of file in bytes:{asizeof.asizeof(result)}")
            return result

        return wrapper

    return deco


def filtered_line(filename: Path, key_word: str) -> Generator:
    with open(filename, encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if key_word in line.lower():
                yield line


searhed_word_01 = "course"
searhed_word_02 = "hillel"

filter_result_01 = created_file_result("result_01.txt")(filtered_line)(
    ROCKYOU_FILE, searhed_word_01
)
filter_result_02 = created_file_result("result_02.txt")(filtered_line)(
    ROCKYOU_FILE, searhed_word_02
)
