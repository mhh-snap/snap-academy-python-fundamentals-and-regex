def prod(window: list[int]) -> int:
    """
    Util func to calculate product accross a window.

    :param window: Window to perform product across.
    :type window: list[int]
    :return: Product
    :rtyp: int
    """
    product = 1
    for num in window:
        product *= num
    return product

def get_largest_window(lst: list, k: int) -> list[int]:
    """
    Calculates k-window with largest product. Variation
    on classic sliding window.

    :param lst: List we perform our sliding window accross.
    :type lst: list
    :param k: Window width.
    :type k: int
    :return: k-window from lst with largest product.
    :rtype: list[int]
    """
    n = len(lst)
    first_window = lst[:k]
    largest_window = first_window
    largest_prod = prod(largest_window)

    # Check if first window has any zeros which can be skipped.
    # Sorry, variable name is kinda cheeky as we haven't neccessarily found 0 at pos 0
    last_zero_in_first_window_idx = 0
    for j in range(k):
        if first_window[j] == 0:
            last_zero_in_first_window_idx = j

    i = last_zero_in_first_window_idx + 1
    while i <= n - k:
        next_window = lst[i:i + k]
        next_product = prod(next_window)
        
        if next_product > largest_prod:
            largest_window = next_window
            largest_prod = next_product

        # Skips past any zeros
        if i + k < n and lst[i + k] == 0:
            i += k + 1
        else:
            i += 1
    
    return largest_window

def main(puzzle_input: list[int]) -> None:
    """
    :param puzzle_input: 1000-digit list of integers.
    :type puzzle_input: list[int]
    """
    largest_window = get_largest_window(lst=puzzle_input, k=13)
    print(f"largest_window: {"".join(str(num) for num in largest_window)}, product: {prod(largest_window)}")

if __name__ == "__main__":
    file_path = r".\python\exercise-4\input.txt"
    with open(file_path, "r") as file:
        raw_input = file.read()
    
    clean_input = [int(char) for char in raw_input.strip()]
    
    main(puzzle_input=clean_input)
    