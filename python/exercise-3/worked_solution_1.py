def largest_path(data):
    # Get the number of lists in the data
    num_lists = len(data)

    # Define an empty list to store the largest numbers
    largest_path = []

    max_index = 0
    for i in range(num_lists):
        if i == 0 or i == 1:
            max_value = max(data[i])
            max_index = data[i].index(max_value)
            largest_path.append(max_value)
        else:
            next_indices = [max_index, max_index+1]
            new_list = [data[i][next_indices[0]], data[i][next_indices[1]]]
            max_value = max(new_list)
            largest_path.append(max_value)
            max_index = data[i].index(max_value)
            while max_index not in next_indices:
                del data[i][max_index]
                max_index = data[i].index(max_value)

    total = sum(largest_path)

    return(total, largest_path)


def main(puzzle_input: list[list[int]]) -> None:
    """
    :param puzzle_input: 1000-digit list of integers.
    :type puzzle_input: list[int]
    """

    path = largest_path(puzzle_input)

    print('Largest path:', path[1])
    print('Cost of path:', path[0])


if __name__ == "__main__":

    file_path = r".\python\exercise-3\input.txt"

    with open(file_path, "r") as file:
        raw_data = [[int(num) for num in line.strip().split()] for line in file.readlines()]
        
    main(puzzle_input=raw_data)
