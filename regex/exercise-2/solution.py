import re


def main(card_numbers: str) -> None:
    """"""
    print(card_numbers)

    pattern = r"^(?=.*MSTM).*1357(\d)(\d)\d\2\1$"


if __name__ == "__main__":

    file_path = r".\regex\exercise-2\input.txt"
    with open(file_path, "r") as file:
        file_data = file.read().strip().replace(",", " ")

    main(card_numbers=file_data)
