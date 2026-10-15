def main(tree: list[list[dict]]):
    """
    :param tree: Stores the tree as a two dimensional array of dictionaries.
    Each dictionary contains the value of the current position and the positional
    location of it's children.
    :type tree: list[list[dict]]
    """


    # ----- WRITE YOUR SOLUTION HERE -----


if __name__ == "__main__":

    file_path = r".\python\exercise-3\input.txt"
    
    with open(file_path) as input_file:
        raw_array = [row.strip().split(" ") for row in input_file.readlines() if row != "\n"]
        
    clean_tree = []

    # ----- WRITE YOUR SOLUTION HERE -----

    main(tree=clean_tree)