def get_first_missing_pos(int_list: list[int]) -> int:
    """
    Function to calculate the smallest positive integer present in
    a list.
    
    :param int_list: List of integers.
    :type int_list: list[int]
    :return: Least positive integer not included in int_list.
    :rtype: int
    """
    list_len = len(int_list)
    int_set = set(int_list)

    for num in range(1, list_len + 1):
        if num in int_set:
            continue
        else:
            return num
        
    return list_len + 1
        
def main(puzzle_input: list[int]) -> None:
    """
    :param puzzle_input: List of integers.
    :type puzzle_input: list[int]
    """
    print(get_first_missing_pos(int_list=puzzle_input))

if __name__ == "__main__":
    input_path = r".\python\exercise-1\input.txt"
    with open(input_path, "r") as file:
        raw_input = file.read()
    
    num_list = [int(num) for num in raw_input.split("|")]

    main(puzzle_input=num_list)