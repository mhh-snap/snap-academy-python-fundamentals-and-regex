def main(puzzle_input: list[list[str]]) -> None:
    """
    :param puzzle_input: 2D Array containing puzzle grid.
    :type puzzle_input: list[list[str]]
    """
    
    # ----- WRITE YOUR SOLUTION HERE -----

if __name__ == "__main__":
    input_path = r".\python\exercise-5\input.txt"
    with open(input_path, "r") as file:
        raw_input = file.read()

    clean_input = [[char for char in row] for row in raw_input.strip().split("\n")]

    main(puzzle_input=clean_input)