def main(puzzle_input: list[int]) -> None:
    """
    :param puzzle_input: List of integers.
    :type puzzle_input: list[int]
    """


    # ----- WRITE YOUR SOLUTION HERE -----

    
if __name__ == "__main__":
    input_path = r".\python\exercise-1\input.txt"
    with open(input_path, "r") as file:
        raw_input = file.read()
    
    num_list = [int(num) for num in raw_input.split("|")]

    main(puzzle_input=num_list)