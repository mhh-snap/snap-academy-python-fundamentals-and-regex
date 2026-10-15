def main(text: str):
    """
    :param text: Input text.
    :type text: str
    """


    # ----- WRITE YOUR SOLUTION HERE -----


if __name__ == "__main__":
    input_file = r".\python\exercise-2\input.txt"
    with open(input_file, "r") as file:
        raw_file = file.read()

    puzzle_input = raw_file.replace("\n", "").strip().lower()

    main(text=puzzle_input)