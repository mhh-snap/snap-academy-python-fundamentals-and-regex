def main(puzzle_input: list[int]) -> None:
    """
    :param puzzle_input: 1000-digit list of integers.
    :type puzzle_input: list[int]
    """

    # ----- WRITE YOUR SOLUTION HERE -----
    

if __name__ == "__main__":
    file_path = r".\python\exercise-4\input.txt"
    with open(file_path, "r") as file:
        raw_input = file.read()
    
    clean_input = [int(char) for char in raw_input.strip()]
    
    main(puzzle_input=clean_input)