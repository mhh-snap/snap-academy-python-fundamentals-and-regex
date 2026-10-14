def display_grid(grid: list[list[str]]) -> None:
    """"""
    print("\n".join("".join(char for char in row) for row in grid) + "\n")

def one_step_simulate(puzzle_grid: list[list[str]]) -> list[list[str]] | bool:
    """
    Computes the state of the puzzle grid after one step of removals.

    :param puzzle_grid: Current state of the puzzle grid.
    :type puzzle_grid: list[list[str]]
    :return: Either returns state of puzzle grid after removals or bool indicating grid has stabalised.
    :rtype: list[list[str]] | bool
    """
    updated_grid = []
    altered = False

    for row_idx, row in enumerate(puzzle_grid):
        updated_row = []
        for col_idx, char in enumerate(row):

            if row[col_idx] in {"_", "."}:
                updated_row.append(".")
                continue

            row_start = max(0, row_idx - 1)
            col_start = max(0, col_idx - 1)
            
            neighbours = [c for row_slice in puzzle_grid[row_start: row_idx + 2] for c in row_slice[col_start: col_idx + 2]]
            # I have included the current point in the neighbours list therefore
            # we need to check neighbours includes fewer than 5 rather than fewer than 4.
            if neighbours.count("^") < 5:
                updated_row.append("_")
                altered = True
            else:
                updated_row.append("^")
        
        updated_grid.append(updated_row)
    
    if not altered:
        return False
    else:
        return updated_grid

def main(puzzle_input: list[list[str]]) -> None:
    """
    :param puzzle_input: 2D Array containing puzzle grid.
    :type puzzle_input: list[list[str]]
    """
    print("Initial Step")
    display_grid(puzzle_input)

    step_count = 1
    updated_grid = one_step_simulate(puzzle_grid=puzzle_input)
    while updated_grid:
        print(f"Cleanup Step {step_count}")
        
        display_grid(updated_grid)
        updated_grid = one_step_simulate(puzzle_grid=updated_grid)
        
        step_count += 1

if __name__ == "__main__":
    input_path = r"C:\Users\MilesHoar-Hewitt\Documents\python\python-fundamentals\exercise-5\input.txt"
    with open(input_path, "r") as file:
        raw_input = file.read()

    clean_input = [[char for char in row] for row in raw_input.strip().split("\n")]

    main(puzzle_input=clean_input)