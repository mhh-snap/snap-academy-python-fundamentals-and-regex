def main(puzzle_input: list[list[int]]) -> None:
    """
    :param puzzle_input: 1000-digit list of integers.
    :type puzzle_input: list[int]
    """


    # ----- WRITE YOUR SOLUTION HERE -----


if __name__ == "__main__":

    file_path = r".\python\exercise-3\input.txt"

    with open(file_path, "r") as file:
        raw_data = [[int(num) for num in line.strip().split()] for line in file.readlines()]
        
    main(puzzle_input=raw_data)